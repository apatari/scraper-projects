from bs4 import BeautifulSoup
import requests

url = "https://www.backcountry.com/b/edelrid-boa-standard-climbing-rope-9.8mm?CMP_SKU=ELR002Y&MER=0406&skid=ELR002Y-BL-S40M&mr:device=c&mr:adType=plaonline&utm_source=google&utm_medium=pla&utm_campaign=20567682234__p:G%7Cs:BC%7Cct:Shopping%7Cct2:pmax%7Cg:xx%7Cc1:Climb%7Cc2:xx%7Cb:xx%7Cmt:xx____&utm_term=__ELR002Y-BL-S40M&utm_content=__pla&utm_id=go_cmp-20567682234_adg-_ad-__dev-c_ext-_prd-ELR002Y-BL-S40M_mca-7811_sig-CjwKCAjwzN-vBhAkEiwAYiO7oOB0sHISrWgaK0OJakK-bHcOZgncN7Ng-0StOdGKMghbW11OdSR5IBoCjwcQAvD_BwE&gad_source=1&gclid=CjwKCAjwzN-vBhAkEiwAYiO7oOB0sHISrWgaK0OJakK-bHcOZgncN7Ng-0StOdGKMghbW11OdSR5IBoCjwcQAvD_BwE&gclsrc=aw.ds"

result = requests.get(url)

print(result.text)