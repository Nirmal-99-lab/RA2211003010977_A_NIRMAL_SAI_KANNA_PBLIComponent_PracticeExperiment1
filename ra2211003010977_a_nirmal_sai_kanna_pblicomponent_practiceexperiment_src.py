# -*- coding: utf-8 -*-
"""RA2211003010977_A_NIRMAL_SAI_KANNA_PBLIComponent_PracticeExperiment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f17MQUlqG_9M0LRkFsYb8ekK8YemfChz
"""

!pip install pandas numpy matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/country_wise_latest.csv')

df.head()

df.tail()

df.columns

df.info()

df.describe()

df.isnull().sum()

sns.pairplot(df)
plt.show()

sns.distplot(df['Recovered'])

sns.distplot(df['Deaths'])

sns.histplot(df, x="Deaths", kde=True)
plt.show()

sns.histplot(df, x="Recovered", kde=True)
plt.show()

sns.regplot(x='Deaths',y='Recovered',data=df,line_kws={"color":"violet"})

sns.lineplot(x='Deaths',y='Recovered',data=df)
plt.show()

