import requests

BEARER_TOKEN = "kdfjsklapo1kjis02js%jsi12"
SHEET_ENDPOINT = "https://api.sheety.co/643dccdcddb0204a103d7f46ce9f9a94/flightDeals/prices"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city["id"]}",
                json=new_data,
                headers=headers
            )
