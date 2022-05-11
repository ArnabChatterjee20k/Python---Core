import requests
from requests import api

api_key="e5afe013bc40736aae55895b7018363d"

res=requests.post("http://developer.marvel.com//v1//public//characters",data={"apikey":api_key,"limit":10})

# print(res.status_code)

print(res.headers)