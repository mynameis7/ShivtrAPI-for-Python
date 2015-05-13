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


if __name__ == "__main__":
    import members
    def admin_login():
        import login_info as li
        return login(li.email, li.password)
    site = "http://www.logunners.shivtr.com/"
    VARS.SITE = site
    admin_login()
    inactive = members.members("inactive","all")
    active = members.members("active","all")
    deleted = members.members("deleted","all")
    logout()
