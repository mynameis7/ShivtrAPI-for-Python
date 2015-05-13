import requests
from common import format_url, VARS, STRINGS


def forums(forum_id=None):
    """
    Gets a list of all the forum sections
    If forum_id is specified, then get the forum threads in the forum

    Keyword arguments:
    forum_id    -- Id of the forum
    """
    url = format_url(VARS.SITE)
    url += "/forums"
    if forum_id:
        url += "/%s"%forum_id
    url += ".json"
    auth = VARS.TOK
    params = {}
    if auth:
        params[STRINGS.AUTH] = auth
    r = requests.get(url, params=params)
    return r.json()


def forum_threads(thread_id):
    """
    Get the thread with the given ID

    Keyword arguments:
    thread_id   -- Id of the forum thread
    """
    url = format_url(VARS.SITE)
    url += "/forum_threads"
    url += "/%s.json"%thread_id
    auth = VARS.TOK
    params = {}
    if auth:
        params[STRINGS.AUTH] = auth
    r = requests.get(url, params=params)
    return r.json()
