# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 23:36:39 2021

@author: Praveesha
"""

from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing import image
import tensorflow as tf

app = Flask(__name__)
model=load_model('retina_weights.hdf5')
print("+"*50, "Model is loaded")
labels = {0: 'Mild', 1: 'Moderate', 2: 'No_DR', 3: 'Proliferate_DR', 4: 'Severe'}

@app.route('/')
@app.route('/base')
def index():
     return render_template("base.html" )


@app.route("/prediction")
def predict():
    return render_template("predict.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    
    img=request.files['img']
    img.save("img.png")
    image=cv2.imread("img.png")
    image = cv2.resize(image, (256,256))
    image = image / 255
    image = image.reshape(-1,256,256,3)
    pred = model.predict(image)
    pred = np.argmax(pred)
    pred=labels[pred]
    
    if(pred=='No_DR'):
        pred="No Diabetic Retinopathy"
    output="You're diagnosed with "+pred
   
    return render_template("predict.html", data=output)



if __name__ == "__main__":
    app.run(debug=True,port=9850,threaded = False)