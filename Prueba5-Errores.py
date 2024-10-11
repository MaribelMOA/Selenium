from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Configura el driver
driver = webdriver.Chrome()

# Abre la página
driver.get("file:///C:/Users/ESDPC/Documents/Maribel/UABC/Semestre VI/TEDS/ProyectoFinalV3/NEWtech_Predictions/newtech/templates/addNewSales.html")

try:
    # Esperar a que el botón de envío esté presente
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='SUBMIT']"))  # Asumiendo que el texto del botón es "SUBMIT"
    )
    submit_button.click()  # Intentar hacer clic en el botón
except Exception as e:
    assert False, f"Submit button raised an error: {e}"

# Finalmente, cerramos el navegador
driver.quit()
