import multiprocessing
from multiprocessing import Process, Manager
import requests
import random
import pandas as pd

# 1. Create a basic set of functions:
#   1. Normal Function call
#   2. API call
#   3. Mass data iteration

# 2. Add multiprocessing using the previous transferring_data_between_processes.py

# 3. Use manager to return the values back to the same program

# 4. Proces which sends multiple arguments, long program times

from multiprocessing import Process, Manager

url = "https://icanhazdadjoke.com/search"
data = pd.read_excel(r'C:\Users\jack_\PycharmProjects\Module5\5-6-8-Activity_2_Try_Multiprocessing\Data_set.xlsx')


def NormalFunction(x, y):
    z = x + y
    print(z)
    return z


def get_joke():
    # Gets user input for the term to search using GET request
    search_term = "yes"

    # Get request with JSON header and parameter term to search from users input
    response = requests.get(
        url,
        headers={
            "Accept": "application/json"
        },
        params={
            "term": search_term
        }
    )

    # converts the JSON file to a python dict
    data = response.json()

    # Uses the key total_jokes from dict to get a value
    total = data["total_jokes"]

    # Based on if a joke on the search term was found and how many, will return the joke from the
    # request. Data is a dictionary, results is a key that returns a list value that holds dictionaries.
    if total == 1:
        print(f"I have got one joke about {search_term}.")
        print(data["results"][0]["joke"])

    # Selects a random joke from total ammount of jokes found if there is more than one
    elif total > 1:
        print(f"I have found {total} jokes about {search_term}.")
        rand_num = random.randint(0, total - 1)
        print(data["results"][rand_num]["joke"])

    # No joke found
    else:
        print(f"I'm sorry. I could not find any jokes on {search_term}.")


def PrintData():
    df = pd.DataFrame(data, columns=['product_name'])
    print(df)


if __name__ == '__main__':
    processes = [multiprocessing.Process(target=NormalFunction, args=(6, 1)),
                 multiprocessing.Process(target=get_joke), multiprocessing.Process(target=PrintData)]
    for p in processes:
        p.start()
        p.join()
        print(p.name)
