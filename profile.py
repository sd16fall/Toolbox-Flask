from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/form_return/', methods=['POST'])
def form_return():
	if request.form['name'] == '' or request.form['age'] == '':
		return render_template('error.html')
	else:
		name = request.form['name']
		age = request.form['age']
		ninja = 'Patrick Huston'
		return render_template('form_display.html', name = name, age = age, ninja = ninja)

if __name__ == '__main__':
    app.run()