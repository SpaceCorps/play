// The status page: players online over time, per server or per platform (Steam, desktop, iOS, Android).
// The numbers come from the SpaceCorps status service (https://spacecorps.tech/api/status/series, read-only,
// no cookies; see data-endpoint in index.html). Plain SVG, no library, no build step. All text from the API
// goes in with textContent.
import {
  fmtNum,
  nearest,
  pathOf,
  platformModel,
  runs,
  serverModel,
  stepLabel,
  tickLabel,
  timeTicks,
  yScale,
} from "./status-chart.js";

const root = document.getElementById("status");
const ENDPOINT = root.dataset.endpoint;
const SVG = "http://www.w3.org/2000/svg";
const LOCALE = undefined; // the visitor's own
const CAPTION = {
  day: "Last 24 hours",
  week: "Last 7 days",
  month: "Last 30 days",
  quarter: "Last 3 months",
  year: "Last year",
  all: "Since the very beginning",
};
const WINDOW_S = {
  day: 86400,
  week: 7 * 86400,
  month: 30 * 86400,
  quarter: 91 * 86400,
  year: 365 * 86400,
};
// Colour follows the server, never its rank: the known ones have a fixed slot, a new one takes the next free slot.
const SLOTS = { home: 1, "singapore-1": 2, "us-east-1": 3 };
// The same for platforms: a platform keeps its colour in every range and for every server.
const PLATFORM_COLORS = {
  steam: "var(--st-c1)",
  desktop: "var(--st-c2)",
  android: "var(--st-c3)",
  web: "var(--st-c4)",
  ios: "var(--st-c6)",
  unknown: "var(--text-3)",
};

const el = (name, attrs = {}, text) => {
  const e = document.createElementNS(SVG, name);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (text !== undefined) e.textContent = text;
  return e;
};
const h = (tag, cls, text) => {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text !== undefined) e.textContent = text;
  return e;
};

const nowEl = root.querySelector("#st-now");
const plot = root.querySelector("#st-plot");
const caption = root.querySelector("#st-caption");
const note = root.querySelector("#st-note");
const tableBox = root.querySelector("#st-table");
const details = root.querySelector("details");
const buttons = [...root.querySelectorAll("[data-range]")];
const viewBox = root.querySelector("#st-view");
const viewButtons = [...root.querySelectorAll("[data-view]")];
const scopeBox = root.querySelector("#st-scope");

let range = "day";
let view = "server"; // "server": a line per server; "platform": a line per platform
let scope = "total"; // the platform view: one server's id, or "total" for all of them
let hasPlatform = false; // the game reports the split: only then is the switch offered
let data = null; // the answer on show
let model = null; // what the chart draws, built from it
let cursor = -1; // index into the master times, -1: none
const cache = new Map(); // "view:range" -> the last answer

const when = (s) =>
  new Date(s * 1000).toLocaleString(LOCALE, { dateStyle: "medium", timeStyle: "short" });

/* ---- data ---- */
async function load(r, v, { quiet = false } = {}) {
  const key = `${v}:${r}`;
  const current = () => r === range && v === view;
  if (!quiet && current()) plot.classList.add("busy");
  try {
    const res = await fetch(`${ENDPOINT}?range=${r}${v === "platform" ? "&by=platform" : ""}`, {
      headers: { accept: "application/json" },
    });
    if (!res.ok) throw new Error(String(res.status));
    const json = await res.json();
    cache.set(key, json);
    if (v === "server" && json.platform_since && !hasPlatform) {
      hasPlatform = true;
      syncControls();
    }
    if (current()) show(json);
  } catch {
    if (current() && !cache.has(key)) fail();
  } finally {
    if (current()) plot.classList.remove("busy");
  }
}

function select(r) {
  range = r;
  for (const b of buttons) b.setAttribute("aria-pressed", String(b.dataset.range === r));
  const key = `${view}:${r}`;
  if (cache.has(key)) show(cache.get(key)); // keep the frame while it refreshes
  load(r, view);
}

function setView(v) {
  view = v;
  syncControls();
  const key = `${v}:${range}`;
  if (cache.has(key)) show(cache.get(key));
  else plot.replaceChildren(h("p", "st-msg", "Loading…"));
  load(range, v);
}

function syncControls() {
  viewBox.hidden = !hasPlatform;
  for (const b of viewButtons) b.setAttribute("aria-pressed", String(b.dataset.view === view));
  scopeBox.hidden = !(hasPlatform && view === "platform");
}

function fail() {
  plot.replaceChildren(
    h("p", "st-msg", "The history is not available right now. Try again in a minute."),
  );
  caption.textContent = "";
}

