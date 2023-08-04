'''

Application: Helmet Detector using YOLOv8 

Can predict 2 classes: 
    0 --=> With helmet
    1 --=> Without helmet

File name: app.py
app.py: Entry or Execution entry point for application 

'''


#required modules
import os
import shutil
import cv2
from src.utils.main_utils import create_folder
# from ultralytics import YOLO
from flask import Flask, request, render_template, session, redirect, url_for, Response, send_from_directory
from src.pipeline.prediction_pipeline import image_pred


# initializing Flask application with Flask class
app = Flask(__name__, template_folder='templates', static_folder='static')

'''
    
Storage folders:-
    1. uploads = for storing uploaded images by users
    2. pred = folder for storing prediction by model
    3. result = folder for storing resultant images 

'''
UPLOAD_FOLDER = os.path.join('static', 'uploads')
PRED_IMG_FOLDER = r'runs\detect\predict'
RESULT_IMG_FOLDER = os.path.join('static', 'result')

# making folders as flask variable by which we can access it's value throughout the script
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PRED_IMG_FOLDER'] = PRED_IMG_FOLDER
app.config['RESULT_IMG_FOLDER'] = RESULT_IMG_FOLDER
# secret key 
app.secret_key = '6RD2002'

#model = YOLO(r'models\pretrained_models\yolov8n.pt')


'''

url route = /detector
This route comes in work when user wants to detect helmets in a image or video.
This route will render img_vid_detector.html template or this route will used for displaying detected image.

'''
@app.route('/detector')
def img_vid_detector():

    result = os.path.join('runs\detect\predict', session['filename'])
    image_filename = session['filename']

    if os.path.exists(app.config['PRED_IMG_FOLDER']):
        shutil.rmtree(app.config['PRED_IMG_FOLDER']) 
    os.mkdir(app.config['PRED_IMG_FOLDER'])

    shutil.copy(result, app.config['PRED_IMG_FOLDER'])

    path = 'pred/'+session['filename']

    return render_template('img_vid_detector.html', path=path) 


'''

Entry point route '/'
    -This route will render index.html when request.method != 'Post'
    -Else, will redirect to img_vid_detector route, after some computation
    
'''
@app.route('/',  methods=['GET','POST'])
def index():
    # checking data method 
    if request.method == "POST":
        # making user uploaded data folder when it's not exists 
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.mkdir(app.config['UPLOAD_FOLDER'])

        # extracting image and image name from form data and saves them into a user data folder
        _img = request.files['myPhoto']
        session['filename'] = _img.filename
        _img.save(os.path.join(app.config['UPLOAD_FOLDER'], session['filename']))

        # removing runs folder if it exists, so that program execution safe from program conflicts 
        if os.path.exists('runs'):
            shutil.rmtree(r'runs')

        # now calling image_pred function of prediction_pipeline
        image_pred(session['filename'])
        # removing the uploads folder so that we can manage the memory usage
        shutil.rmtree(r'static\uploads')

        return redirect(url_for('img_vid_detector'))
    
    return render_template('index.html')

   
if __name__ == '__main__':
    app.run(debug=True)