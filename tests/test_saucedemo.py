import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browser import get_driver


URL = "https://www.saucedemo.com/"
USER = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def login(driver):

    driver.get(URL)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    driver.find_element(By.ID, "user-name").send_keys(USER)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def test_login_exitoso(driver):

    login(driver)

    assert "inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title


def test_catalogo_productos(driver):

    login(driver)

    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert titulo == "Products"

    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0

    menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert menu.is_displayed()
    assert filtro.is_displayed()

    primer_nombre = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    primer_precio = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"Producto: {primer_nombre}")
    print(f"Precio: {primer_precio}")


def test_carrito(driver):

    login(driver)

    boton_agregar = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn_inventory"
    )

    boton_agregar.click()

    contador = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert contador.text == "1"

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    assert producto_carrito.is_displayed()