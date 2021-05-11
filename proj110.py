import csv
import pandas as pd 
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go
df=pd.read_csv("project110.csv")
data=df["title"].tolist()
populationmean=statistics.mean(data)
print(populationmean)
standarddeviation=statistics.stdev(data)
print(standarddeviation)

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    figure=ff.create_distplot([df],["title"],show_hist=False)
    figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines'))
    figure.show()
    
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print(meanlist)

setup()



