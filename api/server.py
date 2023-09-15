from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['MONGO_DBNAME'] = 'languagetoolserverdb'
app.config['MONGO_URI'] = 'mongodb+srv://jatin:jatin123@cluster0.1zrdh.mongodb.net/languagetoolserverdb?retryWrites=true&w=majority'
CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})
mongo = PyMongo(app)
@app.route("/")
def hello_world():
    lengthdb = mongo.db.length
    count = lengthdb.find_one({})
    countnumber = int(count['count'])
    # return str(count.count)
    
    if(countnumber < 13):
        print('nolinktrigger')
        incrementcountnumber = countnumber + 1
        lengthdb.find_one_and_update({},{'$set': {'count': incrementcountnumber}})
        return 'nolinktrigger'

    elif(lines == 20):
        lengthdb.find_one_and_update({},{'$set': {'count': 1}})
        return 'trigger'
    else:
        b = random.randrange(0,3)
        if(b == 2):
            lengthdb.find_one_and_update({},{'$set': {'count': 1}})
            return 'trigger'
        else:
            incrementcountnumber = countnumber + 1
            lengthdb.find_one_and_update({},{'$set': {'count': incrementcountnumber}})
            return 'nolinktrigger'
    
    # f = open("filee.txt", "r")
    # lines = int(f.read())
    # if(lines < 5):
    #     print('true')
    # print(str(lines))
    # f.close
    # if(lines < 13):
    #     print('nolinktrigger')
    #     y = open('filee.txt','w+')
    #     k = lines + 1
    #     y.write(str(k))
    #     y.close
    #     return 'nolinktrigger'

    # elif(lines == 20):
    #     print('trigger')
    #     y = open('filee.txt','w+')
    #     y.write(str(1))
    #     y.close
    #     return 'trigger'
    # else:
    #     b = random.randrange(0,3)
    #     if(b == 2):
    #         print('trigger')
    #         y = open('filee.txt','w+')
    #         y.write(str(1))
    #         y.close
    #         return 'trigger'
    #     else:
    #         print('nolinktrigger')
    #         y = open('filee.txt','w+')
    #         k = lines + 1
    #         y.write(str(k))
    #         y.close
    #         return 'nolinktrigger'
    # return "Hello World123!"
