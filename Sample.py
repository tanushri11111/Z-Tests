import plotly.figure_factory as ff 
import statistics
import random
import csv
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["id"].tolist()

mean=statistics.mean(data)
st_dv=statistics.stdev(data)

print("Mean of Data is : ",mean)
print("Standard Deviation of Data is : ",st_dv)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist = []
for i in range(0,1000):
    set_of_Mean = randomSetOfMean(100)
    meanlist.append(set_of_Mean)


firstSTART, firstEND = mean - st_dv, mean +  st_dv
secondSTART, ssecondEND= mean - (2*st_dv), mean + (2*st_dv)
thirdSTART, thirdEND = mean - (3*st_dv), mean + (3*st_dv)




fig = ff.create_distplot([meanlist],["Population Mean"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
fig.add_trace(go.Scatter(x=[firstSTART,firstEND], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
fig.show()

zScore = (mean - mean)/st_dv
print("Z Score is = ", zScore)
