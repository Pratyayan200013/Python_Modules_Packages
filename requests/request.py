import requests
# r = requests.get("https://xkcd.com/353/")
# print(r) # r is the response object
'''HTTP status codes --> 200 = success,300 = redirects,400 = client error,500 = server error'''
# print(dir(r)) # gives us all the methods and attributes associated with the object
# print(help(r)) # gives us indepth information about all the methods and attributes associated with the object
# print(r.text)
# print(r.encoding)

# r = requests.get("https://imgs.xkcd.com/comics/python.png")  # Url for image
# print(r.content)
'''with open("python_image.jpg", "wb") as f:
    f.write(r.content)'''

# HTTP GET request
# payload = {"key": "value"}
# In case of GET request it is params
# r = requests.get("https://httpbin.org/", params=payload)
# The URL has been correctly encoded to 'https://httpbin.org/?key=value.. To see the url we use print(r.url)
'''payload = {"key1": "value1", "key2": "value2"}
payload1 = {"key1": "value1", "key2": ["value2", "value3"]}
payload2 = [("key1", "value1"), ("key2", "value2"), ("key2", "value3")]
r1 = requests.get("https://httpbin.org", params=payload)
# The URL has been correctly encoded to 'https://httpbin.org/?key1=value1&key2=value2
print(r1.url)
# In case of GET request it is params
r2 = requests.get("https://httpbin.org", params=payload1)
# The URL has been correctly encoded to 'https://httpbin.org/?key1=value1&key2=value2&key3=value3
print(r2.url)
r3 = requests.get("https://httpbin.org", params=payload2)
# Here the URL has also been correctly encoded to 'https://httpbin.org/?key1=valu1&ke2=value2&key2=value3
print(r3.url)
print(r2.url == r3.url)'''

# HTTP POST request
'''payload = {"username": "Pratyayan Sarkar", "password": "Pratyayan2000/04/13"}
# In case of POST request it is data
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)'''

# Other HTTP requests are PUT,DELETE,HEAD,OPTIONS
# payload = {"key": "value"}
# In case of PUT request it is also data
# r = requests.put("https://httpbin.org/put", data=payload)
# print(r.text)
'''r = requests.delete("https://httpbin.org/delete", data={"key": "value"})
# The DELETE method sends a delete request to the url
print(r.text)
print(r)'''
'''r = requests.options("https://httpbin.org/get")
r1 = requests.head("https://httpbin.org/get")
# print(r) # r is the response object and print(r) gives the HTTP status code
# print(r1) # r1 is the response object and print(r1) gives the HTTP status code
# The HTTP HEAD request makes a similar type of request to the wbsite like the GET request to get a response from the website.. But it only gets the response head to get the information in the meta tag  instead of getting the whole response body..'''

'''r = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# print(r.text)
py_dict = r.json()
# When we are getting a JSON response from a website we should use r.json() instead of r.text
print(py_dict['abilities'])
# r.json() --> It converts the JSON response from the website into a Python dictionary.. We can store the JSON response from the website into a variable using r.json() and then it can be used as a Python dictionary..
print(r.status_code)
# r.status_code gives us the HTTP status code for the response object
print(r.ok)
# r.ok is True for any status code less than 400'''

# Creating Basic Authentication Route
'''payload = {"username": "Pratyayan", "password": "testing"}
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
r = requests.get(
    "https://httpbin.org/basic-auth/Pratyayan/testing", auth=('Pratyayan', 'testing'))
print(r.text)'''
# Note --> In case of HTTP GET request it is params and in case of HTTP POST request it is data and in case of HTTP PUT request it is also data

# Another example of creating basic authentication route
'''r = requests.post("https://httpbin.org/post",
                  data={"username": "Adrija", "password": "some_tests"})
print(r.text)'''
'''r = requests.get("https://httpbin.org/basic-auth/Adrija/some_tests",
                 auth=('Adrija', 'some_tests'))
print(r)
print(r.text)
r1 = requests.get("https://httpbin.org/basic-auth/Pratyayan/testing",
                  auth=('Pratyayan', 'testing'))
print(r1.status_code)
print(r1.ok)
print(r1.text)'''

# Timeout session for a website to response
'''r = requests.get("https://httpbin.org/delay/1", timeout=3)
# A timeout session of 3 seconds is set and the url is set to delay by 1 second i.e the website will give a response after 1 second
print(r)
print(r.status_code)
print(r.ok)'''
# As the website gives a response before the timeout session so we get HTTP status code 200 which means success..
# If the delay is more than the timeout session then it will throw an error..

#r = requests.get("https://api.github.com/events")
# print(r.headers)
# r.headers gives an indepth information about the response from the website we requested

'''r = requests.get("https://api.github.com/events")
print(r.encoding)
# r.encoding gives the encoding of the response we get from the website..
# HTML and XML have the ability to specify their encoding in their body..
# The encoding of the response we get from the website is used when we access r.text. The encoding can be changed using r.encoding='ISO-8859-1'. Now whenever we access r.text the new encoding will be used..
# r.content gives the response in bytes. r.content is used to find the encoding of the response then we can use r.rencoding to set the encoding of the response so that we can r.text with correct encoding..
# So r.content is used to get the binary data of an image
print(r.content)
r.encoding = 'utf-8'
print(r.text.encode('utf-8'))'''

# Raw Response Content
r = requests.get("https://httpbin.org", stream=True)
# To get the raw response content from the website we use r.raw. To do these we should set  stream=True..
'''print(r.raw)
print(r.raw.read(10))
print(r.raw.read())'''
with open("api_github.txt", 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        f.write(chunk)
'''----------------------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------------------------------------------------------'''
