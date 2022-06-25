import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits



data = pd.read_csv("adult.csv")
data.dropna()
data.head(20)