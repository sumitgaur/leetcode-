import requests


def fetch_data(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        data = response.json()
        return data
    except requests.exceptions.Timeout:
        raise RuntimeError("Request timeout")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f'http error {e}')
    except ValueError:
        raise RuntimeError('Invalid json response')
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Request failed {e}')

url = 'https://www/'
data = fetch_data(url)
