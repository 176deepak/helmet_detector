import os
from flask import Flask, request, render_template, session, redirect, url_for
from src.pipeline.prediction_pipeline import image_pred


app = Flask(__name__, template_folder='templates', static_folder='static')

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '6RD2002'


@app.route('/detector')
def img_vid_detector(path):
    return render_template('img_vid_detector.html', path=path)  


@app.route('/',  methods=['GET','POST'])
def index():
    if request.method == "POST":
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.mkdir(app.config['UPLOAD_FOLDER'])

        _img = request.files['myPhoto']
        filename = _img.filename
        _img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # path = image_pred(filename)
                
        # return redirect(url_for('img_vid_detector', path=path))
    return render_template('index.html')
  

@app.route('/detector')
def live_helmet_detector():
    return render_template('live_helmet_detector.html')

if __name__ == '__main__':
    app.run(debug=True)