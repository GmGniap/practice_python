import requests


def check_number(number: int):
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    else:
        return "Negative"


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


def get_short_country_code(name: str) -> str:
    get_json = requests.get(f"https://api.nationalize.io?name={name}").json()
    return get_json["country"][0]["country_id"]


def get_full_country_name(short_code: str) -> str:
    get_all_data = requests.get("https://api.first.org/data/v1/countries").json()
    if short_code in get_all_data["data"]:
        return get_all_data["data"][short_code]["country"]


def guess_age(inp):
    link_age = requests.get("https://api.agify.io?name=" + inp[0]).json()
    age = link_age["age"]
    print(f"U look like: {age}")


def guess_gender(inp):
    link_gender = requests.get("https://api.genderize.io/?name=luc" + inp[0]).json()
    gender = link_gender["gender"]
    print(f"Gender: {gender}")
