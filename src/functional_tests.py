from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.python.org/')

assert 'Welcome to Python.org' in browser.title