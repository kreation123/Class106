import csv 
import numpy as np      
import plotly.express as px
def getdataSource(datapath):
    IceCream=[]
    ColdDrink=[]
    with open(datapath) as f :
        df = csv.DictReader(f)
        for row in df:
            IceCream.append(float(row['Temperature']))
            ColdDrink.append(float(row['Cold drink sales']))
    return {'x':IceCream, 'y':ColdDrink}
def findCorrelation(dataSource):
    Correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print(Correlation[0,1])
def setUp():
    dataPath='./Ice cream.csv'
    dataSource=getdataSource(dataPath)
    findCorrelation(dataSource)
setUp()