from selenium.webdriver.common.by import By


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert add_button is not None, "Add to basket button is not found"

    #pytest --language=es test_items.py