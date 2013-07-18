#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize

browser = mechanize.Browser()
response = browser.open("http://projecteuler.net/login")

browser.select_form("login_form")
browser["username"] = "itroot"
browser["password"] = open("password").read().rstrip("\n")
response = browser.submit()
response = browser.open("http://projecteuler.net/problem=125")
#print response.read()
#"""
for link in browser.links():
    print link
for form in browser.forms():
    print form
#"""
