from flask import Flask, render_template
from mongoengine import *  # StringField , IntField , BooleanField,Document
from models.service import Service

import mlab

app = Flask(__name__)

mlab.connect()
# design database
# creat collection
# class Service(Document):
#     name = StringField() #field = laf ten , gioi tinh . tuoi
#     yob = IntField()
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
#



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g,address__exact='ha noi')
    return render_template('search.html',
                    all_service=all_service)

if __name__ == '__main__':
  app.run( debug=True)
