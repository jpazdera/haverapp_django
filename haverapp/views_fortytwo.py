from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render
import urllib2
import datetime
from xml.etree import ElementTree

def fortytwo(request):
	raw_response =  urllib2.urlopen("http://www.haverford.edu/goevents/").read()
	xml_response = ElementTree.fromstring(raw_response)
	product = ""
	for i in xml_response:
		product += "James"
	return raw_response
#	return HttpResponse(xml_response)

