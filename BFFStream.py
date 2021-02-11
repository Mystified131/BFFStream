#This code imports the necessary modules.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random, datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$APPSTotal'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

app.secret_key = 'noiiuglsrjbijbovubj3irg'

class APPSTotal(db.Model):
    sessiondata = db.Column(db.String(120), primary_key=True)

    def __init__(self, sessiondata):
        self.sessiondata = sessiondata


@app.route('/', methods=['POST', 'GET'])
def sessstart():
    right_now = datetime.datetime.now().isoformat()
    list = []
    for i in right_now:
        if i.isnumeric():
            list.append(i)
    tim = "".join(list)
    sessiondata = tim + "_uniqueBFFhit"
    new_entry = APPSTotal(sessiondata)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('BFF.html')

#This code constructs the player page. It chooses an item randomly from a set of lists, and, after processing, opens a player page and cues up the item.

@app.route('/player', methods=['POST', 'GET'])
def make_player():

    songlength = random.randrange(300, 1000)

    tlst = []

    contentb = []

    infile = open("BFF_Sounds.m3u", "r")
    plist = infile.readline()
    while plist:
        contentb.append(plist)
        plist = infile.readline()
    infile.close()

    atrack = ""

    for trk in range(23):

        atracknum = random.randrange(0,len(contentb))
        atrack = contentb[atracknum]
        tlst.append(atrack)


    #dice = random.randrange(15)

    #if dice > 14:

        #atrack = ""

        #for trk in range(18):

            #tlst.append(atrack)


        #tlst[18] =  "/static/GenWeatherSpot.mp3"

    return render_template('BFF.html', toplay1 = tlst[0], toplay2 = tlst[1], toplay3 = tlst[2], toplay4 = tlst[3], toplay5 = tlst[4], toplay6 = tlst[5], toplay7 = tlst[6], toplay8 = tlst[7], toplay9 = tlst[8], toplay10 = tlst[9], toplay11 = tlst[10], toplay12 = tlst[11], toplay13 = tlst[12], toplay14 = tlst[13], toplay15 = tlst[14],  toplay16 = tlst[15], toplay17 = tlst[16], toplay18 = tlst[17], toplay19 = tlst[18], toplay20 = tlst[19], toplay21 = tlst[20], toplay22 = tlst[21], toplay23 = tlst[22], songlen = songlength )

## THE GHOST OF THE SHADOW ##

