import requests




class DataManager:
    #This class is responsible for talking to the Google Sheet.
    response = requests.post(url="https://api.sheety.co/b5b3853a09c2ef4063292e7e976da595/flightDeals/prices")
    response.raise_for_status()
    data = response.json()
    print(data)
    pass