import requests
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/The_Blue_Marble_%28remastered%29.jpg/640px-The_Blue_Marble_%28remastered%29.jpg"
response = requests.get(url)
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()