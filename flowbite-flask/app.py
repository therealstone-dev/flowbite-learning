from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():


	email = request.form.get('email', '')
	password = request.form.get('password', '')


if __name__ == '__main__':
	app.run(debug=True)