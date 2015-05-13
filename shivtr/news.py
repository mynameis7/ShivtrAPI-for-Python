import requests
from common import format_url, VARS, STRINGS


def news():
    """
    Return a list of news entries for the site
    """
    site = VARS.SITE
    auth = VARS.TOK
    url = format_url(site) + "news_entries.json"
    params = {}
    if auth:
        params[STRINGS.AUTH] = auth
    r = requests.get(url, params=params)
    return r.json()


def news_entry(news_id):
    """
    Return a specific news entry from an id

    Keyword arguments:
    news_id     -- id of the news entry
    """
    site = VARS.SITE
    auth = VARS.TOK
    url = format_url(site) + "news_entries/"
    url += str(news_id)
    url += ".json"
    params = {}
    if auth:
        params[STRINGS.AUTH] = auth
    r = requests.get(url, params=params)
    return r.json()
