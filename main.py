from selenium import webdriver
import time

# Configuración del controlador del navegador
# En este ejemplo se usará el controlador de Google Chrome
driver = webdriver.Chrome()

# Cargar la página web local
url_base = "http://192.168.0.113"
driver.get(url_base)
# Esperar un tiempo para que el sitio cargue completamente
time.sleep(3)
# Ejecutar la función en la consola del navegador


try:
    # Ejecutar la función JavaScript en la consola del navegador
    driver.execute_script("opentab(event, 'filesystab', 'mainuitabscontent', 'mainuitablinks')")
    # driver.execute_script("mifuncion();")
    
except Exception as e:
    print("Dentro")
    html_content = driver.page_source
    content = html_content

    #TODO aplicar la funcionalidad de seleccionar y ejecutar funciones: 
    #Sacar el elemento
    #Llamar la función del selectElement
    #Guardar el position del elemento seleccionado
    #llamar el onclick del play con el position almacenado


    # Obtener los elementos de la lista
    ul_element = driver.find_element_by_id("files_fileList")
    li_elements = ul_element.find_elements_by_class_name("newlist-group-item")
    
    # Imprimir los textos de los elementos li
    contenido = ""
    for li in li_elements:
        contenido+=li

    content = contenido
    with open("1contentWEB.html", "w", encoding="utf-8") as file:
        file.write(content)
    time.sleep(15)
    print(f"Error al ejecutar la función: {e}")
else:
    # Obtener el contenido HTML después de ejecutar la función

    # Hacer algo con el contenido HTML
    print("Entró")
# Esperar un tiempo para que el sitio cargue completamente
# Obtener el contenido HTML de la página después de ejecutar la función

driver.quit()

# import requests
# from bs4 import BeautifulSoup
# import execjs

# # Realizar una solicitud GET al archivo HTML
# url = "http://192.168.0.113"
# payload = {'function_name': "opentab(event, 'filesystab', 'mainuitabscontent', 'mainuitablinks')"}
# response = requests.post(url, payload)

# # Verificar que la solicitud haya sido exitosa
# if response.status_code == 200:

#     # Analizar el contenido HTML con BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Buscar el componente div y extraer su atributo onclick
#     ahref = soup.find('a', {'onclick': "opentab(event, 'filesystab', 'mainuitabscontent', 'mainuitablinks')"})
#     # print(ahref)

#     onclick = ahref['onclick']

#     print(f"Onclick: {onclick}")


#     content = soup.text
#     with open("file123abc.txt", "w", encoding="utf-8") as file:
#         file.write(content)

    
# else:
#     # Manejar el error
#     print(f"Error al obtener index.html: {response.status_code}")
