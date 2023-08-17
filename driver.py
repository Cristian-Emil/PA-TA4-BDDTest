from selenium import webdriver
""" webbrowser"""

class Driver:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close_pyta(self):
        self.driver.quit()
