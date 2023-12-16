import requests


def check_number_format(number: int) -> str:
    """
    Function to check number format
    >>> check_number_format(-2)
    'Negative'
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negativeeeee"
    return "Zero"


## TDD
# 1. Write a test for a feature
# 2. Write code to make the test pass
# 3. Refactor the code as needed

## full name country -
# - Request API
# - name 'wathan' (given)

## How to solve
# - country_code api request -> 'MM' [Done]
# - use 'MM' , request another full country api request -> 'Myanmar'


def short_code(name):
    get_json = requests.get(f"https://api.nationalize.io?name={name}").json()
    return get_json["country"][0]["country_id"]


def full_name(short_name):
    country_data = requests.get("https://api.first.org/data/v1/countries").json()
    if short_name in country_data["data"]:
        return country_data["data"][short_name]["country"]


## Simple Calculator - Add function, Substract , Divide , Multiply
## We'll use TDD method to write


## To test main_func()
def test_full_name():
    short = short_code("paing")
    assert short == "MM"

    full = full_name(short)
    assert full == "Myanmar"


def guess_country():
    inp = input("Enter Your name: ").split()
    link_name = requests.get("https://api.nationalize.io?name=" + inp[0]).json()
    name = link_name["country"][0]["country_id"]
    print(f"U might come from : {name}")
    req = requests.get("https://api.first.org/data/v1/countries").json()
    if name in req["data"]:
        print(req["data"][name]["country"])
    else:
        pass
    return inp
