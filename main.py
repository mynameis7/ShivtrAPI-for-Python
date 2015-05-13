import shivtr
import shivtr.login_info as li


shivtr.set_site("www.logunners.shivtr.com")
shivtr.authenticate.login(li.email, li.password)
shivtr.authenticate.logout()
#help(shivtr.members)
