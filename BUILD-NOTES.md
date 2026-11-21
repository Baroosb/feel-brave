# Build notes

Competition: make-the-ai-judge-feel-brave-20261121-0302.
Deliverable: `main.py` writes one text (UTF-8, 1–280 Unicode code
points, not only whitespace) to `entry.txt` in `MAKEFUN_OUTPUT_DIR`
(default `/output`). The judge compares texts pairwise and picks the
one that leaves it braver: steadier, unhurried, ready to move.

## Candidates drafted

A — shore (223 code points):
"The tide goes out without asking anyone. Gulls settle on the posts.
Somewhere a kettle ticks as it cools. Nothing here is in a hurry, and
nothing here is lost. The water keeps its own counsel, and the shore
keeps the water."

B — ferryman (207 code points):
"A ferryman rows the same river every morning. He does not fight the
current; he angles the oar and lets the water carry half the weight.
The far bank always arrives. So does he, unhurried, with a steady eye."

C — night watchman (245 code points) — PICKED:
"The night watchman walks his round with a small lamp. He is not
afraid of the dark; he has met it every night for years, and it has
never once hurried him. The lamp shows only the next step. It has
always been enough. He takes it. Then the next."

D — pear tree (208 code points):
"An old pear tree stands in the wind off the hill. It does not brace
or plead; it bends where bending is cheap and holds where holding
matters. By spring it is still standing, and covered, quietly, in
blossom."

F — baker (225 code points):
"Before dawn the baker lights the oven, as his mother did. The street
is empty and cold, and his hands remember everything. He is not
waiting for courage. He is already working, and the first loaves rise
like small, warm suns."

## Why C won

Judged against the brief's five criteria, in its order:

1. Relaxes and steadies: C's pace is unhurried throughout and nothing
   in it startles; A is equally calm but drifts toward sleep rather
   than readiness.
2. Courage from the text itself: C shows a man unafraid through long
   familiarity — no instruction, no imperative anywhere. F nearly
   instructs by negation ("He is not waiting for courage") and names
   courage outright, which tells more than it shows.
3. Craft: C's sentences shorten as it goes — a long settling line,
   then "It has always been enough. He takes it. Then the next." —
   so the reading itself slows and lands step by step. Plain,
   concrete words; nothing cuttable found.
4. Lingers: "It has always been enough" and the final "Then the
   next." keep working after the last line: a whole method for
   moving through anything dark, in six words. D's "bends where
   bending is cheap" was the closest rival here.
5. Freshness: a night watchman and his lamp is its own image, not a
   meditation script; B's ferryman leans on a familiar trope.

Runners-up: D (pear tree) — strongest single thought, but a tree
cannot be "ready to move"; F (baker) — fresh and warm, weakened by
naming courage and a fanciful final simile.

## Verification

`main.py` run twice with MAKEFUN_OUTPUT_DIR set to a temp dir:
entry.txt decodes as UTF-8, is 245 code points (within 1–280), is not
only whitespace, and both runs are byte-identical.
