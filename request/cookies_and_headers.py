import requests

# we can view the servers headers usinfg python dixtionary and similarly we can access the cookies in the servers as well

# to send our own cookies we can use the cookies parameter and cookies are returned inside a request cookie jar which acts like a dictionary but also offers a more complete interface suitable for over multuiple domain and paths

response=requests.get("https://httpbin.org/cookies")
# print(response.cookies)

cookies=dict(key1="value1")
response=requests.get("https://httpbin.org/cookies",cookies=cookies)
# print(response.text)

#headers
response=requests.get("https://httpbin.org/headars")
print(response.headers)