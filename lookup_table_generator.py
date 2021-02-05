from selenium import webdriver

BASE_INFO_URL = "https://httpstatuses.com/"
CODE_LIST = [
    100,101,102,
    200,201,202,203,204,205,206,207,208,226,
    300,301,302,303,304,305,307,308,
    400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,
    421,422,423,424,426,428,429,431,444,451,499,
    500,501,502,503,504,505,506,507,508,510,511,599
]
DRIVER = webdriver.Chrome("/Users/bameroncaird/Developer/Chrome_Driver/chromedriver")
TITLE_XPATH = "(//article/child::h1)[1]"

def build_url(status_code):
    return BASE_INFO_URL + str(status_code)

def parse_title(raw_title):
    return raw_title[17:]

def build_lookup_table():
    lookup_table = {}
    for code in CODE_LIST:
        info_url = build_url(code)
        try:
            DRIVER.get(info_url)
            title = parse_title(DRIVER.find_element_by_xpath(TITLE_XPATH).get_attribute('innerHTML'))
            lookup_table[code] = (title, info_url)
        except:
            print("Error: " + str(code))
            lookup_table[code] = (None, info_url)
    DRIVER.quit()
    return lookup_table

# Uncommenting out line 38 will print the full lookup table to the console.
# Just cut and paste the line into a variable in another file.
# print(build_lookup_table())

