from config import base_URL, headers
from requests import get, post

# Runs a get on any endpoint
def endpoint_get(endpoint: str) -> dict:
    return get(
        base_URL + endpoint,
        headers=headers,
    ).json()

# # Accepts an endpoint (format /xxx/xxx) and a dictionary as a json payload
def endpoint_post(endpoint: str, payload: dict) -> dict:
    post_response = post(base_URL + endpoint, headers=headers, json=payload)
    return post_response.json()

# Check response
if __name__ == "__main__":
    res = ()
    if res.status_code != 200:
        print(f"---Error {res.status_code}--- \n\n {res.text}")
    else:
        print("success")
        print(res.json())