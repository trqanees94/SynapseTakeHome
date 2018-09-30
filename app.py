from flask import Flask, render_template, request, redirect

from synapsefi import getUserData
from synapsefi import getNodes



app = Flask(__name__)
app.debug = True

userData = getUserData()
nodeData = getNodes()

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/getUserData")
def getUserData():

    return render_template('index.html', userData1= userData[0], userData2= userData[1], userData3= userData[2], nodeData = nodeData);
                                        #nodeData1 = nodeData[0][1], nodeData2 = nodeData[1][1], nodeData3 = nodeData[2][1]);

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run()
