from flask import Flask, render_template, request
from sklearn.externals import joblib 


app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])

def index(Gender=None, Ethnicity=None, Major=None, HomeState=None):

         GPAHoursEarned= None

    if request.method == 'POST':

        if request.form['Gender'] and request.form['Ethnicity'] and request.form['Major'] and request.form['HomeState']:

            Gender = request.form['Gender']

            Ethnicity = request.form['Ethnicity']

            Major = request.form['Major']
            
            HomeState = request.form['HomeState']
            
            GPAHoursEarned = ballpark_estimator(int(sqft), float(condition))



    return render_template('index.html',

                           Gender=Gender,

                           Ethnicity=Ethnicity,
                           
                           Major=Major,
                           
                           HomeState=HomeState,

                           GPAHoursEarned=GPAHoursEarned)








if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)