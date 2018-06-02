from selenium import webdriver

brower = webdriver.Chrome()
brower.get('http://localhost:8000')

assert 'Django' in brower.title