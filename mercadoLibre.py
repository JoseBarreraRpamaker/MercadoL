
import unittest
from unittest.case import TestCase
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from time import sleep

class MercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(20)
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

    

        articulos =  []
        precios = []
        i=2
    
        while i <= 3:
            articulo = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i}]/div/div/div[2]/div[1]/a/h2').text
            articulos.append(articulo)                      
            precio = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i}]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]').text
            precios.append(precio)                    
            i += 1   
            print(articulos,precios)
            print("productos")                                 


           


    

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)        



    
