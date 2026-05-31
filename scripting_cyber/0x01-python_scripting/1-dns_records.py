#!/usr/bin/env python3
import dns.resolver
import dns.rdatatype

def query_dns_records(domain_name):
	results ={}
	record_types ={
		'A':dns.rdatatype.A,
		'AAAA': dns.rdatatype.AAAA,
		'MX': dns.rdatatype.MX,
		'NS': dns.rdatatype.NS, 
		'TXT': dns.rdatatype.TXT, 
		'SOA': dns.rdatatype.SOA
	}

	for record_type in record_types:
		try:
			answers = dns.resolver.resolve(domain_name, record_type)
			results[record_type] = answers
		except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
			pass
			
	return results	
