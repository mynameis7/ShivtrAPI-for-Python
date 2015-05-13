"""
Shivtr API implementation for python 2.7
"""
__all__ = ["authenticate","common","members","news", "set_site"]

import authenticate
import common
import members
import news
import forums

def set_site(site):
    """
    Set the site for the shivtr app
    """
    common.VARS.SITE = site
