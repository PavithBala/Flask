from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':

        name = request.args.get('Name')
        dateOfJoining = request.args.get('DateOfJoining')

        return '''GET Method 
        Name = {}
        DateOfJoining = {}'''.format(name,dateOfJoining)

    elif request.method == 'POST':

        name = request.form.get('Name')
        dateOfJoining = request.form.get('DateOfJoining')

        return '''POST Method 
                Name = {}
                DateOfJoining = {}'''.format(name, dateOfJoining)

@app.route('/form',methods =['GET'])
def form():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(port=2000,debug=True)