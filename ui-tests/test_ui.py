import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

def test_ws_name_ok(driver):
    driver.find_element(By.ID, "name").send_keys("Master Yoda")
    driver.find_element(By.CSS_SELECTOR, "input[type=button]").click()
    assert driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > table").is_displayed(), "Customer List Screen should be displayed"

def test_ws_empty_name(driver):
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.CSS_SELECTOR, "input[type=button]").click()
    alert = Alert(driver)
    assert alert.text == "Please provide your name"
    alert.accept()

def test_cls_size_category(driver):
    driver.find_element(By.ID, "name").send_keys("Master Yoda")
    driver.find_element(By.CSS_SELECTOR, "input[type=button]").click()
    customers = driver.find_elements(By.CSS_SELECTOR, "#root > div > div > div > div > table > tbody > tr")

    for c in customers:
        employees = int(c.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text)
        size = c.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        assert (employees<=2500 and size=='Small') or ((employees>2500 and employees<=5000) and size=='Medium') or (employees>5000 and size=='Big') , "Customer category by size is incorrect."

def test_cds_contact_info(driver):
    driver.find_element(By.ID, "name").send_keys("Master Yoda")
    driver.find_element(By.CSS_SELECTOR, "input[type=button]").click()
    customers = driver.find_elements(By.CSS_SELECTOR, "#root > div > div > div > div > table > tbody > tr")

    for c, _ in enumerate(customers):
        driver.find_element(By.CSS_SELECTOR, f"#root > div > div > div > div > table > tbody > tr:nth-child({c+1}) > td:nth-child(1)").click()
        try:
            contactinfo = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > p:nth-child(5)").text
            assert (contactinfo.split('Contact:')[1] is not None) and (contactinfo.split('Contact:')[1].strip() != ''), "The Contact info is empty"
        except NoSuchElementException:
            alert = Alert(driver)
            assert alert.text == "No contact info available", "An error popup should have been displayed"
            alert.accept()
        driver.find_element(By.CSS_SELECTOR, "input[type=button]").click()

if __name__ == "__main__":
    pytest.main()