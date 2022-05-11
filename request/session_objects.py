import requests
#the seesion object  peresists certain parameters over multiple requests

#it persists cookies across all requests made from the session instance

# it use urllib3 connection pooling and if I am making the sveral requests to the same host the underlying TCP connection will be reused which can result in a  significant performance increase.

#A session object has all the methods of the main requests API

s=requests.session()
s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")

r=s.get("https://httpbin.org/cookies")#response object

print(r.text)