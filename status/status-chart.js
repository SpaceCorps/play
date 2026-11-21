// Pure helpers of the status chart (no DOM): scales, ticks, line segments, labels. Tested in status-chart.test.js.

/** A y axis from 0: a "nice" step and the top, for the largest value shown (at most about 5 intervals). */
export function yScale(max) {
  const m = Math.max(max, 1);
  const raw = m / 5;
  const pow = Math.max(1, 10 ** Math.floor(Math.log10(raw))); // whole pilots: no half ticks
  const step = [1, 2, 5, 10].map((k) => k * pow).find((s) => s >= raw) ?? pow * 10;
  const top = Math.ceil(m / step) * step;
  const ticks = [];
  for (let v = 0; v <= top + step / 2; v += step) ticks.push(v);
  return { step, top, ticks };
}

const HOUR = 36e5;
// [unit, n]: every n minutes, hours, days or months, the coarsest that still gives enough labels comes last.
const STEPS = [
  ["n", 1],
  ["n", 5],
  ["n", 10],
  ["n", 15],
  ["n", 30],
  ["h", 1],
  ["h", 2],
  ["h", 3],
  ["h", 6],
  ["h", 12],
  ["d", 1],
  ["d", 2],
  ["d", 7],
  ["d", 14],
  ["m", 1],
  ["m", 2],
  ["m", 3],
  ["m", 6],
  ["m", 12],
];

/** Local-time aligned tick times (ms) inside [from, to]: the finest step that gives at most `max` ticks. */
export function timeTicks(from, to, max = 6) {
  for (const [unit, n] of STEPS) {
    const ticks = ticksOf(from, to, unit, n);
    if (ticks.length <= max) return { unit, n, ticks };
  }
  const [unit, n] = STEPS[STEPS.length - 1];
  return { unit, n, ticks: ticksOf(from, to, unit, n) };
}

function ticksOf(from, to, unit, n) {
  const out = [];
  const d = new Date(from);
  if (unit === "n") {
    d.setSeconds(0, 0);
    d.setMinutes(Math.floor(d.getMinutes() / n) * n);
    for (let t = d.getTime(); t <= to; t += n * 60e3) if (t >= from) out.push(t);
  } else if (unit === "h") {
    d.setMinutes(0, 0, 0);
    d.setHours(Math.floor(d.getHours() / n) * n);
    for (let t = d.getTime(); t <= to;) {
      if (t >= from) out.push(t);
      const next = new Date(t);
      next.setHours(next.getHours() + n);
      t = next.getTime() > t ? next.getTime() : t + n * HOUR; // a DST step must move forward
    }
  } else if (unit === "d") {
    d.setHours(0, 0, 0, 0);
    for (let t = d.getTime(); t <= to;) {
      if (t >= from) out.push(t);
      const next = new Date(t);
      next.setDate(next.getDate() + n);
      t = next.getTime();
    }
  } else {
    d.setDate(1);
    d.setHours(0, 0, 0, 0);
    d.setMonth(Math.floor(d.getMonth() / n) * n);
    for (let t = d.getTime(); t <= to;) {
      if (t >= from) out.push(t);
      const next = new Date(t);
      next.setMonth(next.getMonth() + n);
      t = next.getTime();
    }
  }
  return out;
}

/** The label of a tick: the time of day for hour steps, the date for day steps, the month for month steps (with the year in January). */
export function tickLabel(ms, unit, locale) {
  const d = new Date(ms);
  if (unit === "h" || unit === "n")
    return d.toLocaleTimeString(locale, { hour: "2-digit", minute: "2-digit", hour12: false });
  if (unit === "d") return d.toLocaleDateString(locale, { day: "numeric", month: "short" });
  return d.getMonth() === 0
    ? d.toLocaleDateString(locale, { month: "short", year: "numeric" })
    : d.toLocaleDateString(locale, { month: "short" });
}

/** "5 minutes", "2 hours", "day": the width of one point. */
export function stepLabel(seconds) {
  if (seconds < 3600) return seconds === 60 ? "minute" : `${seconds / 60} minutes`;
  if (seconds < 86400) return seconds === 3600 ? "hour" : `${seconds / 3600} hours`;
  return seconds === 86400 ? "day" : seconds === 604800 ? "week" : `${seconds / 86400} days`;
}

