from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.implicitly_wait(10)

# Window size before resizing
print("Current Window Size:", driver.get_window_size())

# Set a fixed browser size
driver.set_window_size(1280, 800)

print("New Window Size:", driver.get_window_size())

# Consistent window size ensures that responsive web pages
# behave the same way during every automation test.

driver.get("https://www.lambdatest.com/selenium-playground/")

# Open Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

# Navigate back
driver.back()

# Open Google in a new tab
driver.execute_script('window.open("https://www.google.com");')

# Print window handles
print("Window Handles:", driver.window_handles)

# Switch to new tab
driver.switch_to.window(driver.window_handles[1])

# Print title
print("New Tab Title:", driver.title)

# Switch back
driver.switch_to.window(driver.window_handles[0])

# Save screenshot
driver.save_screenshot("playground_screenshot.png")

print("Screenshot saved successfully.")

driver.quit()
