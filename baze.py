from selenium import webdriver
from selenium.webdrive.chrome.service import Service
from selenium.driver.common.by import By
import time

browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
page to scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")

page_to_scrape.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(5)

page_to_scrape.find_element(By.LINK_TEXT, " OpenID Connect ").click()
time.sleep(5)

email = page_to_scrape.find_element(By.ID, "i0116")
email.send_keys('ELFAK_EMAIL')
page_to_scrape.find_element(By.CSS_SELECTOR, "input.button_primary").click()
time.sleep(5)

password = page_to_scrape.find_element(By.ID, "i0118")
password.send_keys('ELFAK_PASSWORD')
page_to_scrape.find_element(By.CSS_SELECTOR, "input.button_primary").click()
time.sleep(5)

page_to_scrape.find_element(By.CSS_SELECTOR, "input.button_primary").click()
time.sleep(15)
