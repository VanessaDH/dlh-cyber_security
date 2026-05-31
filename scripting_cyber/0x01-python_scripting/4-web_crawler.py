#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_website(start_url, max_depth=2):
	visited = set()

	def crawl(url, depth):
		if depth == 0 or url in visited:
			return
		try:
			headers = {'User-Agent': 'Mozilla/5.0'}
			response = requests.get(url, timeout=5, headers=headers)
			print(f"Crawling: {url}")
			visited.add(url)

			soup =  BeautifulSoup(response.text, 'html.parser')
			base_domain = urlparse(start_url).netloc

			for tag in soup.find_all('a', href=True):
				link = urljoin(url, tag['href'])
				link_domain = urlparse(link).netloc
			
				if link_domain == base_domain and link not in visited:
					crawl(link, depth - 1)
		except Exception:
			pass
	
	crawl(start_url, max_depth)
	return visited 
