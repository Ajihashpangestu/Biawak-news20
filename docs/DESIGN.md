# Design of The World

## The edition as a fixed composition

The master is a 1024 by 1024 SVG embedded
in an HTML document. The viewBox defines
the coordinate system for every editorial
decision on the page. The width supplied
by CSS scales that geometry as a unit on
smaller screens. The HTML body starts at
the origin, so the browser adds no default
margin. Paper fills the full viewBox and
matches the color of the surrounding HTML.
The matching surfaces allow the image
fitter to identify the drawn content
without having to identify the outer
rectangle.

The horizontal working area begins at x 24
and ends at x 1000. This leaves a margin
of 24 units on each side of the drawn
composition. The key rules, dark panels,
map panel and footer share these edges.
This repetition matters in a square image
because the reader sees the full width at
once. Even where the eye moves from left
to right across several items, a common
edge is still available as a reference
when it returns to the next row.

Each band uses its own vertical measure.
The masthead gets space for a display
face. The compact desk furniture gets
small type and close baselines. The
illustrated cards occupy the middle of the
page. The briefs use the same line spacing
for the entire two column block. The map
gives the eye a wider area of low contrast
before the last line. Changing the height
of a band should include reviewing its
neighbors, because the bottom of the frame
is fixed.

## Masthead and edition markers

The left side of the masthead is the first
thing a reader is likely to see in the
thumbnail. Its serif letters carry the
identity across the image with no
associated mark or loaded font. Tight
tracking keeps the display line together.
The small label sits below the display
line in rust, a color also used to mark
distinct kinds of indexing elsewhere on
the page. This associates the label with
the edition structure while preserving the
visual prominence of the title.

Dates use a shared right edge. The
abbreviated day and numeric date take the
larger line. The longer month and year run
beneath them in a smaller display size.
The kicker uses that same right edge at
the bottom of the masthead. Anchoring
these lines with SVG text means a
different platform's fallback face can
change the distance to the left while
preserving the edge that defines the
column.

A double rule defines the boundary between
the edition identity and content. Each
line is a thin filled rectangle. Aligning
rectangles to the whole unit grid keeps
their edges crisp in the browser capture.
There is enough separation between the
rules to keep them visually distinct in
the full size art. At a reduced size they
read together as a slightly stronger
divider.

The italic lede starts immediately below
the rules. It takes two explicit lines,
each with its own SVG text element, so the
browser does not have to infer a line
break. The two baselines leave a small
interval before the subjects strip. The
right side of the lede band holds the
compact date marker. Its position uses the
space beside the sentence and preserves
the full line measure for the news.

## Index and desk furniture

The subjects strip establishes the broad
subject areas in a single reading line.
Its tracking and capitalization relate it
to the labels in the masthead. The region
row immediately below it has a separate
purpose. Each rounded rectangle provides a
place to find a count, while the plain
text at the left explains the total and
editorial scope. The widths of the chips
account for the different lengths of the
names and leave consistent gaps.

The seven region values come from the
assignment. They total 57. The visible
number 57 also matches the sequence of
item identifiers in the edition. Those
identifiers refer to editorial entries,
including multiple dispatches when a
single event supplies several distinct
pieces of information. The chips reproduce
the specified desk counts. The markup does
not derive them from geographic tags on
individual entries.

The figures sit inside a dark green band.
The label identifies the content at the
top of the panel. The other baselines
repeat across eight columns. Each column
starts on a measured 121 unit pitch. A
figure has the largest face in its column,
with its descriptor in uppercase below and
its attribution on the final baseline. The
source color is quieter than the figure
color but still light against the panel.

Readers can distinguish a tally, a
currency and a measurement by reading the
figure together with its descriptor.
Preserving the unit in the large line
helps keep meaning on the first pass. The
Odisha rainfall amount keeps millimeters.
The Japan Tobacco amount is identified as
an expected loss. The stars beside the
cricket figure preserve the scoring
convention for an unbeaten batter. The
number band selects facts already present
in the supplied notes.

