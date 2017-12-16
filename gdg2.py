from selenium import webdriver
def login():
    username=input("Enter your username")
    password1=input("Enter your password")
    browser=webdriver.Chrome(r"C:\Users\Archie\Downloads\chromedriver_win32\chromedriver.exe")
    browser.get('http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://phc.prontonetworks.com/')
    user=browser.find_element_by_css_selector('body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(3) > td > table:nth-child(1) > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(8) > td:nth-child(2) > input')
    user.send_keys(username)
    password=browser.find_element_by_css_selector('body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(3) > td > table:nth-child(1) > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(10) > td:nth-child(2) > input.textBox')
    password.send_keys(password1)
    login=browser.find_element_by_css_selector('body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(3) > td > table:nth-child(1) > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(13) > td:nth-child(2) > input')
    login.click()

login()