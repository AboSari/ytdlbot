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