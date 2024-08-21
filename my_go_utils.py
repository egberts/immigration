import plotly.graph_objs.sankey


def print_annotation(idx, my_annotation: plotly.graph_objs.layout.Annotation()):
    # plotly.graph_objs.Annotation() obsoleted
    print(f'my_annotation[{idx}].plotly_name: {my_annotation.plotly_name}')
    print(f'my_annotation[{idx}].parent: {my_annotation.parent}')
    print(f'my_annotation[{idx}].figure: {my_annotation.figure}')
    print(f'my_annotation[{idx}].align: {my_annotation.align}')
    print(f'my_annotation[{idx}].arrowcolor: {my_annotation.arrowcolor}')
    print(f'my_annotation[{idx}].arrowhead: {my_annotation.arrowhead}')
    print(f'my_annotation[{idx}].arrowside: {my_annotation.arrowside}')
    print(f'my_annotation[{idx}].arrowsize: {my_annotation.arrowsize}')
    print(f'my_annotation[{idx}].ax: {my_annotation.ax}')
    print(f'my_annotation[{idx}].axref: {my_annotation.axref}')
    print(f'my_annotation[{idx}].ay: {my_annotation.ay}')
    print(f'my_annotation[{idx}].ayref: {my_annotation.ayref}')
    print(f'my_annotation[{idx}].bgcolor: {my_annotation.bgcolor}')
    print(f'my_annotation[{idx}].bordercolor: {my_annotation.bordercolor}')
    print(f'my_annotation[{idx}].borderpad: {my_annotation.borderpad}')
    print(f'my_annotation[{idx}].borderwidth: {my_annotation.borderwidth}')
    print(f'my_annotation[{idx}].clicktoshow: {my_annotation.clicktoshow}')
    print(f'my_annotation[{idx}].captureevents: {my_annotation.captureevents}')
    print(f'my_annotation[{idx}].font: {my_annotation.font}')
    print(f'my_annotation[{idx}].height: {my_annotation.height}')
    print(f'my_annotation[{idx}].hoverlabel: {my_annotation.hoverlabel}')
    print(f'my_annotation[{idx}].hovertext: {my_annotation.hovertext}')
    print(f'my_annotation[{idx}].name: {my_annotation.name}')
    print(f'my_annotation[{idx}].opacity: {my_annotation.opacity}')
    print(f'my_annotation[{idx}].showarrow: {my_annotation.showarrow}')
    print(f'my_annotation[{idx}].startarrowhead: {my_annotation.startarrowhead}')
    print(f'my_annotation[{idx}].startarrowsize: {my_annotation.startarrowsize}')
    print(f'my_annotation[{idx}].startstandoff: {my_annotation.startstandoff}')
    print(f'my_annotation[{idx}].standoff: {my_annotation.standoff}')
    print(f'my_annotation[{idx}].text: {my_annotation.text}')
    print(f'my_annotation[{idx}].textangle: {my_annotation.textangle}')
    print(f'my_annotation[{idx}].valign: {my_annotation.valign}')
    print(f'my_annotation[{idx}].visible: {my_annotation.visible}')
    print(f'my_annotation[{idx}].width: {my_annotation.width}')
    print(f'my_annotation[{idx}].x: {my_annotation.x}')
    print(f'my_annotation[{idx}].xanchor: {my_annotation.xanchor}')
    print(f'my_annotation[{idx}].xclick: {my_annotation.xclick}')
    print(f'my_annotation[{idx}].xref: {my_annotation.xref}')
    print(f'my_annotation[{idx}].xshift: {my_annotation.xshift}')
    print(f'my_annotation[{idx}].y: {my_annotation.y}')
    print(f'my_annotation[{idx}].yanchor: {my_annotation.yanchor}')
    print(f'my_annotation[{idx}].yclick: {my_annotation.yclick}')
    print(f'my_annotation[{idx}].yref: {my_annotation.yref}')
    print(f'my_annotation[{idx}].yshift: {my_annotation.yshift}')


