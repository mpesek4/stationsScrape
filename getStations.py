from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get('http://www.radiosure.com/stations/')

# click radio button
# iframe = driver.find_elements_by_tag_name('iframe')[0]

# print("iframe is", iframe)
# driver.switch_to.frame(iframe)



# driver.find_element_by_css_selector("body > b > b:nth-child(26) > a").click()



WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"#post-264 > div > p:nth-child(2) > iframe")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > b > b:nth-child(26) > a"))).click()





