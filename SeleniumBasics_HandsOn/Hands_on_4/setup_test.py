"""
Selenium Components

1. WebDriver
   - WebDriver is the main component of Selenium.
   - It communicates with the browser using browser drivers.
   - It performs actions like opening websites, clicking buttons, entering text, and reading page data.

2. Selenium Grid
   - Selenium Grid allows tests to run on multiple browsers and multiple machines at the same time.
   - It helps reduce execution time by running tests in parallel.

3. Selenium IDE
   - Selenium IDE is a browser extension used to record and play back test cases.
   - It is useful for beginners and for quickly generating automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Step 1: Imports completed")

# Headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")

print("Step 2: Downloading/locating ChromeDriver...")
driver_path = ChromeDriverManager().install()
print("Driver path:", driver_path)

print("Step 3: Starting Chrome...")
driver = webdriver.Chrome(
    service=Service(driver_path),
    options=options
)

# Implicit wait
driver.implicitly_wait(10)

# Implicit waits apply to every element search.
# They are generally considered a bad practice because they can slow
# execution and make debugging difficult. Explicit waits are preferred.

print("Step 4: Opening website...")
driver.get("https://www.lambdatest.com/selenium-playground/")

print("Step 5: Page title:")
print(driver.title)

driver.quit()
"""
Task 1: Selenium Architecture and Environment Setup

1. WebDriver
   - WebDriver is the main component of Selenium.
   - It communicates with the browser through browser drivers.
   - It automates browser actions like opening websites, clicking buttons, entering text, etc.

2. Selenium Grid
   - Selenium Grid allows parallel execution of tests on multiple browsers and machines.
   - It helps reduce test execution time.

3. Selenium IDE
   - Selenium IDE is a browser extension.
   - It records and plays back browser actions.
   - It is useful for beginners and for generating automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome to run in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit wait
driver.implicitly_wait(10)

# Note:
# Implicit wait is applied globally for all element searches.
# It is generally considered a bad practice because it waits for every
# element lookup and can slow down execution.
# Explicit waits are preferred because they wait only when needed.

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:", driver.title)

driver.quit()
print("Step 6: Browser closed")
