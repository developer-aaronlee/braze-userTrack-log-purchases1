import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/users/track'
API_KEY = 'Bearer api_key'

headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('(purchase)pvolveDuplicates020222.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) == 0:
            continue
        temp = row[0].split(",")
        if temp[0] == "external_id":
            continue

        body = json.dumps({
            "purchases": [{
                "external_id": temp[0],
                "product_id": temp[1],
                "time": temp[2],
                "quantity": float(temp[3]),
                "currency": temp[4],
                "price": float(temp[5])}
            ]})

        response = requests.post(url, data=body, headers=headers)
        print(response.json())
