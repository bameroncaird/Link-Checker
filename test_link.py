import requests
from response_code_lookup import get_code_info

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
HEADERS = {
    'User-Agent' : USER_AGENT
}

def test_link(link):
    code = -1
    try:
        # http_response = requests.get(link, timeout=5)
        http_response = requests.get(link, timeout=10, headers=HEADERS)
        code = http_response.status_code
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        pass
    except requests.TooManyRedirects:
        pass
    except requests.exceptions.RequestException:
        pass
    except Exception:
        pass
    return get_code_info(code)