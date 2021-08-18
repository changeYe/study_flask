import requests


class Http:

    @staticmethod
    def get(url, is_return_json=True):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json() if is_return_json else response.text
        else:
            return {} if is_return_json else ''
