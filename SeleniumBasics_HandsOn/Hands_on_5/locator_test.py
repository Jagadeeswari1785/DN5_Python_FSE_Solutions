from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# -----------------------------
# Locator Strategies
# -----------------------------

# 1. By ID
element1 = driver.find_element(By.ID, "user-message")

# 2. By.NAME
# Current LambdaTest page does not have a 'name' attribute for this input,
# so By.NAME cannot be demonstrated.

# 3. By Class Name
element3 = driver.find_element(By.CLASS_NAME, "border")

# 4. By Tag Name
element4 = driver.find_element(By.TAG_NAME, "input")

# 5. Absolute XPath
element5 = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
)

# 6. Relative XPath
element6 = driver.find_element(
    By.XPATH,
    "//*[@id='user-message']"
)

print("All locator strategies worked successfully.")

# -----------------------------
# CSS Selectors
# -----------------------------

# CSS by ID
driver.find_element(By.CSS_SELECTOR, "#user-message")

# CSS by Attribute
driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)

# CSS Parent > Child
driver.find_element(By.CSS_SELECTOR, "div > input")

print("CSS selectors worked successfully.")



# -----------------------------
# Checkbox Demo
# -----------------------------

# Open Checkbox Demo page
driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

# Find Option 1 label using text()
label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("First Label:", label.text)

# Find all labels containing 'Option'
labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Labels Found:")

for item in labels:
    print(item.text)



# --------------------------------------------------------
# Preferred Locator Ranking
#
# 1. ID
#    - Best choice because IDs are usually unique, fast,
#      readable, and stable.
#
# 2. CSS Selector
#    - Fast, flexible, and easy to read. Preferred when
#      ID is not available.
#
# 3. Name
#    - Good if the 'name' attribute is unique.
#
# 4. Relative XPath
#    - Useful for locating elements based on attributes
#      or relationships. More stable than absolute XPath.
#
# 5. Class Name
#    - Useful, but class names are often shared by
#      multiple elements.
#
# 6. Absolute XPath
#    - Least preferred because even a small HTML
#      structure change can break it.
# --------------------------------------------------------

driver.quit()