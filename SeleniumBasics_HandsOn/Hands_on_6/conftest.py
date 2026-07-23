import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = "chromedriver-win64/chromedriver-win64/chromedriver.exe"


@pytest.fixture(scope="session")
def base_url():
    return "https://www.testmuai.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver(request):
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.implicitly_wait(10)

    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            driver.save_screenshot(f"{item.name}_failure.png")