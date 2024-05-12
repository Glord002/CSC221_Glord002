# -*- coding: utf-8 -*-
"""Special.Py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bHQlHX2acUckdirtX5CXKktDb4asahPf
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
response = requests.get(url)

data = pd.read_csv(url, skiprows=1)

data['Year'] = pd.to_datetime(data['Year'], format='%Y')

plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['J-D'], color='blue', linewidth=1)
plt.title('Global Temperature Anomalies (1880-2021)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid(True)
plt.tight_layout()

plt.savefig('special.png')
plt.show()