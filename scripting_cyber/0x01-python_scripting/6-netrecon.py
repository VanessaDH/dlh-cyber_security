#!/usr/bin/env python3
import socket
import requests
from bs4 import BeautifulSoup

def dns_recon(domain):
	try:
		ip = socket.gethostbyname(domain)
		print(f"	IP ADDRESS:	{ip}")
	except socket.gaierror:
		print(f"	IP ADDRESS: Failed to resolve")

def web_recon(domain):
	try:
		response = requests.get(f"http://{domain}", timeout=5)
		print(f"	Status Code: {response.status_code}")
		
		for key in ['Server','Content-TYpe','X-Frame-Options']:
			if key in response.headers:
				print(f"	{key}: {response.headers[key]}")
				
		soup = BeautifulSoup(response.text, 'html.parser')
		print(f"	Links Found: {len(soup.find_all('a',href=True))}")
	except requests.exceptions.RequestException as e:
		printf(f"	Error: {e}")

def port_scan(domain):

	for port in [80,443]:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1)

			result =  s.connect_ex((domain,port)) == 0
			s.close()

			print(f"	Port {port}: {'OPEN' if result else 'CLOSED'}")
		except Exception:
			print(f"	Port {port}: CLOSED")
