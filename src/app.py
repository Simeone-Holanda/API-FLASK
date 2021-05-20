from flask import Flask


app = Flask(__name__)

@app.route('/user/', methods=['GET'])
def getAllUsers(id):
    return "<h1>Inicio</h1>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)