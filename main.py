from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os



PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\Documents\Projects\chromedriver.exe"
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down_speed = 0
        self.up_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        go_button = self.driver.find_element_by_css_selector("div.start-button a")
        go_button.click()
        time.sleep(50)

        #     close AD
        try:
            cross_button = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
            time.sleep(2)
            cross_button.click()
        except NoSuchElementException:
            pass

        down_speed_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
            'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down_speed = down_speed_button.text
        up_speed_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
            'div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up_speed = up_speed_button.text

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(5)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login_button.click()
        time.sleep(5)
        username_section = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username_section.click()
        time.sleep(2)
        username_section.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        password_section = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password_section.click()
        password_section.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login_button.click()
        time.sleep(2)
        tweet = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.'
                                                         'r-13qz1uu.'
                                                         'r-417010 > main > div > div > div > div > div > div.css-'
                                                         '1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.'
                                                         'r-oyd9sg > div:nth-child(1) > div > div > div > div.css-'
                                                         '1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.'
                                                         'r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > '
                                                         'div > div > div > div > div > div > div > div > label > '
                                                         'div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div'
                                                         ' > div.DraftEditor-editorContainer > div > div > div > div')
        tweet.click()
        message = (f"Hey Internet provider, Why is my internet speed {self.down_speed} down and {self.up_speed} "
                   f"up when I pay for {PROMISED_DOWN} and {PROMISED_UP}.")
        for word in message.split():
            tweet.send_keys(f"{word} ")
            time.sleep(0.2)
        time.sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div'
                                                         '/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/'
                                                         'div/div/div[2]/div[3]/div/span/span')
        time.sleep(2)
        tweet_button.click()
        print("Tweet Sent")
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
bot.tweet_at_provider()
