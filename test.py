from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	city = request.form['city']
	country_code = request.form['cou_code']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city +',' + country_code + '&appid=<your api key>') #get a api key from openweathermap
	json_obj = r.json()
	temp_k = float(json_obj['main']['temp'])
	temp_k = temp_k - 273.15
	status = json_obj['weather'][0]['main']
	descp = json_obj['weather'][0]['description']
	#return status
	return render_template('temperature.html', city=city, temp=str(temp_k), status=status, descp = descp)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)