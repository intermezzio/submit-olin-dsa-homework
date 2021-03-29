import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import EMAIL, PASSWORD, GITHUB_URL

login_url = "https://canvas.olin.edu/"

driver = webdriver.Firefox()

driver.get(login_url)
time.sleep(2)

username_button = driver.find_element_by_css_selector("#i0116")
username_button.send_keys(EMAIL)

submit_button = driver.find_element_by_css_selector("#idSIButton9")
submit_button.click()
time.sleep(1)

password_button = driver.find_element_by_css_selector("#i0118")
password_button.send_keys(PASSWORD)

submit_button = driver.find_element_by_css_selector("#idSIButton9")
submit_button.click()

dont_save_password_button = driver.find_element_by_css_selector("#idBtn_Back")
dont_save_password_button.click()

driver.get("https://canvas.olin.edu/courses/249/assignments")
time.sleep(1)

upcoming_assignments = driver.find_elements_by_css_selector("#assignment_group_upcoming_assignments .ig-row__layout .ig-info a")

that_welcome_thing = driver.find_element_by_css_selector(".fOyUs_bGBk.fOyUs_fKyb.fOyUs_cuDs.fOyUs_cBHs.fOyUs_eWbJ.fOyUs_fmDy.fOyUs_eeJl.fOyUs_cBtr.fOyUs_fuTR.fOyUs_cnfU.fQfxa_bGBk")
that_welcome_thing.click()

links = list()
for el in upcoming_assignments:
	links.append(el.get_attribute("href"))

print(links)


for link in links:
	driver.get(link)
	time.sleep(3)

	root_element = driver.find_element_by_css_selector('html')
	# root_element.send_keys(Keys.END)

	entry = driver.find_element_by_css_selector(".fOyUs_bGBk.ftPBL_bGBk.ftPBL_ycrn input")
	print(entry)
	entry.clear()
	entry.send_keys(GITHUB_URL)
	time.sleep(2)

	root_element.send_keys(Keys.END)

	submit_button = driver.find_element_by_id("submit-button")
	submit_button.click()