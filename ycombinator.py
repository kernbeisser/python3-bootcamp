# imports as needed
import requests

def some_func():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    return response.status_code

def main():
    res = some_func()
    print(f"{res}")

if __name__ == '__main__':
    main()
