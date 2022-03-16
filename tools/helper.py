from urllib.parse import urlparse
import re


def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False


def extract_url(text):
    search = re.search("(?P<url>https?://[^\s]+)", text)
    return search.group("url") if search else None


def get_hostname(url):
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri)
