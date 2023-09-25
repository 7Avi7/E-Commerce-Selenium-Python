import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Run(unittest.TestCase):
    # Initialize the Chrome driver
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_LaunchBrowser(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        time.sleep(2)


    def test_firstItem(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        # 1st Item
        addItem1 = self.driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[2]//a[2]")
        # Create an ActionChains object
        actions = ActionChains(self.driver)
        # Double click on the element
        actions.double_click(addItem1).perform()
        self.driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]").click()
        if addItem1 == self.driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[2]//a[2]"):
            print("Added Item No 1")
        time.sleep(2)

    def test_secondItem(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        # 2nd Item
        addItem2 = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[2]")
        # Create an ActionChains object
        actions = ActionChains(self.driver)
        # Double click on the element
        actions.double_click(addItem2).perform()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) div:nth-child(2) button:nth-child(1)").click()

        if addItem2 == self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[2]"):
            print("Added Item No 2")
        time.sleep(2)

    def test_checkOut(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        # Next processes
        self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[class='cart-preview active'] button[type='button']").click()
        time.sleep(2)


    def test_proceed(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/cart")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys(
            'rahulshettyacademy')
        self.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > button:nth-child(14)").click()
        time.sleep(2)

    def test_LocationWithOrderDone(self):
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/country")
        # Select Country
        select_class = Select(self.driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
        select_class.select_by_visible_text('Bangladesh')
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()

        order_done = self.driver.find_element(By.XPATH,
                                         "//span[contains(text(),'Thank you, your order has been placed successfully')]")

        if order_done == self.driver.find_element(By.XPATH,
                                             "//span[contains(text(),'Thank you, your order has been placed successfully')]"):
            print("Order placed")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

