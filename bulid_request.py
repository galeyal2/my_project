import requests

from utils.my_logger import eyal_logger

url = "http://localhost:9000/user"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
eyal_logger.info("dssfdfs")
if __name__ == "__main__":
    data = {'user': 'eyal6', "email": "eyalgal@gmail.com", "password": "sdfsdf"}
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)
    print(requests.get(url=url, headers=headers).text)
