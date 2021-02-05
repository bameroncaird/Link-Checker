from response_code_lookup import get_code_info
from selenium import webdriver
import requests

DRIVER = webdriver.Chrome("/Users/bameroncaird/Developer/Chrome_Driver/chromedriver")
RESOURCE_LINK = "https://mizzoucareertools.campuscareerinnovations.com/resources/page/"

class Resource:
    title = None
    link = None
    code = None
    page = None
    long_description = False
    TIMEOUT = 5
    def __init__(self, title, link, page):
        self.title = title
        self.link = link
        self.page = page
        if self.link is not None and self.link != "":
            try:
                response = requests.get(self.link, timeout=self.TIMEOUT)
                self.link = response.url
                self.code = response.status_code
                # Check if two-click resource...
            except:
                pass

# The last page of resources fluctuates between page 69 and page 70.
# This function dynamically finds the last page so that we don't have to worry about it.
def find_last_page():
    DRIVER.get(RESOURCE_LINK + "1")
    page_numbers = []
    for element in DRIVER.find_elements_by_class_name('page-numbers'):
        try:
            page_numbers.append(int(element.get_attribute('innerHTML')))
        except:
            pass
    return max(page_numbers)

FIRST_PAGE = 1
LAST_PAGE = find_last_page()

def check_resources():
    current_page = FIRST_PAGE
    while current_page <= LAST_PAGE:
        DRIVER.get(RESOURCE_LINK + str(current_page))
        current_page += 1
