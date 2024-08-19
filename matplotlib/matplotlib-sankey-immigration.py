import matplotlib.pyplot as plt

from matplotlib.sankey import Sankey

# PROs: matplotlib.sankey has sankey.add() over plotly.graph_object.sankey();
#       greatly ease in row-based data entry.

plt.rc('font', size=15)
plt.rc('font', serif='Arial')
plt.axis('off')

fig = plt.figure(figsize=(9, 10))
fig.set_facecolor('white')

ax = fig.add_subplot(1, 1, 1,
                     xticks=[], yticks=[],
                     title="Some title\nwith next line")
Hdot = [260.431, 35.078, 180.794, 221.115, 22.700,
        142.361, 10.193, 10.210, 43.670, 44.312,
        68.631, 10.758, 10.758, 0.017, 0.642,
        232.121, 44.559, 100.613, 132.168]  # MW
sankey = Sankey(
    ax=ax,
    format='%.3G',
    unit=' aliens',
    gap=0.5,
    scale=0.1,
    tolerance=600,
    offset=0.6,
    head_angle=135,
    shoulder=0,
    radius=0.1
)
sankey.add(patchlabel='\n\nPump 1', rotation=0, facecolor='#37c959',
           flows=[6, 5, 4],
           labels=['Shaft power', 'middlename', 'lowerware'],
           orientations=[0, 0, 0])

# Turn off inside information if flow path gets too small
sankey.format = ''
sankey.unit = ''

sankey.add(patchlabel='NODE2', rotation=0,
           flows=[1],
           labels=['bar'],
           orientations=[6],
           prior=0,
           connect=(1, 0))
#sankey.add(patchlabel='\n\nOpen\nheater', facecolor='#37c959',
#           flows=[Hdot[11], Hdot[7], Hdot[4], -Hdot[8]],
#           labels=[None, '', None, None],
#           orientations=[1, 0, -1, 0], prior=0, connect=(2, 1))
#sankey.add(patchlabel='\n\nPump 2', facecolor='#37c959',
#           flows=[Hdot[14], Hdot[8], -Hdot[9]],
#           labels=['Shaft power', '', None],
#           orientations=[1, 0, 0], prior=1, connect=(3, 1))
#sankey.add(patchlabel='Closed\nheater', trunklength=2.914, fc='#37c959',
#           flows=[Hdot[9], Hdot[1], -Hdot[11], -Hdot[10]],
#           labels=['', '', None, None],
#           orientations=[0, -1, 1, -1], prior=2, connect=(2, 0))
# Notice that the explicit connections are handled automatically, but the
# implicit ones currently are not.  The lengths of the paths and the trunks
# must be adjusted manually, and that is a bit tricky.

diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')

for d in diagrams:
    for t in d.texts:
        text = t.get_text()
        if text[-1] == '\n':  # remove empty line at the end, needed for centering
            t.set_text(text[:-1])
        t.set_fontsize(10)
        t.set_verticalalignment('center')
        if text[:4] == 'Loss' and text[:6] != 'Loss 0':  # align all loss labels except loss 0
            t.set_horizontalalignment('left')
            xy = t.get_position()
            t.set_position(xy=(0.18, xy[1]))
        else:
            t.set_horizontalalignment('center')
        #t.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='blue'))
# Notice that the explicit connections are handled automatically, but the
# implicit ones currently are not.  The lengths of the paths and the trunks
# must be adjusted manually, and that is a bit tricky.

# Final adjustment of diagram
# diagrams[0].texts[0].set_position(xy=(0, 0.42)) # adjust position of input 1
# diagrams[0].texts[1].set_position(xy=(1.75, diagrams[0].texts[1].get_position()[1])) # adjust pos. of loss 0
# diagrams[0].texts[2].set_text('')  # remove output 1 as it coincides with input 2
# diagrams[1].texts[-1].set_position(xy=(diagrams[1].texts[-1].get_position()[0], -5)) # adjust pos. of output

plt.tight_layout()
plt.show()
# # now save the image
# fig.savefig("my_sankey.pdf",bbox_inches="tight",dpi=800)
