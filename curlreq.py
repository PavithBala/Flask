from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def getcall():
    if request.method == 'GET':
        return 'This is GET Request'

    elif request.method == 'POST':
        name= request.json['name']
        place=request.json['place']
        data = {'name': name, 'place': place}
        return jsonify(data)


if __name__ == '__main__':
    app.run(port=7000,debug=True)