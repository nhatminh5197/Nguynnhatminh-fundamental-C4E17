from pymongo import MongoClient
#1 . connect to database server
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
#2 . get default database
db = client.get_default_database()
#3 . Get blog collection
blog = db["post"]

post = {
'title':"câu trả lời với c4e",
'author':"nhatminh",
'content':'''Cảm ơn C4e đẫ cho e cảm thấy lúc nào cũng sợ mât tiền , áp lực của deadline làm bài nè và đã cho e kiến thức , niềm đam mê vs code . Thứ mà đại học ko có đuoc'''
}
blog.insert_one(post)
