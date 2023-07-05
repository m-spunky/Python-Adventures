from datetime import datetime
from email.mime import image
from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy

import os

PEOPLE_FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


full_file1 = os.path.join(app.config['UPLOAD_FOLDER'], 'shop1.jpg')
full_file2 = os.path.join(app.config['UPLOAD_FOLDER'], 'shop2.jpg')
full_file3 = os.path.join(app.config['UPLOAD_FOLDER'], 'shop3.jpg')

@app.route('/main')
def welcome1():
    return render_template('index.html', image1 = full_file1,image2 =full_file2,image3=full_file3)

@app.route('/shops')
def welcome2():
    return render_template('shops.html', image1 = full_file1,image2 =full_file2,image3=full_file3)

@app.route('/dest')
def welcome3():
    return render_template('destination.html')


if __name__=="__main__":
    app.run()