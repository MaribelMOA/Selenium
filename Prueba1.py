from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura el driver
driver = webdriver.Chrome()

# Abre la página
driver.get("file:///C:/Users/ESDPC/Documents/Maribel/UABC/Semestre VI/TEDS/ProyectoFinalV3/NEWtech_Predictions/newtech/templates/SignUp.html")

# Verifica que los campos de texto y el botón están presentes
assert driver.find_element(By.ID, "first_name")
assert driver.find_element(By.ID, "last_name")
assert driver.find_element(By.ID, "email")
assert driver.find_element(By.ID, "password")
assert driver.find_element(By.XPATH, "//button[text()='Sign Up']")

# Cierra el driver
driver.quit()
