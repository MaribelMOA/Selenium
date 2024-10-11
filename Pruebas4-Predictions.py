from selenium import webdriver
from selenium.webdriver.common.by import By
# Configura el driver
driver = webdriver.Chrome()

# Abre la página
driver.get("file:///C:/Users/ESDPC/Documents/Maribel/UABC/Semestre VI/TEDS/ProyectoFinalV3/NEWtech_Predictions/newtech/templates/addNewPredictions.html")

# Encontrar el campo MRP y realizar pruebas
mrp_input = driver.find_element(By.NAME, 'mrp')
# Probar ingresar un valor inválido
mrp_input.send_keys("invalid")  # Intentar ingresar un valor inválido
# Verificar que no se haya aceptado el texto no válido
assert "invalid" not in mrp_input.get_attribute('value')  # Debe rechazar texto

# Encontrar el campo Outlet ID y realizar pruebas
outlet_id_input = driver.find_element(By.NAME, 'outlet_id')
outlet_id_input.clear()  # Limpiar cualquier entrada anterior
outlet_id_input.send_keys("OUT123")  # Ingresar un valor válido
# Verificar que el valor ingresado sea el correcto
assert outlet_id_input.get_attribute('value') == "OUT123"

# Finalmente, cerramos el navegador
driver.quit()

