#import libraries
from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/request',methods=['GET','POST'])
def getcall():

    #Get Method
    if request.method == 'GET':
        return 'This is GET Request'

    #Post Method
    elif request.method == 'POST':

        #Converting json obj to python datastructures
        data =request.get_json()

        #Storing data in variables
        name = data["name"]
        place = data["place"]

       #return json object
        return jsonify({'request':'POST request','name':name,'place':place})


if __name__ == '__main__':
    app.run(port=7000,debug=True)