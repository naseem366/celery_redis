
###############   tab = move forward,shift+tab = move back 


# def lengthOfLongestSubstrings(s):
#     longest = 0
#     for i in range(len(s)):
#         seen = ""
#         for j in range(i,len(s)):
#             if s[j] in seen:
#                 break
#             seen += s[j]
#             if len(seen) > longest:
#                 longest = len(seen)
#     return longest

# s = "adadflda"
# print(lengthOfLongestSubstrings(s))


# lst = [1,2,3,2,4,4,2,3,3,3,4,4,4]
# d = dict()
# max_count = 0
# most_frequent = None
# for ch in lst:
#     d[ch] = d.get(ch,0)+1
# print(d)
# for key in d:
#     if d[key] > max_count:
#         max_count = d[key]
#         most_frequent = key
# print(most_frequent)


###### url_shortener ############

from fastapi import FastAPI,HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel,HttpUrl
import random
import string

 
app = FastAPI()

url_store = {}
long_url_to_key = {}

class URLRequest(BaseModel):
    long_url : HttpUrl

def generate_key():
    characters = string.ascii_letters + string.digits
    while True:
        key = "".join(random.choices(characters,k=5))
        if key not in url_store:
            return key


@app.post("/",status_code=201)
def create_short_url(request:URLRequest):
    long_url = str(request.long_url)
    if long_url in long_url_to_key:
        key = long_url_to_key[long_url]
        return {"short_url":f"https://company.com/{key}"}
    
    key = generate_key()
    url_store[key] = {"long_url":long_url,"visits":0}

    long_url_to_key[long_url] = key
    return {"short_url":f"https://company.com/{key}"}


@app.get("/{key}")
def get_short_url(key: str):
    if key not in url_store:
        raise HTTPException(status_code=404,detail="Short URL not found")
    #url_store = url_store[key]
    url_store[key]["visits"] +=1
    return RedirectResponse(url = url_store[key]["long_url"],status_code=307)    


@app.get("/info/{key}")
def get_url_info(key: str):
    if key not in url_store:
        return {"visits":0}
    return {"visits":url_store[key]["visits"]}
