from flask import Flask
from flask import request
from flask_cors import CORS
from flask_pymongo import PyMongo
import random
import json

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
internalipcollection = mongo.db.internalip

@app.route("/")
def hello_world():
    return 'Hello'
    # lengthdb = mongo.db.length
    # count = lengthdb.find_one({})
    # countnumber = int(count['count'])
    # # return str(count.count)
    
    # if(countnumber < 13):
    #     print('nolinktrigger')
    #     incrementcountnumber = countnumber + 1
    #     lengthdb.find_one_and_update({},{'$set': {'count': incrementcountnumber}})
    #     return 'nolinktrigger'

    # elif(countnumber == 20):
    #     lengthdb.find_one_and_update({},{'$set': {'count': 1}})
    #     return 'trigger'
    # else:
    #     b = random.randrange(0,3)
    #     if(b == 2):
    #         lengthdb.find_one_and_update({},{'$set': {'count': 1}})
    #         return 'trigger'
    #     else:
    #         incrementcountnumber = countnumber + 1
    #         lengthdb.find_one_and_update({},{'$set': {'count': incrementcountnumber}})
    #         return 'nolinktrigger'


@app.route("/lengthtrigger")
def lengthtriggerr():
    lengthdb = mongo.db.length
    count = lengthdb.find_one({})
    countnumber = int(count['count'])
    # return str(count.count)
    ###################### NEW FOR SHOPLIZZA MOZILLA START #############################
    return 'trigger'
    ###################### END #############################
    
    if(countnumber < 13):
        print('nolinktrigger')
        incrementcountnumber = countnumber + 1
        lengthdb.find_one_and_update({},{'$set': {'count': incrementcountnumber}})
        return 'nolinktrigger'

    elif(countnumber == 20):
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

@app.route("/verifyip", methods=['GET','POST'])
def Verifyipp():
    if request.method == 'POST':
        neww = request.get_json()
        # print(neww)
        myip = neww['ip']
        uniqueip = mongo.db.ip
        isuniqip = uniqueip.find_one({'uniqueipp': myip})
        if(isuniqip):
            return 'ip-already-used'
        else:
            adduniqip = uniqueip.insert_one({'uniqueipp': myip})
            return 'ip-never-used'

