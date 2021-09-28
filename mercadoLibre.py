import unittest
from unittest.case import TestCase
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoAlertPresentException

class MercadoLibre(unittest,TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get()

        