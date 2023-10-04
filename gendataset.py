import csv
import json
import requests

BASE_URL = "http://api.weatherapi.com/v1/history.json?key=11dc12e69176434e917184442230310&q="
count = 0
# Open the input CSV file
with open('output.csv', 'r') as input_file:
    # Create a CSV reader
    reader = csv.reader(input_file)
    
    # Open the output CSV file
    with open('training dataset.csv', 'w', newline='') as output_file:
        # Create a CSV writer
        writer = csv.writer(output_file)
        
        # Loop through each row in the input CSV
        for row in reader:
            url = BASE_URL + row[0] + "," + row[1] + "&dt=" + row[2] + "&hour=" + row[3]
            finaldata = requests.get(url).json()
            
            # Write the finaldata to the output CSV. 
            # Assuming finaldata is a flat dictionary, we're writing the values of the dictionary.
            if count < 100000:
                writer.writerow([finaldata['location']['lat'],finaldata['location']['lon'],finaldata['forecast']['forecastday'][0]['day']['maxtemp_c'],finaldata['forecast']['forecastday'][0]['day']['avgtemp_c'],
                  finaldata['forecast']['forecastday'][0]['day']['maxwind_kph'],finaldata['forecast']['forecastday'][0]['day']['avghumidity'],finaldata['forecast']['forecastday'][0]['hour'][0]['temp_c'],
                  finaldata['forecast']['forecastday'][0]['hour'][0]['wind_kph'],finaldata['forecast']['forecastday'][0]['hour'][0]['humidity'],'h'])
            else:
                writer.writerow([finaldata['location']['lat'],finaldata['location']['lon'],finaldata['forecast']['forecastday'][0]['day']['maxtemp_c'],finaldata['forecast']['forecastday'][0]['day']['avgtemp_c'],
                  finaldata['forecast']['forecastday'][0]['day']['maxwind_kph'],finaldata['forecast']['forecastday'][0]['day']['avghumidity'],finaldata['forecast']['forecastday'][0]['hour'][0]['temp_c'],
                  finaldata['forecast']['forecastday'][0]['hour'][0]['wind_kph'],finaldata['forecast']['forecastday'][0]['hour'][0]['humidity'],'l'])
            count += 1
            if count >= 199999:
                break
