from calendar import HTMLCalendar
import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World" })
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
# HTTP request -> HTML
# REST API HTTP REQUEST -> JSON

print(get_response.json())
# print(get_response.status_code)
