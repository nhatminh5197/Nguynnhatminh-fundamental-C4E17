from flask import Flask,render_template,redirect
app = Flask(__name__)


@app.route('/')

@app.route('/bmi/<int:w>/<int:h>')

def bmi_calc(w,h):

    bmi = w/(h*h)
    if bmi < 16:
        condition = 'Severe underweight'
    elif 16 <= bmi <= 18.5:
        condition = 'underweight'
    elif 18.5 <= bmi <= 25 :
        condition = 'Normal'
    elif 25 <= bmi <= 30 :
        condition = 'Overnight'
    else:
        condition = 'Obseve'

    return render_template('index1.html', inf=information)

if __name__ == '__main__':
  app.run( debug=True)
