# imports as needed
import requests

def get_jokes(search_term):
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(url, 
                            headers={"Accept" : "application/json"},
                            params={'term' : search_term})
    return response.json()

def main():
    search_term = input("Now, what are we looking at? ")

    data = get_jokes(search_term)

    num_of_jokes = data['total_jokes']

    if num_of_jokes > 0:
        print(f"i've found {num_of_jokes} jokes about cats: ")
        for i in range(num_of_jokes):
            print(f"{data['results'][i]['joke']}")
    if num_of_jokes == 1:
        print(f"i've found {num_of_jokes} joke about cats: ")
        print(f"{data['joke']}")
    else:
        print(f"This is what yout get with an inappropriate search... {num_of_jokes}")

if __name__ == '__main__':
    main()
