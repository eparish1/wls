from pylab import *
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
rc('text.latex', preamble='\usepackage{amsmath},\usepackage{amssymb}')
import os
axis_font = {'size':16,'family':'serif'}
mpl.rc('font',family='serif')
rc('text', usetex=True)
axis_font = {'size':'14'}
close("all")
import matplotlib.patches as patches
fig,ax = plt.subplots(1)
matplotlib.pyplot.arrow(0.,0.,1.,0.,head_width=0.05,head_length=0.05,color='black')
rsz = 0.02
nslabs = 4
dx = 1./nslabs
slab_start = linspace(0.,1.-dx,nslabs)
for i in range(0,np.size(slab_start)):
  start = slab_start[i]
  rect = patches.Rectangle((start-rsz/2.,-rsz/2.),rsz,rsz,linewidth=1,edgecolor='black',facecolor='none')
  ax.add_patch(rect)
  matplotlib.pyplot.text(start,rsz,r'$t_s^{}$'.format(i+1),**axis_font)
  if (i > 0):
    matplotlib.pyplot.text(start,rsz*5,r'$t_f^{}$'.format(i),**axis_font)
    matplotlib.pyplot.text(start - dx/5*3,-rsz*4,r'$\Delta T^{}$'.format(i),**axis_font)
matplotlib.pyplot.text(start + dx/5*2,-rsz*3,r'$\ldots$'.format(i),**axis_font)
 
ylim([-0.2,0.2])
xlim([-0.1,1.1])
ax.set_aspect(aspect=1.)
ax.axis('off')
#ax.set_xticks([])
#ax.set_yticks([])
savefig('time_grid.pdf')
show()
