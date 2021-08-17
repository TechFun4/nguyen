from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
  return 'ok'

app.run(host="0.0.0.0")