/* ---- the numbers now (they double as the legend) ---- */
function colorOf(id, i) {
  return id === "total" ? "var(--st-ink)" : `var(--st-c${SLOTS[id] ?? 4 + (i % 3)})`;
}
const platformColor = (id) => PLATFORM_COLORS[id] ?? "var(--text-3)";

function tile(color, name, value, state, stateClass) {
  const t = h("div", "st-tile");
  const key = h("span", color === "var(--st-ink)" ? "st-key total" : "st-key");
  key.style.setProperty("--c", color);
  key.setAttribute("aria-hidden", "true");
  const label = h("span", "st-name");
  label.append(key, document.createTextNode(name));
  t.append(label, h("span", "st-value", value), h("span", stateClass, state));
  return t;
}

function renderNow() {
  nowEl.classList.toggle("by-platform", view === "platform");
  if (view === "platform") return renderNowPlatform();
  nowEl.replaceChildren(
    ...data.servers.map((s, i) => {
      const t = tile(
        colorOf(s.id, i),
        s.name,
        s.up ? String(s.online) : "0",
        s.id === "total" ? (s.up ? "online now" : "offline") : s.up ? "up" : s.status || "down",
        s.up ? "st-state up" : "st-state down",
      );
      t.dataset.id = s.id;
      return t;
    }),
  );
}

// One tile for the server (or all of them), then one per platform with its share of the pilots now.
function renderNowPlatform() {
  const s = data.servers.find((x) => x.id === scope);
  if (!s) return nowEl.replaceChildren();
  const tiles = [
    tile(
      "var(--st-ink)",
      scope === "total" ? "All servers" : s.name,
      s.up ? String(s.online) : "0",
      scope === "total" ? (s.up ? "online now" : "offline") : s.up ? "up" : s.status || "down",
      s.up ? "st-state up" : "st-state down",
    ),
  ];
  if (!s.platforms) {
    tiles.push(
      h(
        "p",
        "st-note st-now-note",
        scope === "total"
          ? "No server reports pilots by platform yet."
          : `${s.name} does not report pilots by platform yet.`,
      ),
    );
  } else {
    for (const l of model.lines) {
      const n = s.platforms[l.id] ?? 0;
      const share = s.online > 0 ? `${Math.round((100 * n) / s.online)}% of pilots` : "–";
      const t = tile(l.color, l.name, String(n), share, "st-state plain");
      t.dataset.id = l.id;
      tiles.push(t);
    }
  }
  nowEl.replaceChildren(...tiles);
}

/* ---- the chart ---- */
function show(json) {
  if (view === "platform" && json.by !== "platform") return fail(); // an API that does not know the view
  data = json;
  if (view === "platform") {
    if (!json.servers.some((s) => s.id === scope)) scope = "total";
    model = platformModel(json, scope, platformColor);
    renderScopes(json);
  } else {
    model = serverModel(json, colorOf);
  }
  plot.setAttribute(
    "aria-label",
    `Line chart of players online per ${view === "platform" ? "platform" : "server"}. Use the left and right arrow keys to read values, or open the table below.`,
  );
  renderNow();
  renderChart();
  renderTable();
  const rangeName =
    view === "platform" && range === "all"
      ? "Since the game began reporting platforms"
      : CAPTION[range];
  caption.textContent = `${rangeName}${view === "platform" ? " · by platform" : ""} · one point per ${stepLabel(json.step)}`;
  renderNote(json);
}

function renderNote(json) {
  const parts = [];
  if (view === "platform") {
    parts.push(
      json.since
        ? `The game began reporting pilots by platform on ${when(json.since)}, so this view starts there; nothing earlier can be split.`
        : "The game does not report pilots by platform yet. This view fills in as soon as it does.",
      `Desktop is the native game outside Steam; Unknown is a build the game does not recognise.${scope === "total" ? " Pilots on a server that does not report the split yet count as Unknown." : ""}`,
    );
  } else if (json.since) {
    const cut = range !== "all" && json.since > json.generated - WINDOW_S[range];
    parts.push(
      `Recording started ${when(json.since)}.${cut ? " Nothing was recorded before that, so this range starts there." : " Nothing exists before that."}`,
    );
  }
  parts.push(
    "Players are pilots connected to a server, menus included. Each point is the average over its width; the tooltip also shows the peak. Times are in your time zone.",
  );
  note.textContent = parts.join(" ");
}

// The platform view's second row: all servers, or one of them.
function renderScopes(json) {
  scopeBox.replaceChildren(
    ...json.servers.map((s) => {
      const b = h("button", "", s.id === "total" ? "All servers" : s.name);
      b.type = "button";
      b.dataset.scope = s.id;
      b.setAttribute("aria-pressed", String(s.id === scope));
      return b;
    }),
  );
}