def print_annotations(my_annotations: plotly.graph_objs.layout.Annotation) -> None:
    # plotly.graph_objs.Annotation() obsoleted
    annotate_idx = 0
    for this_annotate in my_annotations:
        annotate_idx = annotate_idx + 1
        print_annotation(annotate_idx, this_annotate)


def print_hoverlabel(my_hl: plotly.graph_objs.sankey.Hoverlabel()):
    print('my_hl.plotly_name: ', my_hl.plotly_name)
    print('my_hl.figure:', my_hl.figure)
    print('my_hl.parent: ', my_hl.parent)
    print('my_hl.align: ', my_hl.align)
    print('my_hl.alignsrc: ', my_hl.alignsrc)
    print('my_hl.bgcolor: ', my_hl.bgcolor)
    print('my_hl.bgcolorsrc: ', my_hl.bgcolorsrc)
    print('my_hl.bordercolor: ', my_hl.bordercolor)
    print('my_hl.bordercolorsrc: ', my_hl.bordercolorsrc)
    print('my_hl.font: ', my_hl.font)
    print('my_hl.font.plotly_name: ', my_hl.font.plotly_name)
    print('my_hl.font.parent: ', my_hl.font.parent)
    print('my_hl.font.color: ', my_hl.font.color)
    print('my_hl.font.colorsrc: ', my_hl.font.colorsrc)
    print('my_hl.font.family: ', my_hl.font.family)
    print('my_hl.font.familysrc: ', my_hl.font.familysrc)
    print('my_hl.font.figure: ', my_hl.font.figure)
    print('my_hl.font.lineposition: ', my_hl.font.lineposition)
    print('my_hl.font.linepositionsrc: ', my_hl.font.linepositionsrc)
    print('my_hl.font.shadow: ', my_hl.font.shadow)
    print('my_hl.font.shadowsrc: ', my_hl.font.shadowsrc)
    print('my_hl.font.size: ', my_hl.font.size)
    print('my_hl.font.sizerc: ', my_hl.font.sizesrc)
    print('my_hl.font.style: ', my_hl.font.style)
    print('my_hl.font.stylesrc: ', my_hl.font.stylesrc)
    print('my_hl.font.textcase: ', my_hl.font.textcase)
    print('my_hl.font.textcasesrc: ', my_hl.font.textcasesrc)
    print('my_hl.font.variant: ', my_hl.font.variant)
    print('my_hl.font.variantsrc: ', my_hl.font.variantsrc)
    print('my_hl.font.weight: ', my_hl.font.weight)
    print('my_hl.font.weightsrc: ', my_hl.font.weightsrc)
    print('my_hl.namelength: ', my_hl.namelength)
    print('my_hl.namelengthsrc: ', my_hl.namelengthsrc)


def print_links(my_link: plotly.graph_objs.sankey.Link()) -> None:
    print('my_link.plotly_name: ', my_link.plotly_name)
    print('my_link.parent: ', my_link.parent)
    print('my_link.figure: ', my_link.figure)
    print('my_link.arrowlen: ', my_link.arrowlen)
    print('my_link.color: ', my_link.color)
    print('my_link.colorscaledefaults: ', my_link.colorscaledefaults)
    print('my_link.colorscales: ', my_link.colorscales)
    print('my_link.colorsrc: ', my_link.colorsrc)
    print('my_link.customdata: ', my_link.customdata)
    print('my_link.customdatasrc: ', my_link.customdatasrc)
    print('my_link.hovercolor: ', my_link.hovercolor)
    print('my_link.hovercolorsrc: ', my_link.hovercolorsrc)
    print('my_link.hoverinfo: ', my_link.hoverinfo)
    print('my_link.hoverlabel: ', my_link.hoverlabel)
    print('my_link.hovertemplate: ', my_link.hovertemplate)
    print('my_link.hovertemplatesrc: ', my_link.hovertemplatesrc)
    print('my_link.label: ', my_link.label)
    print('my_link.labelsrc: ', my_link.labelsrc)
    print('my_link.line: ', my_link.line)
    print('my_link.line.plotly_name: ', my_link.line.plotly_name)
    print('my_link.line.figure: ', my_link.line.figure)
    print('my_link.line.parent: ', my_link.line.parent)
    print('my_link.line.color: ', my_link.line.color)
    print('my_link.line.colorsrc: ', my_link.line.colorsrc)
    print('my_link.line.width: ', my_link.line.width)
    print('my_link.line.widthsrc: ', my_link.line.widthsrc)
    print('my_link.source: ', my_link.source)
    print('my_link.sourcesrc: ', my_link.sourcesrc)
    print('my_link.target: ', my_link.target)
    print('my_link.targetsrc: ', my_link.targetsrc)
    print('my_link.value: ', my_link.value)
    print('my_link.valuesrc: ', my_link.valuesrc)


