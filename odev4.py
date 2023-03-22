# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" 
# sitesinde gerçekleştirmeniz istenmektedir.


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class sauceTest:
    def notEnteredPasswordAndUsername(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(5)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface:Username and password do not match any user in this service"
        print(f"Test Sonucu: {testResult}")

    def notEnteredPassword(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("name")
        sleep(5)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print("Lütfen şifre alanını doldurunuz.")
        print(f"Test sonucu: {testResult}")


    def locked_out(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secrect_sauce")
        sleep(3)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu:{testResult}")

    def icon_x(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(3)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        x_icon=driver.find_element(By.CLASS_NAME,"error-buton")
        x_icon.click()  

    def loginInventory(self): 
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secrect_sauce")
        sleep(3)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)   
        driver.get("https://www.saucedemo.com/invertory.html")

    def invertryList(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secrect_sauce")
        sleep(3)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)   
        driver.get("https://www.saucedemo.com/invertory.html")
        list=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Toplam Ürün :{len(list)}")



test=sauceTest()
test.notEnteredPasswordAndUsername()
test.notEnteredPassword()
test.locked_out()
test.icon_x()
test.loginInventory()
test.invertryList()

