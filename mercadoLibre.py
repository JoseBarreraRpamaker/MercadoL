
import unittest
from unittest.case import TestCase
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from time import sleep

class MercadoLibre(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C://Users/pc/OneDrive/Escritorio/driverCho/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        pais = driver.find_element_by_id("UY")
        pais.click()

        buscador = driver.find_element_by_name("as_word")
        buscador.click()
        buscador.clear()
        buscador.send_keys("Playstation 5")
        buscador.submit()
        sleep(3)

        ubicacion = driver.find_element_by_partial_link_text("Maldonado")
        ubicacion.click()
        sleep(3)

        condicion = driver.find_element_by_partial_link_text("Nuevo")
        condicion.click()
        sleep(4)

        articulos =  []
        precios = []

        for i in range(5):
            articulo = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articulos.append(articulo)
            precio = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]').text
            precios.append(precio)


            print(articulos,precios)


    

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)        



    