from flask import Flask, render_template, request
import joblib

diabetes = Flask(__name__)

model = joblib.load('diab_model.pkl')

@diabetes.route('/')
def home():
    return render_template('diabform.html')

@diabetes.route('/predict', methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)

    output = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    if output[0]==1:
        res = "The subject is likely to be a diabetic!!"
    else:
        res = "The subject is unlikely to be a diabetic!!"

    return render_template('predict.html', result = res)
    # return render_template('diabform.html', result = res)

#run the diabetes file
if __name__ =='__main__': 
    diabetes.run(debug=True)
