import pyshorteners

url = input("Enter a URL: ")

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print(f"The shortened URL is: {short_url}")