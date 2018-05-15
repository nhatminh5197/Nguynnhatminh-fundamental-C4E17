from mongoengine import *


# design database
# creat collection

class Service(Document):
    name = StringField() #field = laf ten , gioi tinh . tuoi
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# service = Service(name = "Kieu Trinh",
#                     yob=1997,
#                     gender=0,
#                     height = 168,
#                     phone="0987450000",
#                     address="Ho chi minh",
#                     status = False)
#
# service.save()
