!pip install -q xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from matplotlib.pyplot import figure


"""
pont[x][0]=='Forest interior'
pont[x][1]=='Forest edge'
pont[x][2]=='Seismic line'
"""

def plotsitecon(pon):
  xls = pd.ExcelFile('/content/drive/MyDrive/Colab Notebooks/datasets/Pinzon_etal_EAP20-0549.R1.xlsx')
  dataf = pd.read_excel(xls, 'Site.conditions')

  if pon==0:
    sitehabitat='Forest interior'
  elif pon==1:
    sitehabitat='Forest edge'
  else:
    sitehabitat='Seismic line'

  pont= [[4,5,6]]
  while len(pont)<9:
    pont.append([pont[-1][0]+3,pont[-1][1]+3,pont[-1][2]+3])
  print(pont)

  conditionname=[]
  for x in range(2,len(dataf.columns)):
    conditionname.append(dataf.iloc[3,x])
  conditionname
  condition=[]
  addto=[]
  for y in range(2,len(dataf.columns)):
    addto=[]
    for x in pont:
      addto.append(dataf.iloc[x[pon],y])
    condition.append(addto)
  dicfi=dict(zip(conditionname,condition))
  keylst=dicfi.keys()
  keylst
  valmean=[]
  for x in keylst:
    valmean.append(statistics.mean(dicfi[x]))

  y_pos=np.arange(len(conditionname))
  
  fig, ax = plt.subplots()

  hbars = ax.barh(y_pos, valmean,  align='center')
  ax.set_yticks(y_pos, labels=conditionname)
  ax.invert_yaxis()  # labels read top-to-bottom
  ax.set_xlabel('Average')
  ax.set_title('Condition at %s Habitat.'%sitehabitat)
  # Label with specially formatted floats
  ax.bar_label(hbars, fmt='%.2f')
  ax.set_xlim(left=0) 


def plotsiteconbox(pon):
  xls = pd.ExcelFile('/content/drive/MyDrive/Colab Notebooks/datasets/Pinzon_etal_EAP20-0549.R1.xlsx')
  dataf = pd.read_excel(xls, 'Site.conditions')
  if pon==0:
    sitehabitat='Forest interior'
  elif pon==1:
    sitehabitat='Forest edge'
  else:
    sitehabitat='Seismic line'
  pont= [[4,5,6]]
  while len(pont)<9:
    pont.append([pont[-1][0]+3,pont[-1][1]+3,pont[-1][2]+3])
  print(pont)
  conditionname=[]
  for x in range(2,len(dataf.columns)):
    conditionname.append(dataf.iloc[3,x])
  conditionname
  condition=[]
  addto=[]
  for y in range(2,len(dataf.columns)):
    addto=[]
    for x in pont:
      addto.append(dataf.iloc[x[pon],y])
    condition.append(addto)
  dicfi=dict(zip(conditionname,condition))
  keylst=dicfi.keys()
  keylst
  val=[]
  valmean=[]
  for x in keylst:
    valmean.append(statistics.mean(dicfi[x]))
    val.append(dicfi[x])

  def bigvals():
    for y in range(4):
      x=valmean.index(max(valmean))
      box2v=(val.pop(x))
      box2c=[conditionname.pop(x)]
      fig, cwmv = plt.subplots(figsize=(6, 1))
      cwmv.set_ylabel('Condition')
      cwmv.invert_yaxis()
      cwmv.set_title('Condition at %s Habitat.'%sitehabitat)
      bplot = cwmv.boxplot(box2v,
                        patch_artist=True,  # fill with color
                        tick_labels=box2c,
                        orientation='horizontal')  
      plt.show()
  bigvals()

  fruit_weights = val
  labels = conditionname
  fig, ax = plt.subplots()
  ax.set_ylabel('Condition')
  ax.invert_yaxis()
  ax.set_title('Condition at %s Habitat.'%sitehabitat)
  bplot = ax.boxplot(fruit_weights,
                    patch_artist=True,  # fill with color
                    tick_labels=labels,# will be used to label x-ticks
                    orientation='horizontal')  

  
  

  plt.show()

plotsitecon(2)
plotsiteconbox(2)

