from typing import Any

from flask import Flask, render_template, request

# from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(gender: str = None, ethnicity: str = None, major: str = None, home_state: str = None,
          gra_hours_earned: str = None) -> str:
    if request.method == 'POST':
        if request.form['Gender'] and request.form['Ethnicity'] and request.form['Major'] and request.form['HomeState']:
            gender = request.form['Gender']
            ethnicity = request.form['Ethnicity']
            major = request.form['Major']
            home_state = request.form['HomeState']
            gra_hours_earned = request.form['GPAHoursEarned']

    return render_template('index.html',
                           Gender=gender,
                           Ethnicity=ethnicity,
                           Major=major,
                           HomeState=home_state,
                           GPAHoursEarned=gra_hours_earned)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
