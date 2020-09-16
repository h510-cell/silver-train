import csv
import numpy
import pandas as pd
import plotly.express as px

def getDataSource():
    Days_present=[]
    Marks_in_percentage=[]

def find_correlation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corrcoef is ->"+correlation[0,1])

def plotFigure(dataPath):
    with open(dataPath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df , x:"Days Present"
                            , y:"Mark In Percentage",Color="Roll No")

def setup():
    dataPath = "Student Marks vs Days Present.csv"

    dataSource = getDataSource()
    find_correlation(dataSource)
    plotFigure(dataPath)

fig.show()