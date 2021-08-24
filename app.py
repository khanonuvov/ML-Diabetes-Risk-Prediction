from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Prediction_of_Diabetes.pkl", "rb"))



@app.route("/")
def home():
    return render_template("home.html")



@app.route("/predict", methods = ["POST"])
def predict():

    #age
    age = int(request.form["Age"])

    #Gender
    gender =request.form['Gender']
    if(gender=='Male'):
        gender= 1
    else:
        gender= 0
    
    #Polyuria
    polyuria = request.form['Polyuria']
    if(polyuria=='Yes'):
        polyuria = 1
    else:
        polyuria = 0
    
    #Polydipsia
    polydipsia = request.form['Polydipsia']
    if(polydipsia=='Yes'):
        polydipsia = 1
    else:
        polydipsia = 0
    
    #sudden weight loss
    sudden_weight_loss = request.form['sudden weight loss']
    if(sudden_weight_loss=='Yes'):
        sudden_weight_loss = 1
    else:
        sudden_weight_loss = 0
    
    #weakness
    weakness = request.form['weakness']
    if(weakness=='Yes'):
        weakness = 1
    else:
        weakness = 0

    #Polyphagia
    polyphagia = request.form['Polyphagia']
    if(polyphagia=='Yes'):
        polyphagia = 1
    else:
        polyphagia = 0

    #Genital thrush
    genital_thrush = request.form['Genital thrush']
    if(genital_thrush=='Yes'):
        genital_thrush = 1
    else:
        genital_thrush = 0

    #visual blurring
    visual_blurring = request.form['visual blurring']
    if(visual_blurring=='Yes'):
        visual_blurring = 1
    else:
        visual_blurring = 0

    #Itching
    itching = request.form['Itching']
    if(itching=='Yes'):
        itching = 1
    else:
        itching = 0

    #Irritability
    irritability = request.form['Irritability']
    if(irritability=='Yes'):
        irritability = 1
    else:
        irritability = 0

    #delayed healing
    delayed_healing = request.form['delayed healing']
    if(delayed_healing=='Yes'):
        delayed_healing = 1
    else:
        delayed_healing = 0

    #partial paresis
    partial_paresis = request.form['partial paresis']
    if(partial_paresis=='Yes'):
        partial_paresis=  1
    else:
        partial_paresis = 0

    #muscle stiffness
    muscle_stiffness = request.form['muscle stiffness']
    if(muscle_stiffness=='Yes'):
        muscle_stiffness = 1
    else:
        muscle_stiffness = 0

    #Alopecia
    alopecia = request.form['Alopecia']
    if(alopecia=='Yes'):
        alopecia = 1
    else:
        alopecia = 0

    #Obesity
    obesity = request.form['Obesity']
    if(obesity=='Yes'):
        obesity = 1
    else:
        obesity = 0
    
    #['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
    #'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
    #'Itching', 'Irritability', 'delayed healing', 'partial paresis',
    #'muscle stiffness', 'Alopecia', 'Obesity']
    
    prediction=model.predict([[
            age,
            gender,
            polyuria,
            polydipsia,
            sudden_weight_loss,
            weakness,
            polyphagia,
            genital_thrush,
            visual_blurring,
            itching,
            irritability,
            delayed_healing,
            partial_paresis,
            muscle_stiffness,
            alopecia,
            obesity
    ]])

    #output=round(prediction[0],2)
    if((round(prediction[0],2))==1):
        output = "Positve"
    else:
        output = "Negative"

    return render_template('home.html',str = "Diabetes Risk is ",diabetes_prediction= "{}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