/**
 * Splits a series into runs that are drawn as one line. A hole (a gap longer than 1.5 steps), a point
 * with no value and a point where the server was down all end a run.
 * `points` are [t, avg, max, up]; `x` and `y` map time (s) and value to pixels.
 */
export function runs(points, step, x, y) {
  const out = [];
  let run = [];
  let last = null;
  for (const [t, avg, , up] of points) {
    const down = up <= 0;
    if (down || (last !== null && t - last > step * 1.5)) {
      if (run.length) out.push(run);
      run = [];
    }
    if (!down) run.push([x(t), y(avg)]);
    last = t;
  }
  if (run.length) out.push(run);
  return out;
}

/** SVG path data of a run (one decimal is plenty for pixels). */
export function pathOf(run) {
  return run.map(([px, py], i) => `${i ? "L" : "M"}${px.toFixed(1)} ${py.toFixed(1)}`).join("");
}

/** The index in the sorted list `ts` of the time nearest to `t`. */
export function nearest(ts, t) {
  let lo = 0;
  let hi = ts.length - 1;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (ts[mid] < t) lo = mid + 1;
    else hi = mid;
  }
  return lo > 0 && Math.abs(ts[lo - 1] - t) <= Math.abs(ts[lo] - t) ? lo - 1 : lo;
}

/** The number as shown: whole numbers when large, one decimal for a small mean. */
export function fmtNum(v) {
  return v >= 10 || Number.isInteger(v) ? String(Math.round(v)) : v.toFixed(1);
}

/** What a point on the platform view is called. */
export const PLATFORM_NAMES = {
  steam: "Steam",
  desktop: "Desktop",
  ios: "iOS",
  android: "Android",
  web: "Web",
  unknown: "Unknown",
};

/**
 * What the chart draws, from the answer of the plain view: the total as an area, a line per server, and
 * the times at which some server was not up. `color(id, i)` gives a line its colour.
 * A line is { id, name, color, pts: [[t, mean, peak, up_share], ...] }.
 */
export function serverModel(json, color) {
  const down = new Set();
  for (const [id, pts] of Object.entries(json.series))
    if (id !== "total") for (const p of pts) if (p[3] < 1) down.add(p[0]);
  return {
    kind: "server",
    step: json.step,
    from: json.from,
    totalName: "All servers",
    total: json.series.total ?? [],
    lines: json.servers
      .filter((s) => s.id !== "total")
      .map((s, i) => ({ id: s.id, name: s.name, color: color(s.id, i), pts: json.series[s.id] ?? [] })),
    down: [...down].sort((a, b) => a - b),
  };
}

/**
 * The same, from the answer of `by=platform`, for one server (`scope`) or all of them (`"total"`): a line
 * per client, and the sum of the clients as the area. The points are [t, mean, peak, 1]: whether a server
 * was down comes from `json.down`, not from the points.
 */
export function platformModel(json, scope, color) {
  const mine = json.series[scope] ?? {};
  const lines = (json.platforms ?? []).map((id) => ({
    id,
    name: PLATFORM_NAMES[id] ?? id,
    color: color(id),
    pts: (mine[id] ?? []).map(([t, mean, peak]) => [t, mean, peak, 1]),
  }));
  const sum = new Map();
  for (const l of lines) for (const [t, mean] of l.pts) sum.set(t, (sum.get(t) ?? 0) + mean);
  const total = [...sum]
    .sort((a, b) => a[0] - b[0])
    .map(([t, v]) => [t, Math.round(v * 10) / 10, Math.round(v * 10) / 10, 1]);
  const ids = scope === "total" ? Object.keys(json.down ?? {}).filter((id) => id !== "total") : [scope];
  const down = new Set();
  for (const id of ids) for (const [t] of json.down?.[id] ?? []) down.add(t);
  const server = (json.servers ?? []).find((s) => s.id === scope);
  return {
    kind: "platform",
    step: json.step,
    from: json.from,
    totalName: scope === "total" ? "All servers" : (server?.name ?? scope),
    total,
    lines,
    down: [...down].sort((a, b) => a - b),
  };
}
