import cv2
import numpy as np
import os
import json
from flask import Flask,request,render_template,session

#Our lib
import Utilities as ut
import Database_user as db_user
import Analysis as magic
import Alerts 
import Outer_api as api

app = Flask(__name__)
app.secret_key = 'your_secret_key'


#flutter
@app.route('/uploadx', methods=['POST'])
def uploadx():
    framesArray = []
    user = request.files['username']
    for i in range(126):
        file = request.files[f'frame{i}']
        frame_bytes = file.read()
        np_frame = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
        framesArray.append(frame)
    ut.sendToModel(framesArray , user)
    return Response(response='Frames received', status=200)



#website
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db_user.authPass(username,password):
            session['value'] = username
            return render_template('x.html' , username = username)
        else:
            error_message = 'Invalid credentials. Please try again.'
        return render_template('x2.html', error_message=error_message)
    return render_template('x2.html')

@app.route('/upload', methods=['POST'])
def upload():
    video_file = request.files['video']
    video_path = os.path.join('D:/New folder', video_file.filename) 
    video_file.save(video_path)
    frames =ut.getFrames(video_path)
    username = request.form.get('username')
    x = ut.sendToModel(frames , username)
    return x



#client
@app.route('/chatgpt/<username>/<int:TimeInsec>', methods=['GET'])
def chatgpt(username,TimeInsec):
    TimeInsec = TimeInsec//5
    dic =magic.analysis(username ,TimeInsec )
    response = api.chatGpt(dic['overallEmotion'])
    return Response(response=response, status=200)

@app.route('/image/<username>/<int:TimeInsec>', methods=['GET'])
def image(username,TimeInsec):
    TimeInsec = TimeInsec//5
    dic =magic.analysis(username ,TimeInsec )
    response = api.image()
    return Response(response=response, status=200)

@app.route('/spotify/<username>/<int:TimeInsec>', methods=['GET'])
def spotify(username,TimeInsec):
    TimeInsec = TimeInsec//5
    dic =magic.analysis(username ,TimeInsec )
    response = api.spotify()
    return Response(response=response, status=200)




#supervisor
@app.route('/getAlerts/<PatientName>/<int:TimeInsec>', methods=['GET'])
def getAlerts(PatientName,TimeInsec):
    Alerts.send(PatientName,TimeInsec)
    response = Alerts.getAlerts(PatientName)
    response = json.dumps(response)
    return Response(response=response, status=200)

@app.route('/getReports/<username>/<int:TimeInsec>', methods=['GET'])
def getReports(username , TimeInsec):
    response = magic.analysis(username ,TimeInsec//5 )['report']
    response = json.dumps(response)
    return Response(response=response, status=200)

@app.route('/login/<username>/<password>', methods=['GET'])
def loginz(username,password):
        if db_user.authPass(username,password):
            return Response(response="ok", status=200)
        else:
            return Response(response = "no" , status = 200)
        
@app.route('/signup/<username>/<password>/<type>/<superVisorName>', methods=['GET'])
def signup(username,password,type,superVisorName):
    db_user.signup(username , password , type , superVisorName)
    return Response(response = "done" , status = 200)

@app.route('/getUser/<SupervisorName>', methods=['GET'])
def getUser(SupervisorName):
    response = db_user.getUsers(SupervisorName)
    response = json.dumps(response)
    return Response(response = response , status = 200)

@app.route('/AdvancedReport/<patientName>/<int:TimeInsec>', methods=['GET'])
def MainReportPage(patientName,TimeInsec):        
    response = magic.analysis(patientName ,TimeInsec//5 )
    response = ut.handlePlots(response)
    response = json.dumps(response)
    return Response(response = response , status = 200)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)