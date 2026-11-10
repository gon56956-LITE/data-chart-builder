from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import FancyArrowPatch, Rectangle
from scipy.stats import pearsonr

# Illustrative synthetic observations; no engineering or medical data.
rng = np.random.default_rng(72)
n = 160
u, v, w = rng.normal(size=(3, n))
X = np.column_stack((u, .75*u+.6*rng.normal(size=n), v, -.5*v+.8*rng.normal(size=n), w, rng.normal(size=n)))
y = .75*X[:,0] - .6*X[:,2] + .4*X[:,4] + rng.normal(size=n)
labels = ['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E', 'Feature F']
corr = np.corrcoef(X, rowvar=False)
links = [pearsonr(X[:,i],y) for i in range(len(labels))]
plt.rcParams.update({'font.family':'sans-serif','font.sans-serif':['Arial','DejaVu Sans','Liberation Sans'],'svg.fonttype':'none'})
fig, ax = plt.subplots(figsize=(11,8.2)); fig.subplots_adjust(left=.08,right=.86,top=.79,bottom=.23)
fig.text(.10,.94,'CORRELATION + OUTCOME LINKS',fontsize=11,fontweight='bold',color='#647c8b')
fig.text(.10,.89,'How the factors relate',fontsize=22,fontweight='bold',color='#1b3547')
fig.text(.10,.85,'Synthetic example  |  Pearson correlations  |  n = 160',fontsize=11,color='#627887')
N=len(labels); ax.set_xlim(-4.6,N+.1); ax.set_ylim(N+.05,-.1); ax.set_aspect('equal'); ax.axis('off')
cmap=plt.get_cmap('RdBu_r'); norm=TwoSlopeNorm(vmin=-1,vcenter=0,vmax=1)
for i in range(N):
 for j in range(i,N):
  ax.add_patch(Rectangle((j,i),1,1,facecolor='#f8fafb',edgecolor='#d5dfe4',linewidth=.8))
  if i==j:
   ax.text(j+.5,i+.5,labels[i],ha='center',va='center',fontsize=8.5,fontweight='bold',color='#18394e')
  else:
   r=corr[i,j]; side=.86*np.sqrt(abs(r)); ax.add_patch(Rectangle((j+.5-side/2,i+.5-side/2),side,side,facecolor=cmap(norm(r)),edgecolor='none'))
   if abs(r)>.4: ax.text(j+.5,i+.5,f'{r:.2f}',ha='center',va='center',fontsize=8,color='white')
for j,lab in enumerate(labels):ax.text(j+.5,-.18,lab,ha='left',va='bottom',rotation=45,fontsize=9,color='#29485a')
origin=(-4.05,5.35)
for i,res in enumerate(links):
 r,p=float(res.statistic),float(res.pvalue); color='#bd6152' if r>0 else '#397ba2'
 connection=FancyArrowPatch(origin,(i+.02,i+.5),connectionstyle=f'arc3,rad={-.09-.018*i}',arrowstyle='-',linewidth=.8+3*abs(r),linestyle='-' if p<.05 else (0,(3,3)),color=color,alpha=.86,zorder=0)
 ax.add_patch(connection)
ax.scatter(*origin,s=460,color='#e8f0f3',edgecolor='#8aa3b1',zorder=3)
ax.text(origin[0],origin[1]+.48,'Outcome',ha='center',va='top',fontsize=10,fontweight='bold',color='#29485a')
sm=plt.cm.ScalarMappable(norm=norm,cmap=cmap); cb=fig.colorbar(sm,ax=ax,shrink=.80,pad=.035,fraction=.035);cb.set_label('Predictor Pearson r',fontsize=10);cb.outline.set_visible(False)
fig.text(.10,.165,'Outcome links:   red = positive     blue = negative     width = |r|     solid: p < 0.05     dashed: p ≥ 0.05',fontsize=9.5,color='#29485a')
fig.text(.10,.125,'Matrix: square area = |r|. Pearson p-values are unadjusted; multiple tests shown for illustration.',fontsize=9,color='#607786')
fig.text(.10,.095,'Synthetic data; links and matrix describe association, not causation. No predictive model is used.',fontsize=9,color='#607786')
out=Path(__file__).resolve().parent.parent/'assets'/'correlation-link-heatmap-example'
for ext in ('svg','png'): fig.savefig(out.with_suffix('.'+ext),dpi=300,bbox_inches='tight')
plt.close(fig)