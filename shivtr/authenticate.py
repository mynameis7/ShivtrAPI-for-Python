import requests
from common import format_url, VARS, STRINGS


def login(email, password):
    """
    Login into the website

    Keyword arguments:
    email       -- Email you login with
    password    -- Password you login with
    """
    site = VARS.SITE
    url = format_url(site) + "users/sign_in.json"
    data = '{"user": {"email":"%s", "password":"%s"}}'%(email, password)
    headers = {'content-type': 'application/json'}
    r = requests.post(url, headers=headers, data=data)
    VARS.TOK = r.json()["user_session"]["authentication_token"]


def logout():
    """
    Logs you out of the site
    """
    site = VARS.SITE
    auth = VARS.TOK
    if not auth:
        raise Exception("Not logged in")
    url = format_url(site) + "users/sign_out.json"
    params = {STRINGS.AUTH: auth}
    r = requests.delete(url, params=params)
    VARS.TOK = None
