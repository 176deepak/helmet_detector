from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detector')
def img_vid_detector():
    return render_template('img_vid_detector.html')    

@app.route('/detector')
def live_helmet_detector():
    return render_template('live_helmet_detector.html')

if __name__ == '__main__':
    app.run(debug=True)