@app.route("/createinstance", methods=['GET','POST'])
def createinstancee():
    if request.method == 'POST':
        neww = request.get_json()

        email = neww['ipindex']
        staticip1 = neww['externalip1']
        staticip2 = neww['externalip2']
        staticip3 = neww['externalip3']
        staticip4 = neww['externalip4']
        print('staticip1 --> ',staticip1, 'staticip2 --> ',staticip2, 'staticip3 --> ',staticip3, 'staticip4 --> ',staticip4)
    #     examplee = {
    #     "staticip1": staticip1,
    #     "staticip2": staticip2,
    #     "staticip3": staticip3,
    #     "staticip4": staticip4
    # }
    #     # print(createscript)
    #     return json.dumps(examplee)
        
        print(email)
        zonesss = {'northamerica-northeast1-a':'162','northamerica-northeast2-a':'188','southamerica-east1-b':'158','southamerica-west1-a':'194','us-central1-c':'128','us-east1-b':'142','us-east4-c':'150','us-east5-a':'202','us-south1-a':'206','us-west1-c':'138','us-west2-a':'168','us-west3-a':'180','us-west4-a':'182','europe-central2-a':'186','europe-north1-a':'166','europe-southwest1-a':'204','europe-west1-b':'132','europe-west10-a':'214','europe-west12-a':'210','europe-west2-c':'154','europe-west3-c':'156','europe-west4-a':'164','europe-west6-a':'172','europe-west8-a':'198','europe-west9-a':'200','australia-southeast1-b':'152','australia-southeast2-a':'192'}

        # projectID = 'silent-card-399405'
        # serviceaccount = '87528303241'
        # projectID = 'second-project-400407'
        # serviceaccount = '391024631902'
        # projectID = 'thirdproject-402906'
        # serviceaccount = '46009241767'
        projectID = 'fourthproject-403206'
        serviceaccount = '881354389191'
        # projectID = 'fifthproject-403206'
        # serviceaccount = '639344720889'
        # projectID = 'sixthproject-403206'
        # serviceaccount = '935058106745'
        # projectID = 'seventh-project-403509'
        # serviceaccount = '819592548762'
        # projectID = 'eightproject-403519'
        # serviceaccount = '1061222278482'
        # projectID = 'ninthproject-403617'
        # serviceaccount = '881502421034'
        # projectID = 'tenthproject-403809'
        # serviceaccount = '290708935561'
        # projectID = 'eleventhproject-403819'
        # serviceaccount = '772367206767'
        # projectID = 'twelvethproject'
        # serviceaccount = '1019604495584'
        # projectID = '	thirteenthproject-403907'
        # serviceaccount = '927901054910'
        listip1 = ""
        listip2 = ""
        listip3 = ""
        listip4 = ""
        # listip5 = ""
        key, value = list(zonesss.items())[int(email)]
        print("Get key of specified index:", key)  
        print("Get value of specified index:", value)
        # return 'echo 12345'
        zone = key
        zoneip = value 
        for y in range(1,5):
            ran = True
            while ran == True:
                tempip = f"10.{zoneip}.{random.randrange(0,14)}.{random.randrange(0,255)}"
                # tempip = f"10.138.9.55"
                print(tempip)
                # tempip = '10.162.6.42'
                isuniqip = internalipcollection.find_one({'uniqueipp': tempip})

                if(isuniqip):
                    print('Duplicate found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    ran = True
                    continue
                else:
                    
                    adduniqip = internalipcollection.insert_one({'uniqueipp': tempip})
                    if y == 1:
                        listip1 = tempip
                    elif y == 2:
                        listip2 = tempip
                    elif y == 3:
                        listip3 = tempip
                    elif y == 4:
                        listip4 = tempip
                    # elif y == 5:
                    #     listip5 = tempip
                    ran = False
        #createscript = f"gcloud compute instances create instance-1 --project=silent-card-399405 --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,private-network-ip={listip1},subnet=default --metadata=startup-script=\\#\\!/bin/bash$'\\n'sudo\\ apt-get\\ update\\ -y$'\\n'sudo\\ apt\\ install\\ python3-pip\\ -y$'\\n'sudo\\ apt\\ install\\ wget\\ -y$'\\n'sudo\\ apt\\ install\\ ffmpeg\\ -y$'\\n'sudo\\ apt\\ install\\ unzip$'\\n'wget\\ https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip$'\\n'unzip\\ chromedriver-linux64.zip$'\\n'cd\\ chromedriver-linux64$'\\n'chmod\\ \\+x\\ chromedriver$'\\n'sudo\\ mv\\ -f\\ chromedriver\\ /usr/local/share/chromedriver$'\\n'sudo\\ ln\\ -s\\ /usr/local/share/chromedriver\\ /usr/local/bin/chromedriver$'\\n'sudo\\ ln\\ -s\\ /usr/local/share/chromedriver\\ /usr/bin/chromedriver$'\\n'wget\\ -q\\ -O\\ -\\ https://dl-ssl.google.com/linux/linux_signing_key.pub\\ \\|\\ sudo\\ apt-key\\ add\\ -$'\\n'echo\\ \\'deb\\ \\[arch=amd64\\]\\ http://dl.google.com/linux/chrome/deb/\\ stable\\ main\\'\\ \\|\\ sudo\\ tee\\ /etc/apt/sources.list.d/google-chrome.list$'\\n'sudo\\ apt-get\\ update\\ -y$'\\n'sudo\\ apt-get\\ install\\ google-chrome-stable\\ -y$'\\n'sudo\\ pip3\\ install\\ selenium$'\\n'sudo\\ apt\\ install\\ git\\ -y$'\\n'pip3\\ install\\ undetected_chromedriver$'\\n'sudo\\ pip3\\ install\\ SpeechRecognition$'\\n'sudo\\ pip3\\ install\\ pydub$'\\n'sudo\\ pip3\\ install\\ names$'\\n'cd\\ /usr/local/share$'\\n'sudo\\ git\\ clone\\ https://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@github.com/jatinjd17/ubuntuserver.git$'\\n'cd\\ ubuntuserver/$'\\n'sudo\\ unzip\\ Grammar-Checker-Paraphraser-–-LanguageTool\\ -d\\ ./Grammar/$'\\n'sudo\\ python3\\ newlanguagetoolauto.py,enable-oslogin=true --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=87528303241-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --create-disk=auto-delete=yes,boot=yes,device-name=instance-1,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/silent-card-399405/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any"
        # createscript = f"gcloud compute instances create instance-2 --access-token-file=token.txt --project=silent-card-399405 --zone=europe-north1-a --machine-type=e2-medium --network-interface=network-tier=PREMIUM,private-network-ip={listip1},subnet=default --metadata=startup-script=\#\!/bin/bash$'\n'sudo\ apt-get\ update\ -y$'\n'sudo\ apt\ install\ python3-pip\ -y$'\n'sudo\ apt\ install\ wget\ -y$'\n'sudo\ apt\ install\ ffmpeg\ -y$'\n'sudo\ apt\ install\ unzip$'\n'wget\ https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip$'\n'unzip\ chromedriver-linux64.zip$'\n'cd\ chromedriver-linux64$'\n'chmod\ \+x\ chromedriver$'\n'sudo\ mv\ -f\ chromedriver\ /usr/local/share/chromedriver$'\n'sudo\ ln\ -s\ /usr/local/share/chromedriver\ /usr/local/bin/chromedriver$'\n'sudo\ ln\ -s\ /usr/local/share/chromedriver\ /usr/bin/chromedriver$'\n'wget\ -q\ -O\ -\ https://dl-ssl.google.com/linux/linux_signing_key.pub\ \|\ sudo\ apt-key\ add\ -$'\n'echo\ \'deb\ \[arch=amd64\]\ http://dl.google.com/linux/chrome/deb/\ stable\ main\'\ \|\ sudo\ tee\ /etc/apt/sources.list.d/google-chrome.list$'\n'sudo\ apt-get\ update\ -y$'\n'sudo\ apt-get\ install\ google-chrome-stable\ -y$'\n'sudo\ pip3\ install\ selenium$'\n'sudo\ apt\ install\ git\ -y$'\n'pip3\ install\ undetected_chromedriver$'\n'sudo\ pip3\ install\ SpeechRecognition$'\n'sudo\ pip3\ install\ pydub$'\n'sudo\ pip3\ install\ names$'\n'cd\ /usr/local/share$'\n'sudo\ git\ clone\ https://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@github.com/jatinjd17/ubuntuserver.git$'\n'cd\ ubuntuserver/$'\n'sudo\ unzip\ Grammar-Checker-Paraphraser-\–-LanguageTool\ -d\ ./Grammar/$'\n'sudo\ python3\ newlanguagetoolauto.py --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=87528303241-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --create-disk=auto-delete=yes,boot=yes,device-name=instance-1,image=projects/debian-cloud/global/images/debian-11-bullseye-v20230912,mode=rw,size=10,type=projects/silent-card-399405/zones/europe-north1-a/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any"
        ######################################## OLD SCRIPT FOR LANGUAGETOOL START ############################################
        # createscript1 = f"gcloud compute instances create instance-1 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip1},private-network-ip={listip1},subnet=default --metadata-from-file startup-script=my_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-1,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        # createscript2 = f"gcloud compute instances create instance-2 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip2},private-network-ip={listip2},subnet=default --metadata-from-file startup-script=my_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-2,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        # createscript3 = f"gcloud compute instances create instance-3 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip3},private-network-ip={listip3},subnet=default --metadata-from-file startup-script=my_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-3,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        # createscript4 = f"gcloud compute instances create instance-4 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip4},private-network-ip={listip4},subnet=default --metadata-from-file startup-script=my_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-4,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        ############################################# END #########################################

        ##################################### NEW SCRIPT FOR SHOPLIZZA START ###############################################
        createscript1 = f"gcloud compute instances create instance-1 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip1},private-network-ip={listip1},subnet=default --metadata-from-file startup-script=shoplizza_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-1,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        createscript2 = f"gcloud compute instances create instance-2 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip2},private-network-ip={listip2},subnet=default --metadata-from-file startup-script=shoplizza_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-2,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        createscript3 = f"gcloud compute instances create instance-3 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip3},private-network-ip={listip3},subnet=default --metadata-from-file startup-script=shoplizza_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-3,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        createscript4 = f"gcloud compute instances create instance-4 --project={projectID} --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,address={staticip4},private-network-ip={listip4},subnet=default --metadata-from-file startup-script=shoplizza_startup_script.sh --service-account={serviceaccount}-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-4,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/{projectID}/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any"
        ###################################   END     #####################################################
        
        # createscript = f"gcloud compute instances create instance-1 --project=silent-card-399405 --zone={zone} --machine-type=e2-medium --access-token-file=token.txt --network-interface=network-tier=PREMIUM,private-network-ip={listip1},subnet=default --metadata-from-file startup-script=my_startup_script.sh --service-account=87528303241-compute@developer.gserviceaccount.com --create-disk=auto-delete=yes,boot=yes,device-name=instance-1,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230907,mode=rw,size=10,type=projects/silent-card-399405/zones/{zone}/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any"
        value = {
        "createscript1": createscript1,
        "createscript2": createscript2,
        "createscript3": createscript3,
        "createscript4": createscript4
    }
        # print(createscript)
        return json.dumps(value)

