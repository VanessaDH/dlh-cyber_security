#!/usr/bin/env python3
import dns.resolver
import dns.rdatatype

def query_dns_records(domain_name):
	results ={}
	record_types = ['A', 'AAA', 'MX','NS', 'TXT', 'SOA']

	for record_type in record_types:
		try:
			answers = dns.resolver.resolve(domain_name, record_type)
			results[record_type] = answers
		except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers,dns.rdatatype.UnknownRdatatype):
			pass
			
	return results	