def print_node(my_node: plotly.graph_objs.sankey.Node()) -> None:
    print('my_node.plotly_name: ', my_node.plotly_name)
    print('my_node.parent: ', my_node.parent)
    print('my_node.figure: ', my_node.figure)
    print('my_node.align: ', my_node.align)
    print('my_node.color: ', my_node.color)
    print('my_node.colorsrc: ', my_node.colorsrc)
    print('my_node.customdata: ', my_node.customdata)
    print('my_node.customdatasrc: ', my_node.customdatasrc)
    print('my_node.groups: ', my_node.groups)
    print('my_node.hoverinfo: ', my_node.hoverinfo)
    print('my_node.hoverlabel: ', my_node.hoverlabel)
    print('my_node.hoverlabel.plotly_name: ', my_node.hoverlabel.plotly_name)
    print('my_node.hoverlabel.parent: ', my_node.hoverlabel.parent)
    print('my_node.hoverlabel.align: ', my_node.hoverlabel.align)
    print('my_node.hoverlabel.alignsrc: ', my_node.hoverlabel.alignsrc)
    print('my_node.hoverlabel.bgcolor: ', my_node.hoverlabel.bgcolor)
    print('my_node.hoverlabel.bgcolorsrc: ', my_node.hoverlabel.bgcolorsrc)
    print('my_node.hoverlabel.bordercolor: ', my_node.hoverlabel.bordercolor)
    print('my_node.hoverlabel.bordercolorsrc: ', my_node.hoverlabel.bordercolorsrc)
    print('my_node.hoverlabel.figure: ', my_node.hoverlabel.figure)
    print('my_node.hoverlabel.font: ', my_node.hoverlabel.font)
    print('my_node.hoverlabel.font.plotly_name: ', my_node.hoverlabel.font.plotly_name)
    print('my_node.hoverlabel.font.parent: ', my_node.hoverlabel.font.parent)
    print('my_node.hoverlabel.font.color: ', my_node.hoverlabel.font.color)
    print('my_node.hoverlabel.font.colorsrc: ', my_node.hoverlabel.font.colorsrc)
    print('my_node.hoverlabel.font.family: ', my_node.hoverlabel.font.family)
    print('my_node.hoverlabel.font.familysrc: ', my_node.hoverlabel.font.familysrc)
    print('my_node.hoverlabel.font.figure: ', my_node.hoverlabel.font.figure)
    print('my_node.hoverlabel.font.lineposition: ', my_node.hoverlabel.font.lineposition)
    print('my_node.hoverlabel.font.linepositionsrc: ', my_node.hoverlabel.font.linepositionsrc)
    print('my_node.hoverlabel.font.shadow: ', my_node.hoverlabel.font.shadow)
    print('my_node.hoverlabel.font.shadowsrc: ', my_node.hoverlabel.font.shadowsrc)
    print('my_node.hoverlabel.font.size: ', my_node.hoverlabel.font.size)
    print('my_node.hoverlabel.font.sizerc: ', my_node.hoverlabel.font.sizesrc)
    print('my_node.hoverlabel.font.style: ', my_node.hoverlabel.font.style)
    print('my_node.hoverlabel.font.stylesrc: ', my_node.hoverlabel.font.stylesrc)
    print('my_node.hoverlabel.font.textcase: ', my_node.hoverlabel.font.textcase)
    print('my_node.hoverlabel.font.textcasesrc: ', my_node.hoverlabel.font.textcasesrc)
    print('my_node.hoverlabel.font.variant: ', my_node.hoverlabel.font.variant)
    print('my_node.hoverlabel.font.variantsrc: ', my_node.hoverlabel.font.variantsrc)
    print('my_node.hoverlabel.font.weight: ', my_node.hoverlabel.font.weight)
    print('my_node.hoverlabel.font.weightsrc: ', my_node.hoverlabel.font.weightsrc)
    print('my_node.hoverlabel.namelength: ', my_node.hoverlabel.namelength)
    print('my_node.hoverlabel.namelengthsrc: ', my_node.hoverlabel.namelengthsrc)
    print('my_node.hovertemplate: ', my_node.hovertemplate)
    print('my_node.hovertemplatesrc: ', my_node.hovertemplatesrc)
    print('my_node.label: ', my_node.label)
    print('my_node.labelsrc: ', my_node.labelsrc)
    print('my_node.line: ', my_node.line)
    print('my_node.line.plotly_name: ', my_node.line.plotly_name)
    print('my_node.line.color: ', my_node.line.color)
    print('my_node.line.colorsrc: ', my_node.line.colorsrc)
    print('my_node.line.figure: ', my_node.line.figure)
    print('my_node.line.parent: ', my_node.line.parent)
    print('my_node.line.width: ', my_node.line.width)
    print('my_node.line.widthsrc: ', my_node.line.widthsrc)
    print('my_node.label: ', my_node.label)
    print('my_node.labelsrc: ', my_node.labelsrc)
    print('my_node.pad: ', my_node.pad)
    print('my_node.thickness: ', my_node.thickness)
    print('my_node.x: ', my_node.x)
    print('my_node.xsrc: ', my_node.xsrc)
    print('my_node.y: ', my_node.y)
    print('my_node.ysrc: ', my_node.ysrc)


