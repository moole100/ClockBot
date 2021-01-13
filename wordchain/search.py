import sys
from selenium import webdriver

options = None
driver = None

if(sys.platform == "linux"):
    options = webdriver.firefox.options.Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(executable_path='./geckodriver', options=options)
elif(sys.platform == "win32"):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome("chromedriver.exe", options=options)
else:
    print("I don't know what {} is, exiting".format(sys.platform))
    exit()

driver.get("https://ko.dict.naver.com/#/search?query=단어")

def find_naver(voca):
    url = "https://ko.dict.naver.com/#/search?query={}".format(voca)
    driver.get(url)
    driver.implicitly_wait(1)
    xpath2 = '//div[@class="component_keyword has-saving-function"]'
    xpath3 = '//strong[@class="highlight"]'
    try:
        temp_voca = driver.find_element_by_xpath(xpath2+xpath3).text
        if voca == temp_voca:
            return True
        else:
            return False
    except Exception:
        return False

while True:
    voca = input("Search: ")
    print("Searching up {}".format(voca))
    if(find_naver(voca)):
        print("존재하는 단어")
    else:
        print("그게 뭔데 씹덕아")
