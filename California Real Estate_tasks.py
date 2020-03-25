from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "accept").click()

print(driver.find_element(By.LINK_TEXT, "California Real Estate").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))

assert "California Real Estate" in driver.title
print(driver.title)

driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")

driver.implicitly_wait(10)


driver.find_element(By.NAME, "g2-name").send_keys("Vitaliy and Mariya")


driver.find_element(By.ID, "g2-email").send_keys("vpark191070@gmail.com")


driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Hello!  ")
driver.find_element(By.ID,"contact-form-comment-g2-message").send_keys("How are you? ")
driver.find_element(By.NAME, "g2-message").send_keys("I am fine, ")
driver.find_element(By.TAG_NAME, "textarea").send_keys("Thank you!")

driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").click()

driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))



# closing browser tab
driver.close()
