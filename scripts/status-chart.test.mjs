// Tests of the status page's chart helpers (status/status-chart.js). No dependencies: `node --test scripts/`.
import assert from "node:assert/strict";
import test from "node:test";
import { fmtNum, nearest, pathOf, runs, stepLabel, tickLabel, timeTicks, yScale } from "../status/status-chart.js";

test("yScale starts at 0 and gives a round top at most five intervals high", () => {
  assert.deepEqual(yScale(0), { step: 1, top: 1, ticks: [0, 1] });
  assert.deepEqual(yScale(35).ticks, [0, 10, 20, 30, 40]);
  assert.equal(yScale(44).top, 50);
  assert.deepEqual(yScale(120).ticks, [0, 50, 100, 150]);
  assert.deepEqual(yScale(3000).ticks, [0, 1000, 2000, 3000]);
  for (const m of [1, 2, 7, 13, 99, 101, 640, 9999]) {
    const s = yScale(m);
    assert.ok(s.top >= m, `top covers ${m}`);
    assert.ok(s.ticks.length <= 6, `few ticks for ${m}`);
  }
});

test("timeTicks aligns to the clock and keeps the label count down", () => {
  const from = new Date(2026, 10, 20, 14, 7).getTime();
  const day = timeTicks(from, from + 24 * 36e5);
  assert.equal(day.unit, "h");
  assert.ok(day.ticks.length <= 6);
  for (const t of day.ticks) assert.equal(new Date(t).getMinutes(), 0);
  const week = timeTicks(from, from + 7 * 864e5);
  assert.equal(week.unit, "d");
  for (const t of week.ticks) assert.equal(new Date(t).getHours(), 0);
  const year = timeTicks(from, from + 365 * 864e5);
  assert.equal(year.unit, "m");
  assert.ok(year.ticks.length <= 6);
  for (const t of year.ticks) assert.equal(new Date(t).getDate(), 1);
  // a young install has a window of minutes: it gets minute ticks, on the clock
  const young = timeTicks(from, from + 13 * 60e3);
  assert.equal(young.unit, "n");
  assert.ok(young.ticks.length > 1);
  for (const t of young.ticks) assert.equal(new Date(t).getMinutes() % young.n, 0);
  assert.doesNotThrow(() => timeTicks(from, from + 30e3));
});

test("tickLabel is the clock, the date or the month", () => {
  const t = new Date(2027, 0, 5, 9, 30).getTime();
  assert.equal(tickLabel(t, "h", "en-GB"), "09:30");
  assert.equal(tickLabel(t, "d", "en-GB"), "5 Jan");
  assert.equal(tickLabel(new Date(2027, 0, 1).getTime(), "m", "en-GB"), "Jan 2027");
  assert.equal(tickLabel(new Date(2027, 3, 1).getTime(), "m", "en-GB"), "Apr");
});

test("stepLabel names the width of a point", () => {
  assert.deepEqual(
    [60, 300, 1800, 3600, 7200, 21600, 86400, 604800].map(stepLabel),
    ["minute", "5 minutes", "30 minutes", "hour", "2 hours", "6 hours", "day", "week"],
  );
});

test("runs break at holes and at downtime", () => {
  const id = (v) => v;
  const pts = [[0, 1, 1, 1], [300, 2, 2, 1], [600, 3, 3, 1], [3000, 4, 4, 1], [3300, 5, 5, 1], [3600, 0, 0, 0], [3900, 6, 6, 1]];
  assert.deepEqual(runs(pts, 300, id, id), [[[0, 1], [300, 2], [600, 3]], [[3000, 4], [3300, 5]], [[3900, 6]]]);
  assert.deepEqual(runs([], 300, id, id), []);
  assert.deepEqual(runs([[0, 1, 1, 0]], 300, id, id), []);
});

test("a partly down bucket is still drawn", () => {
  const id = (v) => v;
  assert.deepEqual(runs([[0, 5, 9, 0.4]], 300, id, id), [[[0, 5]]]);
});

test("pathOf writes SVG path data", () => {
  assert.equal(pathOf([[0, 10], [5.55, 20.04]]), "M0.0 10.0L5.5 20.0");
  assert.equal(pathOf([]), "");
});

test("nearest finds the closest time", () => {
  const ts = [0, 100, 200, 400];
  assert.deepEqual([-5, 40, 60, 290, 310, 9999].map((t) => nearest(ts, t)), [0, 0, 1, 2, 3, 3]);
  assert.equal(nearest([7], 3), 0);
});

test("fmtNum keeps small means readable", () => {
  assert.deepEqual([0, 3, 3.14, 12.6, 1234.4].map(fmtNum), ["0", "3", "3.1", "13", "1234"]);
});
