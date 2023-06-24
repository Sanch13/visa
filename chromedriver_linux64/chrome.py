from selenium import webdriver
import time
from fake_useragent import UserAgent


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome(options=options)

# url = "https://visa.vfsglobal.com/blr/ru/pol/login"
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"


driver.get(url=url)

time.sleep(5)

driver.close()
