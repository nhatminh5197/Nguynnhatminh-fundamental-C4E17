from flask import Flask,render_template,redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    information = {
    "name":"Nguyen Nhat Minh",
    "age":18,
    "gender":"male",
    "Work":"Student",
    "School":"DHBKHN",
    "Hobiies":"football"
   }

    return render_template("index.html",inf = information)

@app.route('/school')
def school1():
       return redirect('http://techkids.vn ' )






if __name__ == '__main__':
  app.run( debug=True)
