import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = "uOStceKl5K3VGYJww4dBBkFowjxWpNMc"
        self._api_secret = "Yw09Uzkx1zBWp2Xi"
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        parameters = {
            "keyword": city_name.upper(),
            "max": 2,
            "include": "AIRPORTS"
        }
        response = requests.get(url=CITY_ENDPOINT, params=parameters, headers=headers)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        response.raise_for_status()
        return response.json()['access_token']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            'Authorization': f'Bearer {self._token}'
        }

        parameters = {
            'originLocationCode': origin_city_code,
            'destinationLocationCode': destination_city_code,
            'adults': "1",
            'nonStop': "true",
            'departureDate': from_time.strftime("%Y-%m-%d"),
            'returnDate': to_time.strftime("%Y-%m-%d"),
            'currencyCode': 'GBP',
            'max': "10",
        }

        response = requests.get(url=FLIGHT_ENDPOINT, params=parameters, headers=header)

        if response.status_code != 200:
            print(f"check_flight() response code: {response.status_code}")
            print("Response body:", response.text)
            return None

        return response.json()