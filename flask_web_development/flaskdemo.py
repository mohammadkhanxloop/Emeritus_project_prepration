from flask import Flask, render_template, request

flaskdemo = Flask(__name__)

@flaskdemo.route('/')
def index():
    return 'Hello, Flask!'

@flaskdemo.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        output = f'Hello, {name}!'
        return render_template('submit.html', name=name, output=output)
    else:
        # Handle GET request
        return render_template('submit.html')

if __name__ == '__main__':
    flaskdemo.run(debug=True)



