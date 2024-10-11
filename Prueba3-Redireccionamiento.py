from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura el driver
driver = webdriver.Chrome()

# Abre la página
driver.get("file:///C:/Users/ESDPC/Documents/Maribel/UABC/Semestre VI/TEDS/ProyectoFinalV3/NEWtech_Predictions/newtech/templates/SignIn.html")

# Hace clic en el enlace de "Sign In"
sign_in_link = driver.find_element(By.LINK_TEXT, "Sign In")
sign_in_link.click()

# Verifica que la URL haya cambiado a la página de index luego de haber iniciado sesion
assert driver.current_url == "file:///C:/Users/ESDPC/Documents/Maribel/UABC/Semestre VI/TEDS/ProyectoFinalV3/NEWtech_Predictions/newtech/templates/index.html"

# Cierra el driver
driver.quit()
