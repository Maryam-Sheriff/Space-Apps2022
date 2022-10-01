from instabot import Bot
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('C:/Users/clinic/PycharmProjects/instagram_uploader/geckodriver.exe')
#browser = webdriver.Firefox()

#Facebook
#browser.get('http://www.facebook.com')
#assert 'Facebook' in browser.title

  #Instagram

# here I will ask him to enter his account data in a pop-up window to get his info to use
# in the bot login
#browser.get('http://www.instagram.com')
#assert 'Instagram' in browser.title

bot = Bot()
bot.login(username="demo.773",  # the username from the text box -- Demo app i made --> demo.773
          password="demoapphaha")  # the password from the text box -- pass --> demoapphaha
bot.upload_photo("Mylove.jpeg",
                 caption="Test")

#LinkedIn
#browser.get('http://www.LinkedIn.com')
#assert 'LinkedIn' in browser.title


#twitter
#browser.get('http://www.twitter.com/')
#assert 'Twitter' in browser.title
