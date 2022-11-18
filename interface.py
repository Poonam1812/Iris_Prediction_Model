from flask import Flask, jsonify,render_template, request, redirect, url_for
import config
from iris_app.utils import Iris

app = Flask(__name__)
#model = pickle.load(open("iris_app",'iris_Logistic_model.pkl', 'rb'))
@app.route("/") # HOme API

def hello_iris():
    print("welcome to IRIS Prediction")
    return render_template("home.html")

@app.route('/result')
def result():
    
    
    return "successful"
################################################################################
################################################################################

@app.route("/predict", methods= ['POST','GET'])

def get_pred_species():

    #data=request.form
    #print("data is :", data)  # immutable dictionary
    if request.method =='POST':
        SepalLengthCm = request.form['SepalLengthCm']
        print("SepalLengthCm",SepalLengthCm)
        SepalWidthCm = request.form['SepalWidthCm']
        print("SepalWidthCm",SepalWidthCm)
        PetalLengthCm = request.form['PetalLengthCm']
        print("PetalLengthCm",PetalLengthCm)
        PetalWidthCm = request.form['PetalWidthCm'] 
        print("PetalWidthCm",PetalWidthCm)
        #return redirect (url_for('result'))
    
        iris_predict = Iris(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
   
        pred_species=iris_predict.get_predicted_species()
    
        return render_template("result.html", pred=pred_species)

   
if __name__ =="__main__":
    app.run(debug=True)

