Unreviewed
==========
* D3sankey - https://blog.ouseful.info/2017/03/17/experimenting-with-sankey-diagrams-in-r-and-python/
* gvisSankey - https://www.r-bloggers.com/2017/11/quick-round-up-visualising-flows-using-network-and-sankey-diagrams-in-python-and-r/
* riverplot (R) - https://www.r-bloggers.com/2017/11/quick-round-up-visualising-flows-using-network-and-sankey-diagrams-in-python-and-r/

PROs:
==========
| package | positive reason |
|---|---|
| plotly.sankey | After 12 nodes, it starts getting wonky (wont fix after 5 years). DOA.
| sankeymatic | Quickest way to create a chart (https://sankeymatic.com/build/)
| sankeymatic | supports Imbalance I/O 
| sankeyflow | Easiest Row data entry (all index are labeled, not an integer)
| sankey (via matplotlib) | beautiful cyclic graph
| HoloViews | Very good hover box
| HoloViews | Very good dynamic labeling of links/nodes

CONs:
==========
| package                     | negative reason |
|-----------------------------|---|
| plotly                      | MUST BE ONLINE with Internet 100%. All their JavaScript packages are pulled from Internet for each HTML access
| sankey (via matplotlib)     | No hover tipbox info
| sankey                      | no Imbalance I/O (must be precise?)
| sankeyflow (via matplotlib) | only acyclic graph (no circular)
| HoloViews                   | only acyclic graph (no circular)
| HoloViews                   | Disjoint X-\>Y-\>V (columnar data entry); difficult to track or insert a single column dataset
| sankeymatic | Only acyclic graph
| chart-studio | requires Authentication API
| sankey (via matplotlib) | only does arrow to arrow (no node boxes)
| sankeyview | 8y inactive repository
| bokeh | No support for sankey type of chart/graph

