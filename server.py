from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://root:root@mycluster-shard-00-00.hax9w.gcp.mongodb.net:27017,mycluster-shard-00-01.hax9w.gcp.mongodb.net:27017,mycluster-shard-00-02.hax9w.gcp.mongodb.net:27017/portofolio_db?ssl=true&replicaSet=atlas-328frz-shard-0&authSource=admin&retryWrites=true&w=majority")

@app.route('/')
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')

def write_to_database(data):
    mongo.db.messages.insert_one(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        return render_template('submit.html', submitted="True")
    else:
        return render_template('submit.html', submitted="False")
        