import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
key = input(str())
################################################## Kerry #######################################################
driver.get("https://th.kerryexpress.com/th/track/v2/")
wait = WebDriverWait(driver, 10)

prepair = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/kett-root/kett-search-form/div/div/div/form/div/div[1]/input")))
prepair.click()
input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/kett-root/kett-search-form/div/div/div/form/div/div[1]/textarea")))
input_element.send_keys(f"{key}") #SHP5319461816

button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/kett-root/kett-search-form/div/div/div/form/div/div[2]/button")))
button_element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div")))
number_element = driver.find_element(By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[1]/div[1]/div/span")
กำหนดส่ง_element = driver.find_element(By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[1]/div[2]/div[2]/div/span")
จาก_element = driver.find_element(By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[2]/div[1]/div[1]/span[2]")
จากจังหวัด_element = driver.find_element(By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[2]/div[1]/div[1]/span[3]")
ถึง_element = driver.find_element(By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[2]/div[1]/div[2]/span[2]")
ถึงจังหวัด_element = driver.find_element(By.XPATH, "/html/body/kett-root/div[1]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[2]/div[1]/div[2]/span[3]")

number = number_element.get_attribute("innerHTML")
กำหนดส่ง = กำหนดส่ง_element.get_attribute("innerHTML")
จาก = จาก_element.get_attribute("innerHTML")
จากจังหวัด = จากจังหวัด_element.get_attribute("innerHTML")
ถึง = ถึง_element.get_attribute("innerHTML")
ถึงจังหวัด = ถึงจังหวัด_element.get_attribute("innerHTML")

print("Tracking Number :", number)
print(กำหนดส่ง)
print("จาก :", จาก)
print("จากจังหวัด :", จากจังหวัด)
print("ถึง :", ถึง)
print("ถึงจังหวัด :", ถึงจังหวัด)

driver.quit()
####################################################################################################################