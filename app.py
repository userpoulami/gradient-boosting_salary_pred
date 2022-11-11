from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)#initializing a flask app

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/report.html',methods=['GET'])  # route to display the home page
@cross_origin()
def report():
    return render_template("report.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        fnlwgt = int(request.form['Fnlwgt'])
        capitalgain = int(request.form["capital gain"])
        capitalloss = int(request.form["capital loss"])
        hoursperweek = int(request.form["hours per week"])
        education = int(request.form['Education'])
        workclass = int(request.form["workclass"])
        Educationalnum=int(request.form["Educational-num"])
        Maritalstatus=int(request.form["Marital-status"])
        Relationship=int(request.form["Relationship"])
        Race=int(request.form["Race"])
        Gender=int(request.form["Gender"])
        Nativecountry = int(request.form["Native-country"])
        occupation = int(request.form["occupation"])
        filename = "model.pickle"
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict([[Age,fnlwgt,education,Educationalnum,Maritalstatus,Relationship,Race,Gender,capitalgain,capitalloss,hoursperweek,Nativecountry,workclass,occupation]])
        print('prediction is', prediction)

        return render_template('result.html', prediction=prediction)


    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) #