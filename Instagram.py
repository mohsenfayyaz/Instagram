import pdb
import pickle
from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/danialves/')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('https://www.instagram.com/leomessi/following/')
dom = driver.find_element_by_xpath('//*')

following_button = driver.find_element_by_partial_link_text("following")
following_button.click()



# pdb.set_trace()
# username = dom.find_element_by_name('username')
# password = dom.find_element_by_name('password')
# login_button = dom.find_element_by_xpath('//*[@class="_qv64e _gexxb _4tgw8 _njrw0"]')
#
# username.clear()
# password.clear()
# username.send_keys('your username')
# password.send_keys('your password')
#
# login_button.click()
# driver.get('https://www.instagram.com/accounts/login')
#
# if 'logged-in' in driver.page_source:
#     print('Logged in')

# from selenium.webdriver.common.keys import Keys
# html = driver.find_element_by_tag_name('html')
# html.send_keys(Keys.END)




pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))