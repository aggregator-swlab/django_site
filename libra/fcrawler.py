from bs4 import BeautifulSoup
import requests
import sys
import re
import urllib2

all_prods = list()

url = "http://www.flipkart.com/search?q=iphone"
page = urllib2.urlopen(url)
soupe = BeautifulSoup(page, "html.parser")
all_links = soupe.find_all("div", class_="gd-col gu3")
for i in all_links:

	prod = dict()

	imgurl = i.find('img')['data-src']
	title = i.select('a.fk-display-block')[0].get('title')
	link = i.select('a.fk-display-block')[0].get('href')
	if i.has_attr('div.fk-stars-small'):
		rating = i.select('div.fk-stars-small')[0].get('title')
	else:
		rating = "NA"
	lst = list()
	for j in range(0, len(i.select('ul.pu-usp li'))):
		lst.append(i.select('ul.pu-usp li span')[j].string)
	price = i.select('span.fk-font-17')[0].string

	# print "Title : " + title
	# print "Price : " + price
	# print "Link : www.flipkart.com" + link
	# print "Img Url : " + imgurl
	# print "Rating : " + rating
	# k=1
	# for j in lst:
	# 	print "Feature " + str(k) + " : " + j
	# 	k=k+1
	# print "\n\n********************************\n\n"

	link = "www.flipkart.com" + link

	prod['ptitle'] = title
	prod['pprice'] = price
	prod['plink'] = link
	prod['pimgurl'] = imgurl
	prod['prating'] = rating

	print prod

	# prod.append()
	# prod.append(price)
	# prod.append(link)
	# prod.append(imgurl)
	# prod.append(rating)
	all_prods.append(prod.copy())
	# print prod
print all_prods
# for i in all_prods:
# 	print i
