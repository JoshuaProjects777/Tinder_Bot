

##HI WELCOME TO THE TINDER BOT THE REQUIREMENTS FOR THIS BOT ARE LISTED BELOW:
## 1.undected chromedriverv2.
## 2.a google account with two setp verification swicthed off
## 3.selenium


##Please note this is not a fully operated bot there is only one element missing which is
#when tinder wishes to gain permision the bot clicks on the allow button then it swifts to the broswer to allow permission
#this allow button presented by the broser and not by tinder has to be clicked manuelly
#so this one button is the only button to be clicked manuelly the enable notification button after that is automated so dont
#click on anything.


   ##PLEASE INPUT YOUR EMAIL AND PASSOWRD BELOW WITHIN THE "  ".

   ##EXAMPLE email="wdnfoiwnd@gmail.com"
   ##        password="duhwo"

email = "input your email here"
password = "input your password here"

##PLEASE MAKE SURE NOT TO DELETE THE " " quoatations as these will turn the email/password text to green and this is needed to run the programe


###START OF PROGRAME##



import undetected_chromedriver
from selenium.webdriver.common.by import By
import time


if __name__ == '__main__':
    class Basic:
        ##basic setup to the driver##
        def __init__(self):
            self.driver = undetected_chromedriver.Chrome()
            self.driver.get("https://tinder.com/")
            self.driver.delete_all_cookies()

        ##contains login code untill loged in with google##
        def login(self):
            time.sleep(10)
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()
            time.sleep(8)
            ##this clicks on sign to google page and signs with google account##
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button").click()
            self.handle = []
            self.handle = self.driver.window_handles
            print(self.driver.window_handles)
            self.driver.switch_to.window(self.handle[1])
            time.sleep(10)
            self.driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(
                email)
            time.sleep(8)
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(
                password)
            time.sleep(7)
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
            time.sleep(10)
            self.driver.switch_to.window(self.handle[0])
            print(self.driver.window_handles)
            time.sleep(15)
            ##this clicks over the basic tinder allow and enable notifications buttons##
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
            time.sleep(20)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[2]/span').click()
            time.sleep(20)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="s-138260025"]/div/div[2]/div/div/div[1]/button').click()
            time.sleep(10)

        ##contains auto swipe AND also closes two popup notifications
        # 1 popup is put tinder on homescreen
        # 2 popup is super likes
        #if there are any more popups please add them using a except Exception(see self.popup for more insight##
        def swiping(self):
            from random import random
            while True:
                time.sleep(1)
                try:
                    ran = random()
                    if ran <= 0.90:
                        time.sleep(0.5)
                        self.driver.find_element(By.XPATH,
                                                 "//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-like-green):a']").click()
                    else:
                        time.sleep(0.5)
                        self.driver.find_element(By.XPATH,
                                                 "//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-pink):a']").click()
                        time.sleep(1)
                except Exception:
                    try:
                        self.popup = self.driver.find_element(By.XPATH,
                                                              '//*[@id="s-1866641101"]/div/div/div[2]/button[2]')
                        self.popup.click()
                    except Exception:
                        try:
                            self.new_popup = self.driver.find_element(By.XPATH,
                                                                      '//*[@id="s-1866641101"]/div/div/button[2]')
                            self.new_popup.click()
                        except:
                            self.driver.close()

        ##function to first run the login page then the auto swiping function in the same browser##
        def run(self):
            self.first_login = Basic.login(self)
            self.second_swipe = Basic.swiping(self)
            self.all = self.first_login, self.second_swipe


    ##runs the programe##
    RUN = Basic().run()


##END OF PROGRAMME##
