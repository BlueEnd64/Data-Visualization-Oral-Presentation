!pip install -q xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from matplotlib.pyplot import figure

def rovebeetles():
  xls = pd.ExcelFile('/content/drive/MyDrive/Colab Notebooks/datasets/Data.for.dryad.xlsx')
  data = pd.read_excel(xls, 'Catches')
  species=[]
  for x in range(3,len(data.columns)):
    species.append(data.iloc[:,x])
  meanB=[]
  meanU=[]
  for x in range(3,len(data.columns)):
    addto=[]
    for y in range(45):
      addto.append(data.iloc[y,x])

    meanB.append(statistics.mean(addto[:27]))
    meanU.append(statistics.mean(addto[27:]))

  species = list(data.columns)[3:]
  specie_means = {
    'Brun': meanB,
    'Unbrun': meanU,
  }
  x = np.arange(len(species))  # the label locations
  width = 0.5  # the width of the bars
  multiplier = 0
  fig, ax = plt.subplots(layout='constrained',figsize=(15, 6))
  for attribute, measurement in specie_means.items():
      offset = width * multiplier
      rects = ax.bar(x + offset, measurement, width, label=attribute)
      ax.bar_label(rects, padding=3, rotation='vertical')
      multiplier += 1
  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Abundance Average ')
  ax.set_title('Abundance Average in Brun and Unbrun by species\n')
  ax.set_xticks(x + width, species)
  plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
  ax.legend(loc='upper right', ncols=3)
  plt.show()

rovebeetles()
