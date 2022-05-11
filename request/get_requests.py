import requests

#get request is used to request data  from the srever 

response=requests.get("https://httpbin.org/get")#response object
print(response.text) 

payload={"key1":"value1"} 
response=requests.get("https://httpbin.org/get",params=payload)#passsing parameters  inside url
print(response.url)