import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query":"Where there is data smoke, there is business fire."})
# get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.status_code)
print(get_response.json()["query"])
