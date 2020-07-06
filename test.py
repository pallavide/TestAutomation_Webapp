from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome("C:\\Users\\Corleone\\Downloads\\driver\\chromedriver.exe")

#Go to the site
driver.get('https://joinassembly.com/')
driver.maximize_window()
time.sleep(5)

#Search for the email field in the page and list the number of email fields available
ele1 = driver.find_elements(By.NAME, 'EMAIL')
print(len(ele1))

#Trying with first set of email id provided
driver.find_element_by_xpath("//*[@id='reviews']/section[5]/div[2]/div/div/div/form/div/input").send_keys("abc@gmail.com")
driver.find_element_by_xpath("//*[@id='reviews']/section[5]/div[2]/div/div/div/form/div/span[2]/button").click()
print("the credentials are not working")
time.sleep(5)

#Trying with second set of email id provided
driver.find_element_by_xpath("//*[@id='reviews']/section[5]/div[2]/div/div/div/form/div/input").send_keys("abc@carrothr.com")
driver.find_element_by_xpath("//*[@id='reviews']/section[5]/div[2]/div/div/div/form/div/span[2]/button").click()
time.sleep(3)
print(driver.title)
time.sleep(5)

#going back to the original page
driver.back()
print(driver.title)

#Clicking on ‘Feature’ in the header should navigate to the Feature section
driver.find_element_by_xpath("//*[@id='home']/nav/div/div[1]/div/ul/li[2]/a").click()
time.sleep(3)

#‘Recognition’ tab should be highlighted
status1 = driver.find_element_by_xpath("//*[@id='features']/div/div/div[1]/div[1]/ul/li[1]/a").is_displayed()
print(status1)

#Clicking on ‘Anniversaries and Birthdays’ should enable this tab and disable all other tabs
driver.find_element_by_xpath("//*[@id='features']/div/div/div[1]/div[1]/ul/li[2]/a").click()
status2 = driver.find_element_by_xpath("//*[@id='features']/div/div/div[1]/div[1]/ul/li[2]/a").is_enabled()
print(status2)

#clciking the home button
driver.find_element_by_xpath("//*[@id='home']/nav/div/div[1]/div/ul/li[1]/a").click()
time.sleep(2)

#scroll down the page till the footer
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#click on ‘Contact Us’ under Support
driver.find_element_by_xpath("//*[@id='home']/footer/div[2]/div[1]/div[3]/div/a[1]").click()

#Enter ‘Slack’ in ‘Find an answer yourself’ field and verify the results displayed.
#automating the intercom pop-up
wait = WebDriverWait(driver, 3)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "intercom-u5foh5 ejdnm0c2")))

driver.switch_to.frame("intercom-u5foh5 ejdnm0c2")
ele2 = driver.find_element_by_xpath("//*[@id='intercom-container']/div/div/div[1]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/input")
ele2.send_keys('slack')

ele3 = driver.find_element_by_xpath("//*[@id='intercom-container']/div/div/div[1]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/input")
ele3.click()

#verify the results displayed

print_text = Select(ele3)
all_options = print_text.options

for option in all_options:
    print(option.text)






