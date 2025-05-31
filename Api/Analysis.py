import pandas as pd
import numpy as np
from collections import Counter
import datetime
import statistics

import matplotlib
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.nonparametric.smoothers_lowess import lowess

#Our lib
import Database_emotion as db
#matplotlib.use('Qt5Agg')


data = []
def analysis(userName , emotionNumber):  
    
    dic = {}
    
    data = db.retrieve(userName, emotionNumber)
    emotionNumber = len(data)
    
    #To handle when the data is empty
    data.append("pos")
    emotionNumber += 1
    
    df = init(data)
    TimeAxis = np.arange(0, emotionNumber * 5, 5)
    dic['userName'] = userName
    dic['emotionNumber'] = emotionNumber
    
    overallEmotion = getOverallEmotion(df['emotion'])
    dic['overallEmotion'] = overallEmotion
    
    # the last paramater is the windows size
    fig , p = smothingValue(df['numericalEmotion'] ,TimeAxis, 3 )
    dic['smothingValue'] = fig
    dic['slop'] = p.tolist()

    fig = highlightCurv(df['numericalEmotion'] ,TimeAxis )
    dic['highlightcurv'] = fig
     #the last specify how much we want to predict
    fig = predictEmotion(df['numericalEmotion'], TimeAxis, emotionNumber/3)
    dic['predictEmotion'] = fig

    fig = movingAvg(df['numericalEmotion'], 10)
    dic['movingAvg'] = fig

    fig =  loess(df['numericalEmotion'] , TimeAxis)
    dic['loess'] = fig
    #the last paramater for lag
    fig =  autoCorrelation(df['numericalEmotion'] , len(df['numericalEmotion'])-1)
    dic['autoCorrelation'] = fig

    # the last paramater represent the periodc periodPattern
    trend , seasonal , residuals = getDecompastion(df['numericalEmotion'] , 3)
   
    fig = normalPlot(df['numericalEmotion'])
    dic['normalPlot'] = fig

    fig = trendlPlot(trend)
    dic['trendlPlot'] = fig

    fig = seasonalPlot(seasonal)
    dic['seasonalPlot'] = fig


    fig = residualsPlot(df['numericalEmotion'])
    dic['residualsPlot'] = fig

    directionOfEmotion  = getDirection(p) 
    dic['directionOfEmotion'] =directionOfEmotion
    
    pos , neg , ratio = getNumberOfEmotion(df['emotion'])
    dic['posNumber'] = pos
    dic['negNumber'] = neg
    dic['ratio'] = ratio
    
    report = getReport(df['emotion'], dic )
    dic['report'] = report
    
    return dic


    
def init(data):
    labelMapping = mappingToNumerical("numerical")
    
    startTime = datetime.datetime(1970, 1, 1)
    timeStamps = [startTime + datetime.timedelta(seconds=i*5) for i in range(len(data))]
    
    df = pd.DataFrame({'timeStamp': timeStamps, 'emotion': data})
    df['timeStamp'] = pd.to_datetime(df['timeStamp'])
    df.set_index('timeStamp', inplace=True)
    
    df["numericalEmotion"] = df["emotion"].map(labelMapping)
    
    return df

def mappingToNumerical(type):
    if type == "numerical":
        return {"neg": -1, "pos": 1}
    else:
        return {-1 : "neg" , 1:"pos"}

def getOverallEmotion(emotions):
    return statistics.mode(emotions)

def smothingValue(df ,TimeAxis, windowSize):
    rollingAvg = pd.Series(df).rolling(windowSize, min_periods=1).mean()
    
    xAxis = np.arange(len(df))
    p = np.polyfit(xAxis, rollingAvg, 1)
    trendLine = np.polyval(p, xAxis)
    
    fig, ax = plt.subplots()
    ax.plot(TimeAxis, rollingAvg)
    ax.plot(TimeAxis, trendLine, color='orange')
    ax.set_title(f'Smoothed Values with windows of size {windowSize} with Trend Line')
    ax.set_xlabel('Time')
    ax.set_ylabel('Emotion')
    return fig , p

def highlightCurv(df ,TimeAxis ):
    fig, ax = plt.subplots()
    ax.plot(TimeAxis, df, color='blue', label='Time Series Data',alpha=0.5)
    ax.fill_between(TimeAxis, -1,  df, where=np.array(df) == 1, color='green', alpha=0.3)
    ax.set_title('Time Series Data (Highlighted Curve)')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Value')
    ax.legend()
    return fig 

def getDecompastion(df , periodPattern):
    result = seasonal_decompose(df, period=periodPattern) 
    trend = result.trend
    seasonal = result.seasonal
    residuals = result.resid
    return trend , seasonal , residuals

date_format = mdates.DateFormatter('%S')
def normalPlot(df):
    fig, ax = plt.subplots()
    TimeAxis = np.arange(0, len(df) * 5, 5)
    ax.plot(TimeAxis,df, label='Original')
    ax.legend(loc='best')
    #fig.autofmt_xdate(rotation=45)  
    #ax.xaxis.set_major_formatter(date_format)  
    return fig



