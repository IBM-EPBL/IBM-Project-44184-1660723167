from flask import Flask, render_template, request, flash, redirect
import random
import numpy as np
import tensorflow as tf
#from PIL import Image
from keras.models import load_model
#from tensorflow.keras.preprocessing import image
import os

UPLOAD_FOLDER = 'static/file/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    if request.method == 'POST':
        classes = ['PINEAPPLE', 'ORANGE', 'BANANA', 'WATERMELON', 'APPLES' ]
        m = load_model('nutrition.h5')
        file1 = request.files['img']
        imgfile = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(imgfile)
        img_ = tf.keras.utils.load_img(imgfile, target_size=(227, 227))
        img_array = tf.keras.utils.img_to_array(img_)
        img_processed = np.expand_dims(img_array, axis=0)
        img_processed /= 255.
        prediction = m.predict(img_processed)

        index = np.argmax(prediction)
        answer=""
        gram= ""
        if index == 0:
            answer = classes[index]
            print(answer)
            gram="nutrition value for apple is 95 calories, 0 gram fat, 1 gram protein, 25 grams carbohydrate, 19 grams sugar (naturally occurring), and 3 grams fiber."
            print(gram)
        elif index == 1:
            answer = classes[index]
            print(answer)
            trion = "nutrition value for avocado is  240 calories, 13 grams carbohydrate, 3 grams protein, 22 grams fat (15 grams monounsaturated, 4 grams polyunsaturated, 3 grams saturated), 10 grams fiber, and 11 milligrams sodium"
            gram = trion
        elif index == 2:
            answer = classes[index]
            print(answer)
            gram="nutrition value for banana is 110 calories, 0 gram fat, 1 gram protein, 28 grams carbohydrate, 15 grams sugar (naturally occurring), 3 grams fiber, and 450 mg potassium."
            print(gram)
        elif index == 3:
            answer = classes[index]
            print(answer)
            gram ="nutrition value for banana red is vitamin B6, magnesium, and vitamin C make this banana variety particularly nutrient dense. Summary The red banana is of great nutritional value. It's rich in essential minerals, vitamin B6, and fiber"
            print(gram)
        elif index == 4:
            answer = classes[index]
            print(answer)
            gram = "nutrition value for blueberry is fiber, vitamin C, vitamin K, manganese and potassium in every handful of blueberries – at just 80 calories per cup."
            print(gram)
        elif index == 5:
            answer = classes[index]
            print(answer)
            gram = "nutrition value for grape is Calories: 104. Carbs: 27 grams. Protein: 1 gram."
            print(gram)

        answer=answer
        gram= gram
        return render_template('predict.html', pred=answer, result=gram)
if __name__ == '__main__':
        app.run(debug=True)


