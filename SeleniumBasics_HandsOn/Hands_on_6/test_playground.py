import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("message", ["Hello"])
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    textbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-message"))
    )

    textbox.clear()
    textbox.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    import time
    time.sleep(3)

    msg = driver.find_element(By.ID, "message")

    print("TEXT :", repr(msg.text))
    print("HTML :", msg.get_attribute("outerHTML"))

    assert True


def test_checkbox_demo(driver, base_url):

    driver.get(base_url + "checkbox-demo")

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()


def test_dropdown_selection(driver, base_url):

    driver.get(base_url + "select-dropdown-demo")

    dropdown = Select(
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "select-demo"))
        )
    )

    dropdown.select_by_visible_text("Wednesday")

    selected = dropdown.first_selected_option.text

    assert selected == "Wednesday"