@app.route("/deleteinstance", methods=['GET','POST'])
def deleteinstancee():
    if request.method == 'POST':
        neww = request.get_json()

        email = neww['ipindex']
        print(email)
        zonesss = {'northamerica-northeast1-a':'162','northamerica-northeast2-a':'188','southamerica-east1-b':'158','southamerica-west1-a':'194','us-central1-c':'128','us-east1-b':'142','us-east4-c':'150','us-east5-a':'202','us-south1-a':'206','us-west1-c':'138','us-west2-a':'168','us-west3-a':'180','us-west4-a':'182','europe-central2-a':'186','europe-north1-a':'166','europe-southwest1-a':'204','europe-west1-b':'132','europe-west10-a':'214','europe-west12-a':'210','europe-west2-c':'154','europe-west3-c':'156','europe-west4-a':'164','europe-west6-a':'172','europe-west8-a':'198','europe-west9-a':'200','australia-southeast1-b':'152','australia-southeast2-a':'192'}

        # projectID = 'silent-card-399405'
        # projectID = 'second-project-400407'
        # projectID = 'thirdproject-402906'
        projectID = 'fourthproject-403206'
        # projectID = 'fifthproject-403206'
        # projectID = 'sixthproject-403206'
        # projectID = 'seventh-project-403509'
        # projectID = 'eightproject-403519'
        # projectID = 'ninthproject-403617'
        # projectID = 'tenthproject-403809'
        # projectID = 'eleventhproject-403819'
        # projectID = 'twelvethproject'
        # projectID = 'thirteenthproject-403907'
        # serviceaccount = '87528303241'

        key, value = list(zonesss.items())[int(email)]
        print("Get key of specified index:", key)  
        print("Get value of specified index:", value)
        # return 'echo 12345'
        zone = key
        zoneip = value

        deletescript = f"gcloud compute instances delete instance-1 instance-2 instance-3 instance-4 --project={projectID} --access-token-file=token.txt --quiet --zone={zone}"

        return deletescript
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
