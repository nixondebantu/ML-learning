import json
import csv

with open("fire_nrt_SV-C2_386234.json", "r") as file:
    finaldata = json.load(file)

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['latitude', 'longitude', 'acq_date', 'acq_time'])

    count = 0
    for a in finaldata:
        if (a['confidence'] == 'h' and count < 100000):
            # Write a row for this data point
            acq_time_first_two_digits = int(str(a['acq_time'])[:2])
            writer.writerow([a['latitude'], a['longitude'], a['acq_date'], acq_time_first_two_digits])
            count = count + 1
    count = 0
    for a in finaldata:
        if (a['confidence'] == 'l' and count < 100000):
            # Write a row for this data point
            acq_time_first_two_digits = int(str(a['acq_time'])[:2])
            writer.writerow([a['latitude'], a['longitude'], a['acq_date'], acq_time_first_two_digits])
            count = count + 1