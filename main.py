import requests
import json

city = (input("Enter the Name of the City\n"))

url = f"https://api.weatherapi.com/v1/current.json?key=cf54fee539144bfa965140759250609&q={city}"
r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
print(wdic["current"] ["temp_c"] , wdic["location"] ["region"])