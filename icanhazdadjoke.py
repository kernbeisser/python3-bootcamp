# imports as needed
import requests

def some_func():
    url = "https://icanhazdadjoke.com"
    response = requests.get(url, headers={"Accept" : "text/plain"})
    return response.text

def main():
    res = some_func()
    print(f"{res}")

if __name__ == '__main__':
    main()