The time band has a blue background that
separates it from the figures strip even
at small sizes. A single rule runs almost
the whole panel. Four markers sit on that
rule with consistent spacing, and the time
labels start below the markers on a common
baseline. The geometry represents an
editorial sequence. The intervals between
dots do not encode elapsed hours.

The first marker uses the nominal midpoint
of the provided landfall window. Its
corresponding card carries the actual
range. The next two entries use the
specific local time and offset supplied
for Kyiv and Brussels. IST is five hours
and thirty minutes ahead of UTC. EET adds
two hours, and CET adds one hour. A market
following its own clock enters the rolling
game milestone without a single UTC
conversion. Keep the word rolling beside
the caption when adjusting the copy.

## Story grid

The hero grid has three columns with eight
unit breaks. Each hero is 320 units wide.
Card identity is held in a dark strip
along its top edge. The first thing below
that strip is the illustration, beginning
fourteen units from the top. A pale area
at the bottom holds the title and
description so that labels stay over a
calm surface regardless of the luminance
of the drawing.

The next ten cards use two rows of five.
The declared width and height are 188 and
71. The rows have a narrow break, so the
headings should remain well inside their
own cards. The gap between columns
accommodates a long title at the
prescribed text length. The compact height
requires the artwork to read as a shallow
crop in the assembled page. Essential
subject marks belong near the visible top
of this crop.

The card group carries the story number in
a data attribute. The top strip repeats
the number in visible type along with the
subject or region. That link between
markup and design makes it possible to
locate a story using the verifier and the
image. The explicit ordering of groups
follows the order in which panels are
read, starting with the three leads and
continuing row by row.

Each card closes with a short line of
evidence or context followed by its source
and date. That line has a prescribed
measure inside the card. Space is tight in
a five column grid. Retaining different
scopes between title and description is
useful here. The headline should tell a
reader what changed and the description
should identify the figure, place or
attribution needed to interpret it.

The clay paper tone of the cards is
slightly darker than the page color. Its
job is to keep the body text legible and
provide a continuous rectangular edge. The
left edge of a heading is close to the
edge of the strip card because the
requested title measure occupies almost
the full width. A longer explanation
belongs in the briefs where there is a
wider line and a clearer place for the
full source.

## Illustration layers

Every scene begins with a nested SVG.
Scene paths use a 188 by 57 drawing
coordinate space. Each card translates a
local scene to its grid position. The
reduced coordinate space allows shapes to
be read and edited without doing
arithmetic on whole page positions. The
viewport clips the illustration so that a
long wave or horizon can run through the
edge cleanly.

The first layer pairs a sky or field with
the darker shape of a horizon. The two
shapes can meet at a plain baseline, a
city silhouette, a coast or a bend in the
ground. As a quick check, view this layer
by itself and verify that the subject
still has an open area to occupy. A
complicated horizon can compete with the
subject and make the card look compressed.

The second layer uses a pair of subject
paths. A broad darker stroke is offset
beneath the thin light stroke. The shift
yields a small suggestion of depth and
prevents pale strokes from blending into a
light patch of sky. The same path
instructions register both contours, so
adjustments to a structure should be made
to both instances. Where two strokes form
corners, rounded joins reduce bright
spikes.

The final layer adds a warm accent.
Several accent marks can read as a single
object when they share a location and
purpose. Flags, a ball or a line in the
water provide an immediate identifying
cue. Keeping the accent small leaves room
for the line drawing to carry the story.
Its warm color also ties otherwise
distinct palettes together across the
grid.

The cyclone art uses curved forms and cool
marine colors. The curves indicate a storm
moving over water and towards land. The
separate caption provides the actual
landfall location and window. The bridge
art uses repeated arches and a low city
shape. Those arches refer to the reported
damage without claiming a precise geometry
or location of impact. A pair of warm
strokes draws attention to the sky above
the river.

