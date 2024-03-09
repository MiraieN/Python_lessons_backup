from selenium import webdriver

driver = webdriver.Firefox()  # You can use other drivers like Firefox, etc.

url = "https://www.marvel.com/characters"
driver.get(url)

page_source = driver.page_source

driver.quit()