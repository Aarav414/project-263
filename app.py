from flask import Flask, render_template, request
import requests

app = flask(__name__)

@app.route("/")

def main():
	return render_template("index.html")
	@app.route('/',methods=['POST'])

def math():
	equation = request.form['text']
	operation = request.form['operation']
	api_link = f'https://newton.now.sh/api/v2//'+operation+'/'+ equation

requests.get(result).json()
answer = result[result]

def app.run():
	return.render_template(index.html,result=answer,equation=equation)
	if __name__ == "__main__":
		app.run()



