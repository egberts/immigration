
# Much like sankeyflow Python package and SankeyMATIC,
# we co-opt simplified data entry using the
# source-value-destination trigraph and fan out into
# links and nodes.
#
# Of course, there would be data-checking and node-link checking as well.
import plotly
import pprint


def transpose_trigraph_into_plotly_trace(trigraph: list) -> plotly.graph_objs.Sankey:
    a1 = []
    a2 = []
    a3 = []
    for t1, t2, t3 in trigraph:
        a1.append(t1)
        a2.append(t2)
        a3.append(t3)
    trace = {
        'source': a1,
        'value': a2,
        'target': a3
    }
    return trace


def main():
    trigraph = [
        ('a', 123, 'z'),
        ('b', 234, 'y'),
        ('c', 345, 'x'),
        ('d', 456, 'w'),
        ('e', 567, 'v'),
        ('f', 678, 'u')
    ]
    trace = transpose_trigraph_into_plotly_trace(trigraph)

    pp = pprint.PrettyPrinter(indent=8, compact=True)
    pp.pprint(trace)


if __name__ == "__main__":
    main()