The diplomacy card makes a sheet of paper
the main shape. The parallel lines are
marks of writing within the illustration.
They are paths rather than literal text.
The diagram emphasizes the reported
content of the declaration and avoids
suggesting that the edition covers the
previous day's summit. The caption
identifies the two topics omitted from the
document.

The market line and the chip are
recognizable shapes even when their labels
are small. The government building and its
flag establish the summit scene. A ship
silhouette suggests energy shipping and
the passage through Hormuz. The cricket
card combines wickets, bat and ball. The
game card uses the shape of a controller.
The diplomacy and court themed cards use
architectural and document imagery where a
small portrait would fail to identify the
people involved.

The images communicate through
association. The news descriptions
establish the edition's factual claims. A
path that shows a building, court scale or
military tent should stay general unless
the source notes establish something
visually specific. This keeps the scene
useful when the subject of the story is a
document, judgment or deployment update.

## Type and reading distances

The edition has two font stacks. Georgia,
Times New Roman and the generic serif are
available to the display lines, titles and
lede. Helvetica, Arial and the generic
sans serif serve the index, caption and
description lines. Leaving fallback
selection to the browser removes
dependencies and allows the file to open
from disk. Measurements therefore depend
on the combination of SVG attributes and
the actual fonts available on the capture
machine.

The largest lettering anchors the page. In
a full image, the 19 unit card titles
provide a consistent next rung beneath the
date. Minor subtitles, source lines and
brief rows have progressively smaller
sizes. The paper tone and dark ink help
the body text remain distinct when the
reader zooms. At a display width of 300
pixels, a 9.5 unit line is roughly 2.8 CSS
pixels high before any effects from crop
normalization. The thumbnail can convey
hierarchy, while reading every brief
requires a larger view.

The title and brief line measures are
controlled with textLength. The rendering
engine distributes the correction over the
string using spacing and glyph scaling.
This constrains the horizontal extent even
when a font fallback changes the default
advance. Large corrections can narrow the
letters or open short words. Proofreading
the final strings should include checking
that a long phrase can be shortened
without deleting the qualifier that makes
it accurate.

The background and text colors also
communicate rank. Dark ink is used for the
longer reading surfaces. Cream type marks
information shown on dark bands. Muted
pale green picks out the bracketed source
in the figures row. Rust marks edition
labels, map pins and dispatch numbers. The
same rust across the page gives those
small elements a consistent role.

## Editing and attribution

The supplied notes are the source packet
for this edition. The date at the top and
the date attached to a citation serve
different purposes. The large date
identifies the edition as a whole. The
smaller date indicates the reported day
for the statement beside it. When a story
concerns a preexisting condition, detail
such as an October total or a five year
theft remains tied to the report date.

The three leading panels address immediate
public risk, damage in a capital and
international diplomacy. The lede makes
room for the talks in Brussels and for the
opening trading session, giving the reader
a transition from the first stories into
the remaining grid. The ten short cards
extend the subject range into trade,
energy, sport, culture, climate diplomacy
and the courts.

The position of a card can work alongside
several dispatches. The storm card
identifies landfall. The associated lines
can then give the completion time, wind
speed, rainfall, evacuation and shelters.
The Ukraine card identifies the bridge
damage as central to the attack. Separate
lines record what was launched, what was
intercepted, which bridges were hit, the
casualty tally and the second wave.

Numbers with similar appearances require
additional care. A launch total uses a
different verb from an interception total.
The closing price has a different meaning
from the offer price and from the opening
valuation. Retaining those labels prevents
three separate values in the market story
from being read as interchangeable. A wind
range and a peak gust should likewise
retain their distinct units and
descriptions.

A compact source string is kept near the
assertion it supports. Where space is most
limited, the abbreviation WW stands for
World Watch and CSM stands for CS Monitor.
AA refers to Anadolu Agency. Full
spellings appear in other passages where
there is room. The combined source text on
the hero cards reflects the packet's
bundles of attribution.