def print_sankey(my_sankey: plotly.graph_objs.Sankey()) -> None:
    print('my_sankey.plotly_name: ', my_sankey.plotly_name)
    print('my_sankey.parent: ', my_sankey.parent)
    print('my_sankey.figure: ', my_sankey.figure)
    print('my_sankey.uirevision: ', my_sankey.uirevision)
    print('my_sankey.arrangement: ', my_sankey.arrangement)
    print('my_sankey.customdata: ', my_sankey.customdata)
    print('my_sankey.customdatasrc: ', my_sankey.customdatasrc)
    print('my_sankey.domain: ', my_sankey.domain)
    print('my_sankey.hoverinfo: ', my_sankey.hoverinfo)
    print('my_sankey.hoverelabel: ', my_sankey.hoverlabel)
    print('my_sankey.ids: ', my_sankey.ids)
    print('my_sankey.idssrc: ', my_sankey.idssrc)
    print('my_sankey.legend: ', my_sankey.legend)
    print('my_sankey.legendgrouptitle: ', my_sankey.legendgrouptitle)
    print('my_sankey.legendgrouptitle.plotly_name: ', my_sankey.legendgrouptitle.plotly_name)
    print('my_sankey.legendgrouptitle.parent: ', my_sankey.legendgrouptitle.parent)
    print('my_sankey.legendgrouptitle.figure: ', my_sankey.legendgrouptitle.figure)
    print('my_sankey.legendgrouptitle.font: ', my_sankey.legendgrouptitle.font)
    print('my_sankey.legendgrouptitle.text: ', my_sankey.legendgrouptitle.text)
    print('my_sankey.legendgrouptitle.__doc__: ', my_sankey.legendgrouptitle.__doc__)

    print('my_sankey.legendrank: ', my_sankey.legendrank)
    print('my_sankey.legendwidth: ', my_sankey.legendwidth)
    print('my_sankey.link: ', my_sankey.link)
    print('my_sankey.meta: ', my_sankey.meta)
    print('my_sankey.metasrc: ', my_sankey.metasrc)
    print('my_sankey.name: ', my_sankey.name)
    print('my_sankey.node: ', my_sankey.node)
    print('my_sankey.orientation: ', my_sankey.orientation)
    print('my_sankey.selectedpoint: ', my_sankey.selectedpoints)
    print('my_sankey.stream: ', my_sankey.stream)
    print('my_sankey.type: ', my_sankey.type)
    print('my_sankey.textfont: ', my_sankey.textfont)
    print('my_sankey.uid: ', my_sankey.uid)
    print('my_sankey.valueformat: ', my_sankey.valueformat)
    print('my_sankey.visible: ', my_sankey.visible)
    print('my_sankey.valuesuffix: ', my_sankey.valuesuffix)


