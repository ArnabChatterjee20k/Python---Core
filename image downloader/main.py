import requests 
link="https://i.ytimg.com/vi/YTHdEDS9-Rk/maxresdefault.jpg"
req=requests.get(link)
# print(req.status_code)
# img=bytes(req.content,"utf8")
print("started execution")
img=req.content
with open("img.jpg","wb") as f:
    f.write(img) 
print("done")    