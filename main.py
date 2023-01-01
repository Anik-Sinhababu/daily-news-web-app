import requests
api_key = "5628c780313a460f8a1aa361871463da"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=in&apiKey=5628c780313a460f8a1aa361871463da"
#Make request
req = requests.get(url)
#Get a ditionary with data
content = req.json()
#Access ata with their titles
print(content["articles"])
for article in content["articles"]:
      print(article["title"])