function geometry() {
  const w = Math.max(280, Math.floor(plot.clientWidth));
  const hgt = w < 520 ? 260 : 340;
  return { w, h: hgt, l: w < 520 ? 34 : 42, r: 12, t: 14, b: 28 };
}

function emptyMessage() {
  if (model.kind !== "platform")
    return "No samples recorded yet. The first one arrives within a minute.";
  if (!data.since)
    return "The game does not report pilots by platform yet. This view fills in as soon as it does.";
  return scope === "total"
    ? "No pilots by platform are recorded in this range yet."
    : `${model.totalName} has not reported pilots by platform in this range.`;
}

function renderChart() {
  if (!model) return;
  const total = model.total;
  if (!total.length) {
    plot.replaceChildren(h("p", "st-msg", emptyMessage()));
    return;
  }
  const g = geometry();
  // the line runs from the first to the newest point; one point alone gets half a step each side
  const last = total[total.length - 1][0];
  const from = last > model.from ? model.from : model.from - model.step / 2;
  const to = last > model.from ? last : model.from + model.step / 2;
  const x = (t) => g.l + ((t - from) / (to - from)) * (g.w - g.l - g.r);
  // the area (the sum) first, then a line each
  const order = [
    { id: "total", name: model.totalName, color: "var(--st-ink)", pts: total },
    ...model.lines,
  ];
  const peak = Math.max(1, ...order.flatMap((l) => l.pts.map((p) => p[1])));
  const ys = yScale(peak);
  const y = (v) => g.t + (1 - v / ys.top) * (g.h - g.t - g.b);

  const svg = el("svg", {
    viewBox: `0 0 ${g.w} ${g.h}`,
    width: g.w,
    height: g.h,
    "aria-hidden": "true",
  });
  // grid and y labels
  for (const v of ys.ticks) {
    svg.append(
      el("line", { x1: g.l, x2: g.w - g.r, y1: y(v), y2: y(v), class: v === 0 ? "axis" : "grid" }),
    );
    svg.append(
      el("text", { x: g.l - 8, y: y(v) + 4, class: "tick", "text-anchor": "end" }, String(v)),
    );
  }
  // x labels
  const tk = timeTicks(from * 1000, to * 1000, g.w < 520 ? 4 : 6);
  for (const t of tk.ticks) {
    const px = x(t / 1000);
    if (px < g.l - 1 || px > g.w - g.r + 1) continue;
    svg.append(el("line", { x1: px, x2: px, y1: g.h - g.b, y2: g.h - g.b + 4, class: "axis" }));
    svg.append(
      el(
        "text",
        {
          x: px,
          y: g.h - 8,
          class: "tick",
          "text-anchor": px < g.l + 18 ? "start" : px > g.w - g.r - 18 ? "end" : "middle",
        },
        tickLabel(t, tk.unit, LOCALE),
      ),
    );
  }
  // buckets in which a server was down or updating
  const wPx = Math.max(1.5, x(from + model.step) - x(from));
  for (const t of model.down)
    svg.append(
      el("rect", { x: x(t) - wPx / 2, y: g.t, width: wPx, height: g.h - g.t - g.b, class: "down" }),
    );
  // total: an area with a line, then the lines on top
  for (const run of runs(total, model.step, x, y)) {
    if (run.length > 1)
      svg.append(
        el("path", {
          d: `${pathOf(run)}L${run[run.length - 1][0].toFixed(1)} ${y(0)}L${run[0][0].toFixed(1)} ${y(0)}Z`,
          class: "area",
        }),
      );
  }
  for (const item of order) {
    for (const run of runs(item.pts, model.step, x, y)) {
      if (run.length === 1)
        svg.append(el("circle", { cx: run[0][0], cy: run[0][1], r: 2.5, fill: item.color }));
      else
        svg.append(
          el("path", {
            d: pathOf(run),
            class: item.id === "total" ? "line total" : "line",
            stroke: item.color,
          }),
        );
    }
  }
  // hover layer
  const cross = el("line", { y1: g.t, y2: g.h - g.b, class: "cross", visibility: "hidden" });
  const dots = order.map((item) =>
    el("circle", { r: 4, class: "dot", fill: item.color, visibility: "hidden" }),
  );
  svg.append(cross, ...dots);
  plot.replaceChildren(svg, tip);

  const times = total.map((p) => p[0]);
  const lookup = order.map((item) => new Map(item.pts.map((p) => [p[0], p])));
  const downAt = new Set(model.down);
  const place = (idx) => {
    cursor = idx;
    const t = times[idx];
    const px = x(t);
    cross.setAttribute("x1", px);
    cross.setAttribute("x2", px);
    cross.setAttribute("visibility", "visible");
    order.forEach((_, i) => {
      const p = lookup[i].get(t);
      if (p && p[3] > 0) {
        dots[i].setAttribute("cx", x(t));
        dots[i].setAttribute("cy", y(p[1]));
        dots[i].setAttribute("visibility", "visible");
      } else dots[i].setAttribute("visibility", "hidden");
    });
    fillTip(t, order, lookup, downAt.has(t));
    tip.hidden = false;
    const tw = tip.offsetWidth;
    tip.style.left = `${Math.min(Math.max(px + 14 > g.w - tw ? px - tw - 14 : px + 14, 4), g.w - tw - 4)}px`;
    tip.style.top = `${g.t + 4}px`;
  };
  const hide = () => {
    cursor = -1;
    cross.setAttribute("visibility", "hidden");
    for (const d of dots) d.setAttribute("visibility", "hidden");
    tip.hidden = true;
  };
  plot.onpointermove = (e) => {
    const r = svg.getBoundingClientRect();
    const t = from + ((e.clientX - r.left - g.l) / (g.w - g.l - g.r)) * (to - from);
    place(nearest(times, t));
  };
  plot.onpointerleave = hide;
  plot.onfocus = () => place(cursor >= 0 ? cursor : times.length - 1);
  plot.onblur = hide;
  plot.onkeydown = (e) => {
    if (e.key === "ArrowLeft") place(Math.max(0, (cursor < 0 ? times.length - 1 : cursor) - 1));
    else if (e.key === "ArrowRight")
      place(Math.min(times.length - 1, (cursor < 0 ? times.length - 1 : cursor) + 1));
    else if (e.key === "Escape") hide();
    else return;
    e.preventDefault();
  };
  if (cursor >= 0 && cursor < times.length) place(cursor);
}

