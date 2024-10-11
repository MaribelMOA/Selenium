from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura el driver
driver = webdriver.Chrome()

# Abre la página
driver.get("file:///C:/Users/ESDPC/Documents/Maribel/UABC/Semestre VI/TEDS/ProyectoFinalV3/NEWtech_Predictions/newtech/templates/SignIn.html")

# Intenta enviar el formulario sin rellenar los campos
sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign In']")
sign_up_button.click()

# Verificar que no se haya enviado el formulario (HTML5 requerirá que se completen los campos)
assert "This field is required" in driver.page_source

# Cierra el driver
driver.quit()
