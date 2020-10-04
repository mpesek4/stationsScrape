from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get('http://www.radiosure.com/stations/')

# click radio button
python_button = driver.find_elements_by_partial_link_text('Down')
print(python_button)
python_button.click()