The date check records the exclusions the
desk supplied. Follow up reporting on a
subsequent day has its own place in the
issue, so a response to a ruling or the
first day on sale can appear while the
earlier underlying event stays in the
cutoff line. This distinction also
controls choice of tense. Scheduled
remarks are described as due, possible
agreements as possible and a court remand
as a further procedural step.

## Dispatches and location guide

The brief section establishes its reading
order with numbers. The reader scans from
14 through 35 on the left and resumes at
36 on the right. The central vertical rule
separates the two text fields. Both
columns use a pitch of eleven units. Each
number has an advance of its own before
the prose begins. This permits right and
left columns to use the same text measure
despite their different positions.

Every story sentence and its source appear
in the same SVG text element. The reader
can follow a line through to the closing
parenthesis without deciding which
attribution applies. This also gives the
checker a single string to inspect for
each dated dispatch. The compact leading
uses every available row, so a second line
of copy in a dispatch would require moving
or rethinking the contents below it.

The map positions six labels on a stylized
world outline. A thin grid and pale water
separate the continents without turning
the guide into a second headline. Spots
identify places used by the edition. The
city names are individually anchored to
avoid collisions. A label at the end
anchor can extend away from a cluster
while another moves to the right. Local
drawing coordinates make it easier to
adjust a city name without moving the map
group.

The visual map is a locator. Its shapes
are generalized and do not show borders.
Accurate editorial detail remains in the
adjacent stories, which name places and
explain their relationship to the action.
This lets the map connect the reader to
the page without implying precision for
the boundaries, travel distances or
relative importance of mapped locations.

The bottom rule closes the content block.
Beneath it the cutoff line combines the
excluded items and the clock convention.
It uses the same working edges as the
bands above. The page contains a little
more paper below the baseline so that
descenders in the line remain fully inside
the square.

## Capture and delivery

The capture script changes to the
directory containing the page and invokes
the fitter. The fitter constructs a local
file URI from an absolute path. That
allows Chromium to handle spaces and other
characters correctly. A viewport taller
than the source SVG leaves enough space to
include its full height even if the
browser uses a different platform font.

The screenshot is opened as RGB so the
threshold calculation treats all three
channels uniformly. The reference frame
uses the exact paper color. A pixel counts
towards the content bounds when any
channel differs by more than eight.
Antialiased extremities that only barely
differ from paper are intentionally
absorbed into the small margin added
around the measured box.

Margins are clamped to the screenshot
edges. The file is then resized to 1024 by
1024 with a Lanczos filter. This step
normalizes the output from the measured
rectangle and can slightly change its
aspect ratio when the detected art is
taller than it is wide. The fitter reports
both bounding boxes, which gives a
reviewer enough information to reason
about the difference between source
position and final position.

The PNG written by the fitter is the one
consumed by the TypeScript entry point.
The delivery script opens it relative to
its own module location. Output paths use
the make.fun environment setting where
available and otherwise use the default
grader directory. The delivered bytes are
the original PNG bytes. Hashing those
bytes in each script gives a direct way to
compare the rendered and copied artifacts.

## Structural proof

The checker uses the Python HTML parser to
collect attributes from the source page.
It records the numbered groups and the
figures independently. The expected
sequence guards against omissions,
duplicate numbers and incidental
reordering. The source suffix rule for
briefs checks all forty four dispatches,
so a missing date is detected even when
the total count still passes.

A declared width check is different from a
browser proof. It can flag a requested
text measure that extends past the global
edge. Real glyph bounds also depend on
font metrics, local transforms and the
presence of a text anchor. A visual check
in Chromium is appropriate after changing
a long headline or moving labels next to
each other. Compare both the large capture
and a small preview to check relative
weight and line clarity.

There is no remote input during the
render. The paths and the published copy
are in the sole HTML source. The project
badges live in the repository
documentation and are separate from that
HTML. Running the checker before capture
gives a quick way to find a missing tag or
source before starting a browser. Running
the fitter and the delivery script
produces two hashes that can be compared
without relying on browser state.
