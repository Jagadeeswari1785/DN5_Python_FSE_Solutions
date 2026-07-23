from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Launch Chrome
service = Service("chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Open Bootstrap Alerts Demo
driver.get("https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/")

# ----------------------------------------------------
# Task 36 - Explicit Wait
# ----------------------------------------------------
start = time.time()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success-auto"))
)

button.click()

# Wait until the success alert is present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "alert-success-auto")
    )
)

print("Success alert located using Explicit Wait.")

end = time.time()
print("Explicit Wait Time:", round(end - start, 2), "seconds")

# ----------------------------------------------------
# Task 37 - time.sleep()
# ----------------------------------------------------
driver.refresh()

driver.find_element(
    By.CSS_SELECTOR,
    "button.btn-success-auto"
).click()

time.sleep(3)

print("Sleep Wait Completed")

# ----------------------------------------------------
# Task 38
# ----------------------------------------------------
# visibility_of_element_located:
# Waits until the element is visible.
#
# element_to_be_clickable:
# Waits until the element is visible, enabled,
# and ready to be clicked.

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success-auto"))
)

print("Element is clickable.")

# ----------------------------------------------------
# Task 39 - Fluent Wait
# ----------------------------------------------------
wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

wait.until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "alert-success-auto")
    )
)

print("Fluent Wait Created Successfully")

driver.quit()