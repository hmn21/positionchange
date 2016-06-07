from __future__ import print_function
from selenium import webdriver
import smtplib
import time
driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get("http://www.shfe.com.cn/bourseService/businessdata/calendar/")
time.sleep(1)
print(driver.find_element_by_id("calendartext").text)
text = driver.find_element_by_id("calendartext").text
driver.close()


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("email", "")

msg = "YOUR MESSAGE!"
server.sendmail("from", "to", msg)
server.quit()
