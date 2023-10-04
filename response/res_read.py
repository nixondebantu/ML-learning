import json

with open("response\demo.json", "r") as file:
    finaldata = json.load(file)
    #lat-lon-maxtemp_c-avgtemp_c-maxwind_kph-avghumidity-temp_c-wind_kphhumidity
    print(finaldata['location']['lat'],finaldata['location']['lon'],finaldata['forecast']['forecastday'][0]['day']['maxtemp_c'],finaldata['forecast']['forecastday'][0]['day']['avgtemp_c'],
          finaldata['forecast']['forecastday'][0]['day']['maxwind_kph'],finaldata['forecast']['forecastday'][0]['day']['avghumidity'],finaldata['forecast']['forecastday'][0]['hour'][0]['temp_c'],
          finaldata['forecast']['forecastday'][0]['hour'][0]['wind_kph'],finaldata['forecast']['forecastday'][0]['hour'][0]['humidity'])