import requests
res=requests.get("http://randomfox.ca/floof")
# print(res.status_code)
# print(res.text)
# print(res.json())#printing in dictionary format

fox=res.json()
print(fox["image"])