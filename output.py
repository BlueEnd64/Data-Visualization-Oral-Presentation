
!pip install -q xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics


df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/datasets/eap2281-sup-0003-appendixs3.xlsx')



xls = pd.ExcelFile('/content/drive/MyDrive/Colab Notebooks/datasets/Pinzon_etal_EAP20-0549.R1.xlsx')
df1 = pd.read_excel(xls, 'Spiders')
df2 = pd.read_excel(xls, 'Ants')
df3 = pd.read_excel(xls, 'Carabid beetles')

def nameget(df):
  if df.iloc[3,4]=='Agelutah':
    return 'Spiders'
  elif df.iloc[3,4]=='Campnova':
    return 'Ants'
  else:
    return 'Carabid beetles'


def plotdata(df):

  print(type(df))
  data = pd.DataFrame(df)

  rows=[]
  savex=0
  Species=[]
  for x in range(302):
    if type(data['Family'].loc[x])==type(str()):
      Species.append(data['Family'].loc[x])
      rows.append([savex,x])
      savex=x
  rows.pop(0)
  Species.pop(-1)

  for v in range(len(rows)):
    print(Species[v],rows[v])

  ask_Species=input('Enter Species name:')
  for f in list(data['Species']):
    if str(f).find(ask_Species) == 0:
      print(list(data['Species']).index(f))


  species_plot=int(input('Enter Species index:'))#

  inplotx=['Burn Forest', 'Burn Edge', 'Burn Line', 'Unburn Forest', 'Unburn Edge', 'Unburn Line', 'Total']

  inploty=[]
  for x in inplotx:
    inploty.append(data[x].loc[species_plot])

  y = np.array(inploty)

  for x in rows:
    if species_plot in range(x[0],x[1]):
      intitle_Family=Species[rows.index(x)]

  plt.title('Family %s | Species %s'%(intitle_Family,data['Species'].loc[species_plot]))
  print(x,y)
  plt.barh(inplotx,y)
  plt.show()


def dexplot(dexframe,dexin):
  print('The plotable indexs in the frame are 3 to %s.'%(len(dexframe.columns)-1))
  inplotx=[]
  inploty=[]
  for x in range(4,49):
    if dexframe.iloc[x,dexin] != 0:
      yin=dexframe.iloc[x,dexin]
      xin=str(dexframe.iloc[x,0]+dexframe.iloc[x,1]+dexframe.iloc[x,2])
      inplotx.append(xin)
      inploty.append(yin)

  plt.title(df1.iloc[3,dexin])
  plt.barh(inplotx,inploty)
  plt.show()

def sitemean(dataset):
  """
  prints out the means of each site in two list brun unbrun 
  and finds the highits mean of brun and unbrun 
  """

  lstBSite=[]
  lstmeanB=[]
  outhighB=[]
  for x in range(4,31):
    lstBSite.append(str(dataset.iloc[x,0]+' '+dataset.iloc[x,1]+' '+dataset.iloc[x,2]))
    lstmeanB.append(list(dataset.iloc[x,3:]))
  

  for x in lstmeanB:
    
    outhighB.append(statistics.mean(x))


  lstUSite=[]
  lstmeanU=[]
  outhighU=[]
  for x in range(31,49):
    lstUSite.append(str(dataset.iloc[x,0]+' '+dataset.iloc[x,1]+' '+dataset.iloc[x,2]))
    lstmeanU.append(list(dataset.iloc[x,3:]))
  

  for x in lstmeanU:
    outhighU.append(statistics.mean(x))

  print(max(outhighU),max(outhighB))
  print(lstUSite[outhighU.index(max(outhighU))],lstBSite[outhighB.index(max(outhighB))])


  y_pos=np.arange(len(lstBSite))
  fig, ax = plt.subplots()
  hbars = ax.barh(y_pos, outhighB,  align='center')
  ax.set_yticks(y_pos, labels=lstBSite)
  ax.invert_yaxis()  # labels read top-to-bottom
  ax.set_xlabel('Abundance')
  ax.set_title('Abundance of %s.'%nameget(dataset))
  # Label with specially formatted floats
  ax.bar_label(hbars, fmt='%.2f')
  ax.set_xlim(left=0) 

  y_pos=np.arange(len(lstUSite))
  fig, ax = plt.subplots()
  hbars = ax.barh(y_pos, outhighU,  align='center')
  ax.set_yticks(y_pos, labels=lstUSite)
  ax.invert_yaxis()  # labels read top-to-bottom
  ax.set_xlabel('Abundance')
  ax.set_title('Abundance of %s.'%nameget(dataset))
  # Label with specially formatted floats
  ax.bar_label(hbars, fmt='%.2f')
  ax.set_xlim(left=0) 




def speciesmean(dataset):

  specienameslst=[]
  specievalue=[]
  for x in range(3,len(df2.columns)):
    specienameslst.append(str(dataset.iloc[3,x]))
    specievalue.append(list(dataset.iloc[4:,x]))


  speciesmeanget=[]
  for x in specievalue:
    speciesmeanget.append(statistics.mean(x))

  print(max(speciesmeanget),specienameslst[speciesmeanget.index(max(speciesmeanget))])
  


  y_pos=np.arange(len(specienameslst))
  
  fig, ax = plt.subplots()

  hbars = ax.barh(y_pos, speciesmeanget,  align='center')
  ax.set_yticks(y_pos, labels=specienameslst)
  ax.invert_yaxis()  # labels read top-to-bottom
  ax.set_xlabel('Abundance')
  ax.set_title('Abundance of %s.'%nameget(dataset))

  # Label with specially formatted floats
  ax.bar_label(hbars, fmt='%.2f')
  ax.set_xlim(left=0) 







def speciesBaUmean(dataset):

  specienameslst=[]
  specievalue=[]
  for x in range(3,len(df2.columns)):
    specienameslst.append(str(dataset.iloc[3,x]))
    specievalue.append(list(dataset.iloc[4:,x]))

  speciesmeanUget=[]
  speciesmeanBget=[]
  for x in range(len(df2.columns)-3):
    speciesmeanBget.append(round(statistics.mean(specievalue[x][0:27]),2))
    speciesmeanUget.append(round(statistics.mean(specievalue[x][27:]),2))

  

  print(speciesmeanBget)
  print(speciesmeanUget)

  #from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py 

  species = specienameslst
  specie_means = {
    'Brun': speciesmeanBget,
    'Unbrun': speciesmeanUget,
  }

  x = np.arange(len(species))  # the label locations
  width = 0.5  # the width of the bars
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  for attribute, measurement in specie_means.items():
      offset = width * multiplier
      rects = ax.bar(x + offset, measurement, width, label=attribute)
      ax.bar_label(rects, padding=3, rotation='vertical')
      multiplier += 1

  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Abundance()')
  ax.set_title('Abundance in Brun and Unbrun by species\n')
  ax.set_xticks(x + width, species)
  plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
  ax.legend(loc='upper right', ncols=3)
  plt.show()


#dexplot(df1,22)

#sitemean(df3)

#speciesBaUmean(df1)

print('-----------------------------------------------------------------------------')


#speciesmean(df1)



#plotdata(df)



