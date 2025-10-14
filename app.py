from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register():
    return render_template('registration.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template('greetings.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)