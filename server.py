from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])

def get_name():
    return 'Welcome to Flask 1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)
