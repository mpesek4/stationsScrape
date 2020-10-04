from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get('http://www.radiosure.com/stations/')

# click radio button
python_button = driver.get_element_by_xpath(//*[normalize-space(@text)='Download updated stations database (updated on October 04, 2020).'])
print(python_button)
python_button.click()