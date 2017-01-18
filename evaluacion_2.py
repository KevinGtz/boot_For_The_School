#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()

	def tearDown(self):
		pass
		#self.driver.close()

#para correr el servidor se usa el comando *nosetests "programa"

	def test_open_aragon_login(self):
		self.driver.get(u'http://www.aragon.unam.mx/evaluacion1.1/Login.php')

		search = self.driver.find_element_by_name('nombre_usuario')
		search_2 = self.driver.find_element_by_name('contrasenia')
		button = self.driver.find_element_by_class_name('button')

		search.send_keys('106004731')
		search_2.send_keys('09071993')
		button.click()

		evaluar =  self.driver.find_element_by_link_text('Evaluar Cursos').click()

		button_2 = self.driver.find_element_by_class_name('button')
		button_2.click()

		for i in range(1,25):

			always = self.driver.find_element_by_name('P{}'.format(i))
			always.click()

		button_3 = self.driver.find_element_by_class_name('button').click()

		search.send_keys(Keys.RETURN)
		driver.implicity_wait(100)