def trendlPlot(trend):
    fig, ax = plt.subplots()
    TimeAxis = np.arange(0, len(trend) * 5, 5)
    ax.plot(TimeAxis,trend, label='Trend')
    ax.legend(loc='best')
    #fig.autofmt_xdate(rotation=45)
    #ax.xaxis.set_major_formatter(date_format)  
    return fig



def seasonalPlot(seasonal):
    fig, ax = plt.subplots()
    TimeAxis = np.arange(0, len(seasonal) * 5, 5)
    ax.plot(TimeAxis,seasonal, label='Seasonal')
    ax.legend(loc='best')
    #fig.autofmt_xdate(rotation=45)
    #ax.xaxis.set_major_formatter(date_format)
    return fig

def residualsPlot(residuals):
    fig, ax = plt.subplots()
    TimeAxis = np.arange(0, len(residuals) * 5, 5)
    ax.plot(TimeAxis,residuals, label='Residuals')
    ax.legend(loc='best')
    fig.autofmt_xdate(rotation=45)
    ax.xaxis.set_major_formatter(date_format)
    return fig


def plotDomnint(df , TimeAxis):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    freq = df["value_n"].resample('5S').apply(lambda x: x.value_counts().index[0])

    # Plot the dominant emotion over time
    fig2, ax2 = plt.subplots(figsize=(10,5))
    freq.value_counts().plot(kind='barh', ax=ax2,color=colors)
    ax2.set_title('Dominant Emotion over Time')
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Emotion')
    return fig2


def getDirection(p):
    trendSlope = p[0]
    if trendSlope > 0:
        trendDirection = 'increasing'

    elif trendSlope < 0:
        trendDirection = 'decreasing'
    else:
        trendDirection = 'stable'
    return trendDirection

def DirectionAlerts(user , Numberemotion):
    data = db.retrieve(user, Numberemotion)
    df = init(data)
    
    TimeAxis = np.arange(0, Numberemotion * 5, 5)
    fig , p = smothingValue(df['numericalEmotion'] ,TimeAxis, 3 )
    
    trendSlope = p[0]
    if trendSlope > 0:
        trendDirection = 'increasing'

    elif trendSlope < 0:
        trendDirection = 'decreasing'
    else:
        trendDirection = 'stable'
    return trendDirection

def getNumberOfEmotion(df):
    counts = Counter(df)
    posCount = counts.get("pos", 0)
    negCount = counts.get("neg", 0)
    return posCount , negCount , posCount/negCount
    
def getReport(df , dic ):
    array = np.array(df).tolist()
    report = {
    'PatientName': dic['userName'],
    'ThisReportForTheLast' : str(dic['emotionNumber'])+" emotions",
    'dominantEmotion': dic['overallEmotion'],
    'posEmotionCount ': str( dic['posNumber']) +" out of "+str(dic['emotionNumber']),
    'negEmotionCount ': str( dic['negNumber']) +" out of "+str(dic['emotionNumber']),
    'rationOfPosEmotionsToNeg': dic['ratio'],
    'trendReport': {
    'direction':  dic['directionOfEmotion'],
    'lastFiveEmotions': array[-5:],
    }

    }
    return report

def predictEmotion(df, TimeAxis , emotion):
    model = AutoReg(df, lags=1)
    result = model.fit()
    forecast = result.predict(start=len(df), end=int(len(df)+emotion))
    fig, ax = plt.subplots()

    TimeAxis = np.arange(0, len(df) * 5, 5)
    TimeAxis2 = np.arange((len(df)-1)* 5, (len(df)-1)* 5+len(forecast) * 5, 5)
    ax.plot(TimeAxis2, forecast, label='Predicted Data')
    ax.set_xlabel('Date')
    ax.set_ylabel('Emotions')
    return fig
 
def movingAvg(df, windowSize):
    rollingMean = df.rolling(window=windowSize).mean()
    fig, ax = plt.subplots()

    TimeAxis = np.arange(0, len(df) * 5, 5)
    TimeAxis2 = np.arange(0, len(rollingMean) * 5, 5)
    ax.plot(TimeAxis, df, label='Original Data')
    ax.plot(TimeAxis2, rollingMean, label='Moving Average')
    ax.set_xlabel('Date')
    ax.set_ylabel('Emotions')
    ax.legend()
    #fig.autofmt_xdate(rotation=45)
    #ax.xaxis.set_major_formatter(date_format)
    return fig

def loess(df , TimeAxies):

    fig, ax = plt.subplots()
    frac = 0.1  
    smoothedData = lowess(df, TimeAxies, frac=frac)


    ax.plot(TimeAxies,df , label='Original Data')
    ax.plot(TimeAxies, smoothedData[:, 1], label='Smoothed Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Data')
    ax.set_title('LOESS Smoothing')
    ax.legend()
    return fig

def autoCorrelation(df , lags):
    fig, ax = plt.subplots()
    sm.graphics.tsa.plot_acf(df, lags=lags, ax=ax)
    ax.set_xlabel('Lag')
    ax.set_ylabel('Autocorrelation')
    ax.set_title('Autocorrelation Plot')
    return fig