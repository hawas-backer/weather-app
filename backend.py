import requests
import os


def get_data(place, days, kind):
    APIkey = os.getenv("Api_key1")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data("thala",3,"temp")