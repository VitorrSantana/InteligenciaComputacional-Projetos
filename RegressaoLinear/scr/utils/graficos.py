import pandas  as pd
import numpy   as np
import seaborn as sns
import matplotlib.pyplot as plt

def title_labels (titleName,sizeFontTitle,xNameLabel,yNameLabel,sizeFontLabels=10):
    plt.title(titleName  ,fontsize   = sizeFontTitle)
    plt.xlabel(xNameLabel,fontsize = sizeFontLabels)
    plt.ylabel(yNameLabel,fontsize = sizeFontLabels)