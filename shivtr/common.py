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
    """
    Global Level Variables for use with the Shivtr API
    """
    SITE = ""
    TOK = None

class STRINGS:
    """
    Strings for use with the API
    """
    AUTH = "auth_token"
    STAT = "status"
    PAGE = "page"
    
