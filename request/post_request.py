import requests
# post request are used to submit the data to the server
payload={"key1":"value1"}
response=requests.post("https://httpbin.org/post",data=payload)

print(response.text)