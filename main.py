from flask import Flask
from flask import render_template, send_file, send_from_directory
import os, random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('index.html')


@app.route('/image/home/random')
def serve_random_image():
    # return image randomly from the images folder
    return send_file(random.choice(os.listdir('static/images/projects/')))
    


@app.route('/wrapper_images')
def serve_wraper():
    # choose random image from the images folder
    return render_template('wrapper_images.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)