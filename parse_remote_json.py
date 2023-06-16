import urllib.request, json

# Used to get APIs from urls

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data)
    print(type(data))
