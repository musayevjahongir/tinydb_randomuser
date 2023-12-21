import requests


def get_users_by_gender(gender: str, n: int) -> list[dict]:
    url = 'https://randomuser.me/api/'
    payload = {
        'gender': gender,
        'results': n
    }

    resp = requests.get(url, params=payload)

    users = []
    if resp.status_code == 200:
        for user in resp.json()['results']:
            users.append({
                "first_name": user['name']['first'],
                "last_name": user['name']['last'],
                "country": user['location']['country'],
                "age": user['dob']['age'],
                "nat": user['nat'],
            })
        return users
    return []