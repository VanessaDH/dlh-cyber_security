#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_website(start_url, max_depth=2, visited=None):
	if visited is None:
		visited = set()

	if max_depth == 0 or start_url in visited:
		return visited
	
	try:
		response = requests.get(start_url, timeout=5)
		print(f"Crawling: {start_url}")
		visited,add(start_url)

		soup =  BeautifulSoup(response.text, 'html.parser')
		base_domain = urlparse(start_url).netloc

		for tag in soup.find_all('a', href=True):
			link = urljoin(start_url, tag['href'])
			link_domain = urlparse(link).netloc
			
			if link_domain == base_domain and link not in visited:
				crawl_website(link, max_depth - 1, visited)
	except Exception:
		pass
	
	return visited 
