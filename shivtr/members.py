import requests
from common import format_url, VARS, STRINGS


def members(status, page=None):
    """
    Query the site for members based on status and page

    Keyword arguments:
    status      -- String of the status, ("active","inactive","deleted")
    page        -- Page number to query, leave blank to get all the pages.
                   (default is None)

    Returns:
    A list of dictionaries of member information
    """
    site = VARS.SITE
    auth = VARS.TOK
    def get_members():
        url = format_url(site) + "members.json"
        print url
        r = requests.get(url, params=params)
        return r.json()
    params = {}
    if auth:
        params[STRINGS.AUTH] = auth
    if status == "inactive":
        params[STRINGS.STAT] = "inactive"
    if status == "deleted":
        params[STRINGS.STAT] = "deleted"

    if page==None:
        data = {"members":[]}
        i = 1
        while True:
            params[STRINGS.PAGE] = i
            mems = get_members()
            if len(mems["members"]) > 0:
                data["members"].extend(mems["members"])
                data["ranks"] = mems["ranks"]
            else:
                break
            i += 1
        return data
    elif page:
        params[STRINGS.PAGE] = page
        return get_members()
    else:
        return get_members()


def members_id(mem_id):
    """
    Query a specific member based on their ID

    Keyword arguments:
    mem_id      -- Id number
    """
    site = VARS.SITE
    auth = VARS.TOK
    url = format_url(site) + "members/%s"%mem_id + ".json"
    params = {}
    if auth:
        params["auth_token"] = auth
    r = requests.get(url, params=params)
    return r.json()
    