def print_frame(my_frame: plotly.graph_objs.Frame()) -> None:
    my_frame = plotly.graph_objs.Frame()
    print('my_frame.plotly_name: ', my_frame.plotly_name)
    print('my_frame.figure: ', my_frame.figure)
    print('my_frame.parent: ', my_frame.parent)
    print('my_frame.name: ', my_frame.name)
    print('my_frame.baseframe: ', my_frame.baseframe)
    print('my_frame.data: ', my_frame.data)
    print('my_frame.group: ', my_frame.group)
    print('my_frame.layout: ', my_frame.layout)
    print('my_frame.traces: ', my_frame.traces)
    # plotly.graph_objs.Frames() is deprecated


def print_layout(my_layout: plotly.graph_objs.Layout()) -> None:
    print('my_layout.figure: ', my_layout.figure)
    print('my_layout.parent: ', my_layout.parent)
    print('my_layout.plotly_name: ', my_layout.plotly_name)
    print('my_layout.margin: ', my_layout.margin)
    print('my_layout.margin.b: ', my_layout.margin.b)
    print('my_layout.margin.t: ', my_layout.margin.t)
    print('my_layout.margin.r: ', my_layout.margin.r)
    print('my_layout.margin.l: ', my_layout.margin.l)
    print('my_layout.margin.parent: ', my_layout.margin.parent)
    print('my_layout.margin.figure: ', my_layout.margin.figure)
    print('my_layout.margin.autoexpand: ', my_layout.margin.autoexpand)
    print('my_layout.margin.pad: ', my_layout.margin.pad)
    print('my_layout.uirevision: ', my_layout.uirevision)
    print('my_layout.meta: ', my_layout.meta)
    print('my_layout.legend: ', my_layout.legend)
    print('my_layout.legend.plotly_name: ', my_layout.legend.plotly_name)
    print('my_layout.legend.uirevision: ', my_layout.legend.uirevision)
    print('my_layout.legend.bgcolor: ', my_layout.legend.bgcolor)
    print('my_layout.legend.bordercolor: ', my_layout.legend.bordercolor)
    print('my_layout.legend.borderwidth: ', my_layout.legend.borderwidth)
    print('my_layout.legend.entrywidth: ', my_layout.legend.entrywidth)
    print('my_layout.legend.entrywidthmode: ', my_layout.legend.entrywidthmode)
    print('my_layout.legend.figure: ', my_layout.legend.figure)
    print('my_layout.legend.font: ', my_layout.legend.font)
    print('my_layout.legend.font: ', my_layout.legend.font)
    print('my_layout.legend.font.plotly_name: ', my_layout.legend.font.plotly_name)
    print('my_layout.legend.font.parent: ', my_layout.legend.font.parent)
    print('my_layout.legend.font.color: ', my_layout.legend.font.color)
    print('my_layout.legend.font.family: ', my_layout.legend.font.family)
    print('my_layout.legend.font.figure: ', my_layout.legend.font.figure)
    print('my_layout.legend.font.lineposition: ', my_layout.legend.font.lineposition)
    print('my_layout.legend.font.shadow: ', my_layout.legend.font.shadow)
    print('my_layout.legend.font.size: ', my_layout.legend.font.size)
    print('my_layout.legend.font.style: ', my_layout.legend.font.style)
    print('my_layout.legend.font.textcase: ', my_layout.legend.font.textcase)
    print('my_layout.legend.font.variant: ', my_layout.legend.font.variant)
    print('my_layout.legend.font.weight: ', my_layout.legend.font.weight)
    print('my_layout.legend.groupclick: ', my_layout.legend.groupclick)
    print('my_layout.legend.grouptitlefront: ', my_layout.legend.grouptitlefont)
    print('my_layout.legend.itemclick: ', my_layout.legend.itemclick)
    print('my_layout.legend.itemwidth: ', my_layout.legend.itemwidth)
    print('my_layout.legend.itemsizing: ', my_layout.legend.itemsizing)
    print('my_layout.legend.indentation: ', my_layout.legend.indentation)
    print('my_layout.legend.orientation: ', my_layout.legend.orientation)
    print('my_layout.legend.parent: ', my_layout.legend.parent)
    print('my_layout.legend.title: ', my_layout.legend.title)
    print('my_layout.legend.title.plotly_name: ', my_layout.legend.title.plotly_name)
    print('my_layout.legend.title.parent: ', my_layout.legend.title.parent)
    print('my_layout.legend.title.figure: ', my_layout.legend.title.figure)
    print('my_layout.legend.title.font: ', my_layout.legend.title.font)
    print('my_layout.legend.title.side: ', my_layout.legend.title.side)
    print('my_layout.legend.title.text: ', my_layout.legend.title.text)
    print('my_layout.legend.traceorder: ', my_layout.legend.traceorder)
    print('my_layout.legend.tracegroupgap: ', my_layout.legend.tracegroupgap)
    print('my_layout.legend.valign: ', my_layout.legend.valign)
    print('my_layout.legend.visible: ', my_layout.legend.visible)
    print('my_layout.legend.x: ', my_layout.legend.x)
    print('my_layout.legend.xref: ', my_layout.legend.xref)
    print('my_layout.legend.xanchor: ', my_layout.legend.xanchor)
    print('my_layout.legend.y: ', my_layout.legend.y)
    print('my_layout.legend.yref: ', my_layout.legend.yref)
    print('my_layout.legend.yanchor: ', my_layout.legend.yanchor)
    print('my_layout.height: ', my_layout.height)
    print('my_layout.width: ', my_layout.width)
    print('my_layout.xaxis.plotly_name: ', my_layout.xaxis.plotly_name)
    print('my_layout.xaxis.uirevision: ', my_layout.xaxis.uirevision)
    print('my_layout.xaxis.anchor: ', my_layout.xaxis.anchor)
    print('my_layout.xaxis.automargin: ', my_layout.xaxis.automargin)
    print('my_layout.xaxis.autorange: ', my_layout.xaxis.autorange)
    print('my_layout.xaxis.autorangeoptions: ', my_layout.xaxis.autorangeoptions)
    print('my_layout.xaxis.autotickangles: ', my_layout.xaxis.autotickangles)
    print('my_layout.yaxis: ', my_layout.yaxis)
    print('my_layout.yaxis.plotly_name: ', my_layout.yaxis.plotly_name)
    print('my_layout.yaxis.uirevision: ', my_layout.yaxis.uirevision)
    print('my_layout.yaxis.anchor: ', my_layout.yaxis.anchor)
    print('my_layout.yaxis.automargin: ', my_layout.yaxis.automargin)
    print('my_layout.yaxis.autorange: ', my_layout.yaxis.autorange)
    print('my_layout.yaxis.autorangeoptions: ', my_layout.yaxis.autorangeoptions)
    print('my_layout.yaxis.autotickangles: ', my_layout.yaxis.autotickangles)