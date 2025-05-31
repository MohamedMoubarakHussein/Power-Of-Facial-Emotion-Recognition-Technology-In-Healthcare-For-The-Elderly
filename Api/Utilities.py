import numpy as np
import os
import cv2
import json
import joblib
from skimage.feature import hog

#our
import Database_emotion as db 


def feature(image):
    features = hog(image, orientations=9, pixels_per_cell=(32, 32), cells_per_block=(4, 4), visualize=False)
    return features

def convert(array):
    return np.array(array)


def getFrames(path):
    video_capture = cv2.VideoCapture(path)
    counter = 0
    freames = []
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        freames.append(frame)
    video_capture.release()
    return freames


face = cv2.CascadeClassifier("D:/Downloads/docs/FCIH/GP/apis/New folder/haarcascade_frontalface_alt2.xml")
def getTheFace(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(32, 32))
    t = 1
    if len(faces) > 0:
        (x, y, w, h)  = faces[0]
        frame = frame[y:y+h+20, x:x+w]
        frame = cv2.resize(frame, (224, 224))
    else:
        frame = np.zeros((224, 224), dtype=np.uint8)
        t = 0
    return frame ,t

def getFeatureVector(frames):
    arrayOfFeatureThatRepresentTheVideo = []
    counter = 0
    for frame in frames:
        frame = getTheFace(frame)
        frame = feature(frame[0])
        arrayOfFeatureThatRepresentTheVideo.append(frame)
    return arrayOfFeatureThatRepresentTheVideo


def convertVideoToFrames(video):
    frames = getFrames(video)
    return frames

model = joblib.load('model.pkl')
def sendToModel(frames, user):
    num_batches = len(frames) // 126
    x = []
    for i in range(num_batches):
        frame = frames[i * 126 : (i + 1) * 126]
        ArrayOfFeatures = getFeatureVector(frame)
        ArrayOfFeatures = np.array(ArrayOfFeatures)
        ArrayOfFeatures = ArrayOfFeatures.reshape(-1, 126, 2304)
        prediction = model.predict(ArrayOfFeatures)
        if prediction[0] > 0.5:
            prediction = "pos"
            x.append("pos")
        else:
            prediction = "neg"
            x.append("neg")
        print(x)
        db.store(user , prediction)
    return x

plots = ['smothingValue', 'highlightcurv' , 'predictEmotion' , 'movingAvg' , 'loess' , 'autoCorrelation','normalPlot', 'trendlPlot' , 'seasonalPlot' , 'residualsPlot']
def handlePlots(response):
    for plot in plots:
        Realplot =response[plot]
        numberOfLine = len(Realplot.get_children()[1].lines)
        dic = {}
        counter = 1
        for i in range(numberOfLine):
            line = Realplot.get_children()[1].lines[i]
            x = line.get_xdata()
            y = line.get_ydata()
            if not isinstance(x , list):
                x = x.tolist()
            if not isinstance(y , list):
                y = y.tolist()
            dic["LineNumber"+str(counter)] = {"x" :x,"y" :y}
            counter+=1
        response[plot] = dic
    return response