const tip = h("div", "st-tip");
tip.hidden = true;
tip.setAttribute("aria-hidden", "true");

function fillTip(t, order, lookup, wasDown) {
  const rows = [h("div", "st-tip-time", when(t))];
  order.forEach((item, i) => {
    const p = lookup[i].get(t);
    const row = h("div", "st-tip-row");
    const key = h("span", item.id === "total" ? "st-key total" : "st-key");
    key.style.setProperty("--c", item.color);
    const name = h("span", "st-tip-name", item.name);
    let value;
    if (!p) value = "no data";
    else if (p[3] <= 0) value = "down";
    else
      value =
        fmtNum(p[1]) +
        (p[2] > p[1] + 0.05 ? ` (peak ${p[2]})` : "") +
        (p[3] < 1 ? ` · up ${Math.floor(p[3] * 100)}%` : "");
    row.append(key, name, h("strong", "st-tip-val", value));
    rows.push(row);
  });
  // the platform view has no per-point uptime: say it when the red band is under the pointer
  if (wasDown && model.kind === "platform")
    rows.push(h("div", "st-tip-time", "A server was down or updating part of this time."));
  tip.replaceChildren(...rows);
}

/* ---- the table view: every value without hovering ---- */
function renderTable() {
  if (!details.open || !model) return;
  const order = [{ name: model.totalName, pts: model.total }, ...model.lines];
  const table = h("table");
  const head = h("tr");
  head.append(h("th", "", "Time"), ...order.map((l) => h("th", "num", l.name)));
  const thead = h("thead");
  thead.append(head);
  table.append(thead);
  const body = h("tbody");
  const byLine = order.map((l) => new Map(l.pts.map((p) => [p[0], p])));
  for (const p of model.total.slice().reverse()) {
    const tr = h("tr");
    tr.append(
      h(
        "td",
        "",
        new Date(p[0] * 1000).toLocaleString(LOCALE, { dateStyle: "short", timeStyle: "short" }),
      ),
    );
    for (const m of byLine) {
      const q = m.get(p[0]);
      tr.append(h("td", "num", !q ? "–" : q[3] <= 0 ? "down" : fmtNum(q[1])));
    }
    body.append(tr);
  }
  table.append(body);
  tableBox.replaceChildren(table);
}

/* ---- wiring ---- */
for (const b of buttons) b.addEventListener("click", () => select(b.dataset.range));
for (const b of viewButtons)
  b.addEventListener("click", () => {
    if (b.dataset.view !== view) setView(b.dataset.view);
  });
scopeBox.addEventListener("click", (e) => {
  const b = e.target.closest("[data-scope]");
  if (!b || !data || b.dataset.scope === scope) return;
  scope = b.dataset.scope;
  show(data);
  scopeBox.querySelector(`[data-scope="${CSS.escape(scope)}"]`)?.focus(); // the buttons were rebuilt
});
details.addEventListener("toggle", renderTable);
let resizeTimer = 0;
new ResizeObserver(() => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(renderChart, 80);
}).observe(plot);
setInterval(() => {
  if (!document.hidden) load(range, view, { quiet: true });
}, 60_000);
select("day");
