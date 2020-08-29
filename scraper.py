from selenium import webdriver
from datetime import date
from dateutil.parser import parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
passwd = open('pass.txt', 'r')
passwd = passwd.read()
class classBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        bot = self
        self.driver.get("https://classroom.google.com/?emr=0")
        email = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        email.send_keys("elamhd21@ausdk12.org")
        next = bot.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        next.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains("SSO"))
        usernamefield = self.driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/table/tbody/tr[1]/td[2]/p/input')
        usernamefield.send_keys("elamhd21")
        passfield = self.driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/table/tbody/tr[2]/td[2]/p/input")
        passfield.send_keys(passwd)
        loginbutton = self.driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/table/tbody/tr[3]/td/p/input")
        loginbutton.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains("Sign in"))
        try:
            verifybutton = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
            verifybutton.click()
        except Exception as e:
            pass    
    def gotophysics(self):
        self.driver.get("https://classroom.google.com/h")
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/ol/li[1]")))
        physics = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ol/li[5]/div[1]/div[3]/h2/a[1]") 
        physics.click()
    def gotocsa(self):
        self.driver.get("https://classroom.google.com/h")
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/ol/li[1]")))
        csa = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ol/li[4]/div[1]/div[3]/h2/a[1]") 
        csa.click()   
    def navigate(self, page):
        if page == "Stream":
            stream = self.driver.find_element_by_xpath("/html/body/nav/div[2]/div/div[1]/a")
            stream.click()
        elif page == "Classwork":
            classwork = bot.driver.find_element_by_xpath("/html/body/nav/div[2]/div/div[2]/a")
            classwork.click()
    def grabstream(self,daysold):
        item = 1
        posts = []
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[1]/div[1]/div[1]/div[1]/span/span[1]")))        
        while True:
            currentpost = ""
            try: 
                currentpostdate = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[1]/div[1]/span/span[1]").text.strip("Created ")

            except Exception as e:
                print(e)
                break
            if ":" in currentpostdate:
                date = currentpostdate #= self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[1]/div[1]/span/span[1]").text.strip("Created ")
                value = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[2]/div[1]/html-blob/span[1]").text
                posts.append([value,date])
                item += 1
            else:
                date = parse(currentpostdate).date()
                delta = date.today() - date
                if delta.days <= daysold:
                    print("appendd")
                    date = currentpostdate = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[1]/div[1]/span/span[1]").text.strip("Created ")
                    value = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[2]/div[1]/html-blob/span[1]").text
                    posts.append([value,date])
                    item += 1
                else:
                    break
        empty = []
        return posts if posts == empty else ["no posts in your selected range", "sorry :("]
        def gethomework(self,duein): 
            navigate("Classwork")
        item = 1
        posts = []      
        while True:
            currentpost = ""
            try: 
                currentpostdate = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/main/div/div/div[4]/ol/li[2]/div[2]/div/div/div[3]/ol/li[" + item + "]/div/div/div[3]/div[2]").text.strip("Created ")

            except Exception as e:
                #print(e)
                break
            if ":" in currentpostdate:
                date = currentpostdate #= self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[1]/div[1]/span/span[1]").text.strip("Created ")
                value = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[2]/div[1]/html-blob/span[1]").text
                posts.append([value,date])
                item += 1
            else:
                date = parse(currentpostdate).date()
                delta = date.today() - date
                if delta.days <= daysold:
                    print("appendd")
                    date = currentpostdate = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[1]/div[1]/span/span[1]").text.strip("Created ")
                    value = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div[" + str(item) +"]/div[1]/div[2]/div[1]/html-blob/span[1]").text
                    posts.append([value,date])
                    item += 1
                else:
                    break

if __name__ == "__main__":        
    bot = classBot()
    bot.login()
  #  bot.gotophysics()
  #  bot.grabstream(1)
# /html/body/div[2]/div[3]/main/div/div/div[4]/ol/li[2]/div[2]/div/div/div[3]/ol/li[1]/div/div/div[3]/div[2]
# /html/body/div[2]/div[3]/main/div/div/div[4]/ol/li[2]/div[2]/div/div/div[3]/ol/li[2]/div/div/div[3]/div[2]
# /html/body/div[2]/div[3]/main/div/div/div[4]/ol/li[1]/div[2]/div/div/div[3]/ol/li[1]/div/div[2]/div[1]/div[1]/div[2]/div/html-blob/span