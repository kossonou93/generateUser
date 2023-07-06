from pprint import pprint

import requests

def api_user():
    r = requests.get(f"https://randomuser.me/api/")
    if not r and r.json():
        return False

    data = r.json().get("results")
    #pprint(data)
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print('PyCharm')

    api_user()