import requests

url = "http://delugedrop.com/3Dash/get_json.php" #url of where to send the request

payload = "id=9872" #id of the level you want
headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)