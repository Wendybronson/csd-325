import requests

print("Requests installed successfully!")
print("Version:", requests.__version__)

import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())