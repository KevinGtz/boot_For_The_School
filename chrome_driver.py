#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

# This is a test in order to use Chrome driver extention for manipulate Chrome
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from llaves import numero_de_cuenta, contrasenia


def open_aragon_page():
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('http://www.aragon.unam.mx/evaluacion1.1/Login.php')
    search = driver.find_element_by_name('nombre_usuario')
    search_2 = driver.find_element_by_name('contrasenia')
    button = driver.find_element_by_class_name('button')

    search.send_keys(numero_de_cuenta)
    search_2.send_keys(contrasenia)
    button.click()

    evaluar = driver.find_element_by_link_text('Evaluar Cursos').click()

    button_2 = driver.find_element_by_class_name('button')
    button_2.click()

    for i in range(1, 25):

        always = driver.find_element_by_name('P{}'.format(i))
        always.click()

    button_3 = driver.find_element_by_class_name('button').click()

    search.send_keys(Keys.RETURN)
    driver.implicity_wait(100)

open_aragon_page()
