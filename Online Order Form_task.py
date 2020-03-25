from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys("Vitaly")
driver.find_element(By.XPATH, "//input[@placeholder='Last']").send_keys("Pak")

driver.find_element(By.XPATH, "//div//div//div[2]//div[1]//div[1]//input[1]").send_keys("vpark191070""@""gmail.com")

driver.find_element(By.XPATH,"//input[contains(@placeholder,'### ### ####')]").clear()
driver.find_element(By.XPATH,"//input[contains(@placeholder,'### ### ####')]").send_keys("829 969 5678")

driver.find_element(By.XPATH, "//label[@id='radio-0000000e1']//label").click()
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div/div/div[1]/div[1]/input[1]").send_keys("8")

driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div/div/div/div/div[2]").click()
driver.find_element(By.XPATH, "//div[contains(text(),'31')]").click()

driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("Calle El Choco")
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Puerto Plata")
driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys("Puerto Plata")
driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("57000")
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys("Dominican")
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys('\n')

driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[contains(text(),'other:')]").click()
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div[9]/div[1]/div[4]/div[1]/input[1]").send_keys("Choice X")
driver.implicitly_wait(10)
driver.execute_script(str("javascript:document.getElementById('g-recaptcha-response').style.display = null;"))
driver.find_element_by_id('g-recaptcha-response').send_keys("123412341234")
driver.find_element_by_id('g-recaptcha-response').send_keys("\n")


driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, "normal-state").click()

driver.close()
