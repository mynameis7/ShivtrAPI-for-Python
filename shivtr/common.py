def format_url(site):
    """
    Format a site url so that it has the required elements

    Keyword arguments:
    site        -- Unformatted url
    """
    url = site
    if not url.startswith("http://"):
        url = "http://" + url
    if not url.endswith("/"):
        url += "/"
    return url

class VARS:
    SITE = ""
    TOK = None

class STRINGS:
    AUTH = "auth_token"
    STAT = "status"
    PAGE = "page"
    
