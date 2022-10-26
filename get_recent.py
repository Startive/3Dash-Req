import requests

url = "http://delugedrop.com/3Dash/get_recent.php" #url of where to send the request

payload = ""
response = requests.request("GET", url, data=payload)

print(response.text)