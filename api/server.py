from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    f = open("filee.txt", "r")
    lines = int(f.read())
    if(lines < 5):
        print('true')
    print(str(lines))
    f.close
    if(lines < 13):
        print('nolinktrigger')
        y = open('filee.txt','w+')
        k = lines + 1
        y.write(str(k))
        y.close
        return 'nolinktrigger'

    elif(lines == 20):
        print('trigger')
        y = open('filee.txt','w+')
        y.write(str(1))
        y.close
        return 'trigger'
    else:
        b = random.randrange(0,3)
        if(b == 2):
            print('trigger')
            y = open('filee.txt','w+')
            y.write(str(1))
            y.close
            return 'trigger'
        else:
            print('nolinktrigger')
            y = open('filee.txt','w+')
            k = lines + 1
            y.write(str(k))
            y.close
            return 'nolinktrigger'
    # return "Hello World123!"
