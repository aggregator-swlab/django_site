from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
import subprocess
import json
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import sys
import re
import urllib2

def hello(request):
	return HttpResponse("Hello azhar!!")

def flipkart(request):

	query = "iphone+6"
	all_prods = list()

	f = open("flipkart_raw_data", "w")
	process = subprocess.call(['curl',  '-H', 'Fk-Affiliate-Id:shariffaz', '-H', 'Fk-Affiliate-Token:c569d5da22704c278e90af8226c42174', 'https://affiliate-api.flipkart.net/affiliate/search/json?query=' + query + '&resultCount=10'], stdout=f)

	with open('flipkart_raw_data') as data_file:
		data = json.load(data_file)

	for value in data["productInfoList"]:

		prod = dict()

		prodcat = value['productBaseInfo']['productIdentifier']['categoryPaths']['categoryPath'][0][0]['title']
		prodid = value['productBaseInfo']['productIdentifier']['productId']
		prodtitle = value['productBaseInfo']['productAttributes']['title']
		prodimgurl = value['productBaseInfo']['productAttributes']['imageUrls']['unknown']
		prodmrp = value['productBaseInfo']['productAttributes']['maximumRetailPrice']['amount']
		prodsp = value['productBaseInfo']['productAttributes']['sellingPrice']['amount']
		produrl = value['productBaseInfo']['productAttributes']['productUrl']
		prodbrand = value['productBaseInfo']['productAttributes']['productBrand']

		prod['category'] = prodcat
		prod['id'] = prodid
		prod['title'] = prodtitle
		prod['imgurl'] = prodimgurl
		prod['mrp'] = prodmrp
		prod['sp'] = prodsp
		prod['url'] = produrl
		prod['brand'] = prodbrand

		all_prods.append(prod.copy())

	return render_to_response('flipkart_api.html', {'allprods': all_prods}, context_instance=RequestContext(request))