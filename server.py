# server file for weather app
from flask import Flask, render_template

#Api key to establish handshake between Accu weather
API_KEY = "qQgGRb1A0A6R5HvKx7T37JCKdaAYG8GT"

app = Flask(__name__)


@app.route('/')
def search():
	return render_template("search.html")

	

@app.route('/get-weather', methods=['GET'])
def get_weather_data():
    """Search location data from ACCU weather site and return weather details."""
    location = request.args.get('location')
    context = {'apikey':API_KEY, 'q':location, 'language':'en-us'}
    response = requests.get('http://dataservice.accuweather.com/locations/v1/search',
                                 params=context)

    data = response.json()
    #print(response, response_list, location)
    
    location_key = data[0]['Key']

    response1 = requests.get('http://dataservice.accuweather.com/currentconditions/v1/%s' % location_key,
                                 params=context)

    # Process the JSON object into a list of results
    data1 = response1.json()
    text = data1[0]['WeatherText']
    temperature = data1[0]['Temperature']['Imperial']['Value']

    return render_template(
        'weather.html',       
        location=location,
        Text=text,
        Temperature=temperature,
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)