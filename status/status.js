// The status page: players online per server over time. The numbers come from the SpaceCorps status service
// (https://spacecorps.tech/api/status/series, read-only, no cookies; see data-endpoint in index.html).
// Plain SVG, no library, no build step. All text from the API goes in with textContent.
import {
  fmtNum,
  nearest,
  pathOf,
  runs,
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

let range = "day";
let data = null;
let cursor = -1; // index into the master times, -1: none
const cache = new Map();

/* ---- data ---- */
async function load(r, { quiet = false } = {}) {
  if (!quiet) plot.classList.add("busy");
  try {
    const res = await fetch(`${ENDPOINT}?range=${r}`, { headers: { accept: "application/json" } });
    if (!res.ok) throw new Error(String(res.status));
    const json = await res.json();
    cache.set(r, json);
    if (r === range) show(json);
  } catch {
    if (r === range && !cache.has(r)) fail();
  } finally {
    if (r === range) plot.classList.remove("busy");
  }
}

function select(r) {
  range = r;
  for (const b of buttons) b.setAttribute("aria-pressed", String(b.dataset.range === r));
  if (cache.has(r)) show(cache.get(r)); // keep the frame while it refreshes
  load(r);
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

function renderNow(json) {
  nowEl.replaceChildren(
    ...json.servers.map((s, i) => {
      const tile = h("div", "st-tile");
      tile.dataset.id = s.id;
      const key = h("span", s.id === "total" ? "st-key total" : "st-key");
      key.style.setProperty("--c", colorOf(s.id, i));
      key.setAttribute("aria-hidden", "true");
      const name = h("span", "st-name");
      name.append(key, document.createTextNode(s.name));
      const value = h("span", "st-value", s.up ? String(s.online) : "0");
      const state = h("span", s.up ? "st-state up" : "st-state down");
      state.textContent =
        s.id === "total" ? (s.up ? "online now" : "offline") : s.up ? "up" : s.status || "down";
      tile.append(name, value, state);
      return tile;
    }),
  );
}

/* ---- the chart ---- */
function show(json) {
  data = json;
  renderNow(json);
  renderChart();
  renderTable();
  const first = json.since ? new Date(json.since * 1000) : null;
  caption.textContent = `${CAPTION[range]} · one point per ${stepLabel(json.step)}`;
  const parts = [];
  if (first) {
    const cut = range !== "all" && json.since > json.generated - WINDOW_S[range];
    parts.push(
      `Recording started ${first.toLocaleString(LOCALE, { dateStyle: "medium", timeStyle: "short" })}.${cut ? " Nothing was recorded before that, so this range starts there." : " Nothing exists before that."}`,
    );
  }
  parts.push(
    "Players are pilots connected to a server, menus included. Each point is the average over its width; the tooltip also shows the peak. Times are in your time zone.",
  );
  note.textContent = parts.join(" ");
}

function geometry() {
  const w = Math.max(280, Math.floor(plot.clientWidth));
  const hgt = w < 520 ? 260 : 340;
  return { w, h: hgt, l: w < 520 ? 34 : 42, r: 12, t: 14, b: 28 };
}

function renderChart() {
  const json = data;
  if (!json) return;
  const total = json.series.total ?? [];
  if (!total.length) {
    plot.replaceChildren(
      h("p", "st-msg", "No samples recorded yet. The first one arrives within a minute."),
    );
    return;
  }
  const g = geometry();
  // the line runs from the first to the newest point; one point alone gets half a step each side
  const last = total[total.length - 1][0];
  const from = last > json.from ? json.from : json.from - json.step / 2;
  const to = last > json.from ? last : json.from + json.step / 2;
  const x = (t) => g.l + ((t - from) / (to - from)) * (g.w - g.l - g.r);
  const peak = Math.max(1, ...Object.values(json.series).flatMap((s) => s.map((p) => p[1])));
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
  const wPx = Math.max(1.5, x(from + json.step) - x(from));
  const downAt = new Set();
  for (const [id, pts] of Object.entries(json.series))
    if (id !== "total") for (const p of pts) if (p[3] < 1) downAt.add(p[0]);
  for (const t of downAt)
    svg.append(
      el("rect", { x: x(t) - wPx / 2, y: g.t, width: wPx, height: g.h - g.t - g.b, class: "down" }),
    );
  // total: an area with a line, then the servers on top
  const area = runs(total, json.step, x, y);
  for (const run of area) {
    if (run.length > 1)
      svg.append(
        el("path", {
          d: `${pathOf(run)}L${run[run.length - 1][0].toFixed(1)} ${y(0)}L${run[0][0].toFixed(1)} ${y(0)}Z`,
          class: "area",
        }),
      );
  }
  const order = ["total", ...json.servers.filter((s) => s.id !== "total").map((s) => s.id)];
  order.forEach((id, i) => {
    const pts = json.series[id] ?? [];
    const color = colorOf(id, i - 1);
    for (const run of runs(pts, json.step, x, y)) {
      if (run.length === 1)
        svg.append(el("circle", { cx: run[0][0], cy: run[0][1], r: 2.5, fill: color }));
      else
        svg.append(
          el("path", {
            d: pathOf(run),
            class: id === "total" ? "line total" : "line",
            stroke: color,
          }),
        );
    }
  });
  // hover layer
  const cross = el("line", { y1: g.t, y2: g.h - g.b, class: "cross", visibility: "hidden" });
  const dots = order.map((id, i) =>
    el("circle", { r: 4, class: "dot", fill: colorOf(id, i - 1), visibility: "hidden" }),
  );
  svg.append(cross, ...dots);
  plot.replaceChildren(svg, tip);

  const times = total.map((p) => p[0]);
  const at = (id, t) => (json.series[id] ?? []).find((p) => p[0] === t);
  const place = (idx) => {
    cursor = idx;
    const t = times[idx];
    const px = x(t);
    cross.setAttribute("x1", px);
    cross.setAttribute("x2", px);
    cross.setAttribute("visibility", "visible");
    order.forEach((id, i) => {
      const p = at(id, t);
      if (p && p[3] > 0) {
        dots[i].setAttribute("cx", x(t));
        dots[i].setAttribute("cy", y(p[1]));
        dots[i].setAttribute("visibility", "visible");
      } else dots[i].setAttribute("visibility", "hidden");
    });
    fillTip(t, order, at);
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

function fillTip(t, order, at) {
  const rows = [
    h(
      "div",
      "st-tip-time",
      new Date(t * 1000).toLocaleString(LOCALE, { dateStyle: "medium", timeStyle: "short" }),
    ),
  ];
  order.forEach((id, i) => {
    const p = at(id, t);
    const server = data.servers.find((s) => s.id === id);
    const row = h("div", "st-tip-row");
    const key = h("span", id === "total" ? "st-key total" : "st-key");
    key.style.setProperty("--c", colorOf(id, i - 1));
    const name = h("span", "st-tip-name", server ? server.name : id);
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
  tip.replaceChildren(...rows);
}

/* ---- the table view: every value without hovering ---- */
function renderTable() {
  if (!details.open || !data) return;
  const order = data.servers.map((s) => s.id);
  const table = h("table");
  const head = h("tr");
  head.append(h("th", "", "Time"), ...data.servers.map((s) => h("th", "num", s.name)));
  const thead = h("thead");
  thead.append(head);
  table.append(thead);
  const body = h("tbody");
  const byId = Object.fromEntries(
    order.map((id) => [id, new Map((data.series[id] ?? []).map((p) => [p[0], p]))]),
  );
  for (const p of (data.series.total ?? []).slice().reverse()) {
    const tr = h("tr");
    tr.append(
      h(
        "td",
        "",
        new Date(p[0] * 1000).toLocaleString(LOCALE, { dateStyle: "short", timeStyle: "short" }),
      ),
    );
    for (const id of order) {
      const q = byId[id].get(p[0]);
      tr.append(h("td", "num", !q ? "–" : q[3] <= 0 ? "down" : fmtNum(q[1])));
    }
    body.append(tr);
  }
  table.append(body);
  tableBox.replaceChildren(table);
}

/* ---- wiring ---- */
for (const b of buttons) b.addEventListener("click", () => select(b.dataset.range));
details.addEventListener("toggle", renderTable);
let resizeTimer = 0;
new ResizeObserver(() => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(renderChart, 80);
}).observe(plot);
setInterval(() => {
  if (!document.hidden) load(range, { quiet: true });
}, 60_000);
select("day");
