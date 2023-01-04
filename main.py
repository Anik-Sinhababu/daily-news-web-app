import requests
from send_mail import send_email
api_key = "5628c780313a460f8a1aa361871463da"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=in&apiKey=5628c780313a460f8a1aa361871463da"
# Make request
req = requests.get(url)
# Get a dictionary with data
content = req.json()
# Access ata with their titles
message = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        message = message + article["title"] + "\n" + \
                  article["description"] + "\n" + article["url"] + "\n\n"


message = message.encode("utf-8")
send_email(message)
