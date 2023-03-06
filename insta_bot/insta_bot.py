from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import username, password, hashtag
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def login(username, password):
    browser = webdriver.Chrome()

    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(2, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        # try:
        #     browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        #     time.sleep(5)
        #
        #     for i in range(1, 2):
        #         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #         time.sleep(random.randrange(3, 5))
        #
        #     hrefs = browser.find_elements(By.TAG_NAME, 'a')
        #     posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
        #     print(posts_urls)
        #     for url in posts_urls:
        #         try:
        #             browser.get(url)
        #             time.sleep(random.randrange(2, 5))
        #             like_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/div[1]/span[1]/button")
        #             like_button.click()
        #             time.sleep(3)
        #             like_button = browser.find_element(By.XPATH,
        #                                                "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[1]/header/div[2]/div[1]/div[2]/button")
        #             like_button.click()
        #
        #             time.sleep(random.randrange(80, 100))
        try:
            browser.get("https://www.instagram.com/eliza_barna/")
            time.sleep(5)

            for i in range(1, 8):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(6, 8))
                print(i)
                print(i)
            hrefs = browser.find_elements(By.TAG_NAME, 'a')
            print(hrefs)
            print(len(hrefs))
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
            print(posts_urls)
            print(len(posts_urls))
            for url in posts_urls:
                try:
                    browser.get(url)
                    time.sleep(random.randrange(2, 5))
                    like_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/div[1]/span[1]/button")
                    like_button.click()
                    time.sleep(3)
                    like_button = browser.find_element(By.XPATH,
                                                       "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[1]/header/div[2]/div[1]/div[2]/button")
                    like_button.click()
                    time.sleep(2)
                    clic = browser.execute_script("document.getElementsByClassName('_a9-- _a9_1')[0].click()")

                    time.sleep(random.randrange(80, 100))
                except Exception as ex:
                    print(ex)

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


login(username, password)
