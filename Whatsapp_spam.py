#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 00:06:10 2017

@author: Prafull
"""

from selenium import webdriver
b = webdriver.firefox()
b.get('http://web.whatsapp.com')
input()
elem = b.find_element_by_xpath('//span[contains(text(),"Your friend name")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
while True:
	elem1[1].send_keys('Your whatsapp is hacked')
	b.find_element_by_class_name('send-container').click()
 
