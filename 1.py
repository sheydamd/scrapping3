import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.ChromiumEdge()
driver.get("https://typekadeh.com/")
button=driver.find_elements(By.TAG_NAME,"button")
button[0].click()
time.sleep(3)
inputs=driver.find_elements(By.CLASS_NAME,"tabs")
inputs[1].click()
mains=driver.find_elements(By.CLASS_NAME,"h-tabs")
for m in mains:
    b=m.find_elements(By.TAG_NAME,"input")
b[0].send_keys("sheydamohamaddust@gmail.com")
b[1].send_keys("sheydamd")
b[2].send_keys("123456")
btn1=driver.find_elements(By.CLASS_NAME,"card-dialog__body")
for btn in btn1:
    bt=btn.find_element(By.TAG_NAME,"button")
bt.click()
time.sleep(100)
