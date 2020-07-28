from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html', submitted=False)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return 'Form submitted'
    else:
        return 'Something went wrong'
        