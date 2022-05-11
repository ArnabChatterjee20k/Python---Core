import requests
response=requests.get("https://httpbin.org/get")#response object
# print(response.status_code)#if status code is 200 then we are good to go
# print(response.cookies)
# print(response.headers)#headers inside a url
print(response.json())#getting the content in format of json
