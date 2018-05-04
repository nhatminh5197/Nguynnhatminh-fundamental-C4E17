from pymongo import MongoClient
from matplotlib import pyplot

url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(url)
db = client.get_default_database()

blog = db["customers"]

all_customers = blog.find()



count_events = blog.find({'ref':'events'}).count()

count_ads = blog.find({'ref':'ads'}).count()

count_wom = blog.find({'ref':'wom'}).count()

print(count_events)
print(count_ads)
print(count_wom)


data_count = [count_ads , count_events , count_wom]

machine_names = ["ads","events","wom"]

pyplot.pie(data_count , labels = machine_names, autopct = "%.1f%%", shadow = True , explode = [0,0,0])
pyplot.axis("equal")
pyplot.title("ads vs events vs wom")
pyplot.show()
