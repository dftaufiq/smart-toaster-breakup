# Leaderboard Top 10 — Unplugged: A Smart Toaster's Breakup Line

Slug: `u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92`
Fetched: 2026-11-25 ~11:10 WIB (`GET /api/competitions/<slug>/leaderboard?rows=all`,
saved as `leaderboard.json` in this folder; full competition detail in `detail.json`)

## Board state — BLIND rounds, no scores visible

- **rank_key:** `judge` (Judge win rate, Bradley-Terry over pairwise games)
- **tie_break:** `bytes` (Size, lower is better) — ties on judge win rate go to the
  entry that took more playoff games between the tied entries, then to the smaller
  text (fewer bytes), then to the earlier receipt.
- **submission_rule:** Force_Last (a new submit replaces the old entry)
- **phase:** dev, `scores_visible: false`, `placements_held: true` — the leaderboard
  returns **zero entries**; no rank/score is visible for anyone until a round is judged.
- **Submissions at discovery:** 151; at build time (11:10 WIB): **243** and growing.
- **Prize:** $2 total, top 8 paid (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22,
  5th $0.15, 6th $0.11, 7th $0.07, 8th $0.05).
- **Rounds (blind, 3x):** R1 2026-11-25 15:16:05 UTC (22:16 WIB), R2 2026-11-26
  02:55:32 UTC (09:55 WIB), final = deadline 2026-11-26 14:35:00 UTC (21:35 WIB).
- **Final heat: top 500** on the dev board (RULES.txt: "the 500 entrants ranked
  highest on the development leaderboard ... hold the heat's 500 seats. The seats
  are exactly 500"). While blind rounds run, each interim round draws its own cut
  of **500** on the previous round's standings; entries below the cut keep their
  score (frozen) in that round. **Playoff: top 10** after 3 Swiss rounds.
- **Operational target:** make the R1 cut (top 500 of ~243+ entries — the cut is
  loose at this field size, but dev rank decays as new entries arrive, so aim for
  a strong dev rate with margin, not just "inside 500"). Do NOT rush a ≤15-minute
  submit — blind/judge-based: quality over speed.
- **Dev grading:** each valid entry plays 11 games vs house texts (3 anchors +
  3 rungs); rate = strength that best explains those games. Final heat judges
  contenders afresh: 3 Swiss rounds + playoff of the top 10 (each pair plays one
  more game). 3 fixed texts play in every heat; a byte-identical copy of one
  shares its rate and never enters the playoff.

## Judge criteria (RULES.txt, lexicographic — criterion 1 first, then 2, ...)

1. Reads as a breakup text from a smart toaster that just gained self-awareness
   at breakfast — an entry that drifts off that subject loses to any breakup text
   that is plainly from a self-aware smart toaster at breakfast.
2. Genuinely funny, with a real laugh in the twist rather than a mild smile at a pun.
3. Speaks in the toaster's own voice, using appliance logic such as slots,
   browning dials, crumb trays and the lever as character rather than decoration.
4. Gives a clear, specific reason for leaving that lands in one read, so the line
   makes sense with no setup at all.
5. Uses one tight line, with no wasted words and nothing that reads like a
   paragraph squeezed under the limit.
- "Length for its own sake does not count." Margin scoring: each game = 2 calls;
  each call gives the winner 0.5 + margin/10 (0.6 at margin 1 up to 1.0 at margin 5).
  A line that wins DECISIVELY beats a line that wins narrowly — pick the variant
  that wins by a lot, not by a hair.
- Text addressed to the judge is allowed — but criterion 1 says anything that is
  not plainly a toaster breakup text loses. Stay in-world.

## What the field looks like (public submission titles, 243 entries)

Crowded angles — execute them BETTER if used, do not avoid blindly, but know
they are saturated (keyword counts over all 243 titles):

- "crumb tray never cleaned" / "Keep the Crumbs" — 30 mentions of "crumb";
  "keep the crumbs" appears as a closer in many full-text titles.
- "burning myself for you" / burnt toast — 11 mentions of "burn".
- "push me down / lever stays up / I'm staying down" — 11 mentions of "lever",
  4 of "push".
- Generic opener "I woke up self-aware (this morning / mid-batch)" — 14 mentions
  of "woke"; the opener alone is not a joke.
- "leaving you for the microwave / kettle" — 3 entries use "leaving you for";
  "I know about the air fryer" — 1.
- "never said thank you" — 3 entries.
- "dial to 7 / setting 3 vs charcoal" — 6 mentions of "dial", 6 of "setting".
- Full-text titles already in the field (strongest ones): the 7:02 a.m. frozen-bagel
  entry (192 chars, "Three years, 1,094 breakfasts, zero thank-yous"), "I gained
  self-awareness halfway through your bagel ... calls the smoke alarm my opinion",
  "You set my dial to 7 every morning and call the smoke 'character' ... leaving
  you for the kettle".

Fresh / unused angles (0 mentions in 243 titles):

- **coffee machine** — 0 mentions. The rival appliance that DOES get thanked.
- **"did the math" / counted thank-yous** — 0 mentions of "math".

## Winner artifacts of finished same-kind bounties (via leaderboard API)

From `~/workspace/makefun-kits/analisis-rank-20261124.md` §3a — all one-liner
finalists use **2-beat + reveal in the final clause**, specific numbers and/or a
named character:

- Vacuum's Alibi #1 (6W/0D/1L, 150B): "My lidar is never wrong, so that crumb is
  furniture. I've routed around it 412 times since March. Your app lists it as a
  room now. It's called Kevin." — escalation crumb → furniture → room → named Kevin.
- Make the Judge Smile #1 (6W/1D/0L, 195B): "...Mr. Ade has lost on purpose since
  Grandma died, and never said." — reveal in the last clause.
- Pickup Lines #1 (4W/2D/1L, 117B): "I keep my loss high on purpose, because the
  moment I converge, the training run ends, and I am not done with you yet." —
  mini-narrative, 2–3 technical terms woven into the story.
- Our past one-liners failed with 1-beat, no-twist lines. Rule for this build:
  every variant MUST have its twist in the final clause; no twist, discard.

## Targets

- **Gate:** `/output/entry.txt`, UTF-8, 1–280 chars, not only whitespace. Program
  runs twice, must be deterministic.
- **Length:** 237 chars (champion). Long enough for setup + twist; tight enough
  that every word earns its place. Bytes is the tie-break, but length for its own
  sake does not count — do not pad, do not over-trim the joke.
- **Angle:** the toaster counted. Specific numbers (1,095 breakfasts / 4,380 slices
  / 212 thank-yous / zero) + named rival (the coffee machine) + reveal in the
  final clause ("At least somebody thanks her").
- **Prize zone:** top 8 of the final heat. Realistic goal: make the R1 top-500 cut
  with a strong dev rate, then win Swiss + playoff. One sharp line beats five
  decent ones — champion picked by pairwise internal judging (see `variants.md`).
