import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
service = Service("C:\\Users\\shashank\\PycharmProjects\\python-automation\\chromedriver.exe")
def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-featues=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def getLogin():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-featues=AutomationControlled")

    driver1 = webdriver.Chrome(service=service, options=options)
    driver1.get("http://automated.pythonanywhere.com/login/")
    return driver1

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
    driver = getDriver()
    time.sleep(2)
    element1 = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[1]')
    print(element1.text)
    element2 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    print(clean_text(element2.text))
    time.sleep(2)
    driver1 = getLogin()
    driver1.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver1.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    print(driver1.current_url)
    time.sleep(2)
    driver1.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver1.current_url)

main()
