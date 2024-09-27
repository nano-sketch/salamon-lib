from bs4 import BeautifulSoup as bs
import urllib.request
import random

useragents = ['Mozilla/5.0 (Windows NT 10.1; WOW64; en-US) AppleWebKit/536.43 (KHTML, like Gecko) Chrome/47.0.2538.234 Safari/601.0 Edge/10.37723',
			  'Mozilla/5.0 (Linux; U; Android 5.1; SM-G920F-ORANGE Build/LRX22G) AppleWebKit/533.32 (KHTML, like Gecko)  Chrome/49.0.1995.227 Mobile Safari/601.4',
			  'Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 10.3;; en-US Trident/4.0)',
			  'Mozilla/5.0 (Linux; Android 4.4; Nexus_ 4 Build/KTU84P) AppleWebKit/600.2 (KHTML, like Gecko)  Chrome/52.0.1054.388 Mobile Safari/534.10',
			  'Mozilla/5.0 (Linux i563 ; en-US) AppleWebKit/603.14 (KHTML, like Gecko) Chrome/54.0.1491.189 Safari/536',
			  'Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_5; like Mac OS X) AppleWebKit/603.19 (KHTML, like Gecko)  Chrome/49.0.3984.151 Mobile Safari/600.7',
			  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_0_2; en-US) Gecko/20100101 Firefox/57.1',
			  'Mozilla/5.0 (Windows NT 6.3; Win64; x64; en-US) AppleWebKit/602.29 (KHTML, like Gecko) Chrome/47.0.2092.203 Safari/601',
			  'Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/600.32 (KHTML, like Gecko) Chrome/47.0.1453.187 Safari/600',
			  'Mozilla/5.0 (Linux i552 x86_64) AppleWebKit/600.25 (KHTML, like Gecko) Chrome/54.0.1123.178 Safari/537',
			  'Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_1; like Mac OS X) AppleWebKit/603.11 (KHTML, like Gecko)  Chrome/55.0.3994.178 Mobile Safari/602.5',
			  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_1_8) AppleWebKit/535.37 (KHTML, like Gecko) Chrome/55.0.1802.316 Safari/535',
			  'Mozilla/5.0 (Windows; U; Windows NT 10.1; WOW64) AppleWebKit/600.9 (KHTML, like Gecko) Chrome/50.0.3220.167 Safari/537.1 Edge/10.63051',
			  'Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.0; WOW64 Trident/7.0)',
			  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_6_8; en-US) AppleWebKit/601.2 (KHTML, like Gecko) Chrome/51.0.3147.379 Safari/534',
			  'Mozilla/5.0 (Linux; Linux x86_64) Gecko/20100101 Firefox/71.7',
			  'Mozilla/5.0 (Windows; U; Windows NT 10.4; WOW64; en-US) AppleWebKit/536.31 (KHTML, like Gecko) Chrome/49.0.2512.385 Safari/536',
			  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_8) Gecko/20130401 Firefox/47.6',
			  'Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_5; like Mac OS X) AppleWebKit/533.41 (KHTML, like Gecko)  Chrome/54.0.3436.128 Mobile Safari/537.5',
			  'Mozilla/5.0 (Windows; Windows NT 6.0;) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/55.0.3446.330 Safari/535',
			  'Mozilla/5.0 (Windows NT 10.3; Win64; x64; en-US) Gecko/20100101 Firefox/51.7',
			  'Mozilla/5.0 (Windows NT 10.3; WOW64) AppleWebKit/533.45 (KHTML, like Gecko) Chrome/47.0.1714.391 Safari/601.7 Edge/17.57282',
			  'Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA MOTO G Build/LPH223) AppleWebKit/537.3 (KHTML, like Gecko)  Chrome/55.0.3464.271 Mobile Safari/602.1',
			  'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_9; like Mac OS X) AppleWebKit/601.14 (KHTML, like Gecko)  Chrome/47.0.3187.394 Mobile Safari/600.3',
			  'Mozilla/5.0 (Windows; Windows NT 10.2; x64) AppleWebKit/536.22 (KHTML, like Gecko) Chrome/50.0.1670.333 Safari/602.5 Edge/15.27404',
			  'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-A700I Build/LMY47X) AppleWebKit/533.48 (KHTML, like Gecko)  Chrome/48.0.3857.298 Mobile Safari/535.4',
			  'Mozilla/5.0 (Linux; U; Android 4.4.1; Nexus_S_4G Build/GRJ22) AppleWebKit/537.27 (KHTML, like Gecko)  Chrome/54.0.2776.396 Mobile Safari/535.3',
			  'Mozilla/5.0 (Windows NT 6.3; x64) Gecko/20100101 Firefox/51.5',
			  'Mozilla/5.0 (Linux; Linux i575 ; en-US) Gecko/20100101 Firefox/60.1',
			  'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_3; like Mac OS X) AppleWebKit/535.31 (KHTML, like Gecko)  Chrome/55.0.1143.252 Mobile Safari/602.9']

class Amazon:
	global useragents
	def __init__(self, dbg=False):
		self.amazon_link = 'https://www.amazon.co.uk'
		self.debug = dbg

	def getMaxPagesBySearchText(self, text, minprice=None, maxprice=None):
		if minprice:
			if type(minprice) == int:
				minprice = str(minprice)
		if maxprice:
			if type(maxprice) == int:
				maxprice = str(maxprice)
		link = self.amazon_link + '/s?k=' + text.replace(' ', '+')
		if minprice and maxprice:
			link = link + f'&rh=p_36%3A{minprice}00-{maxprice}00'
		#r = requests.get(link, headers={'User-Agent':'Defined'})
		ur = urllib.request.Request(link)
		uagent = random.choice(useragents)
		ur.add_header('User-Agent', str(uagent))
		r = urllib.request.urlopen(ur).read()
		sp = bs(r, 'lxml')
		navbar = sp.find('span', class_='s-pagination-strip')
		maxpages = None
		temp = navbar.find_all('span', {'class': ['s-pagination-item', 's-pagination-disabled'], 'aria-disabled': 'true'})
		for x in temp:
			if x.svg == None:
				maxpages = x
		temp = None
		if maxpages:
			return int(maxpages.text)
		else:
			return 1

	def getMaxPagesBySearchLink(self, link, minprice=None, maxprice=None):
		if minprice:
			if type(minprice) == int:
				minprice = str(minprice)
		if maxprice:
			if type(maxprice) == int:
				maxprice = str(maxprice)
		if minprice and maxprice:
			link = link + f'&rh=p_36%3A{minprice}00-{maxprice}00'
		#r = requests.get(link, headers={'User-Agent':'Defined'})
		ur = urllib.request.Request(link)
		uagent = random.choice(useragents)
		ur.add_header('User-Agent', str(uagent))
		r = urllib.request.urlopen(ur).read()
		sp = bs(r, 'lxml')
		navbar = sp.find('span', class_='s-pagination-strip')
		maxpages = None
		temp = navbar.find_all('span', {'class': ['s-pagination-item', 's-pagination-disabled'], 'aria-disabled': 'true'})
		for x in temp:
			if x.svg == None:
				maxpages = x
		temp = None
		if maxpages:
			return int(maxpages.text)
		else:
			return 1

	def getSearchResultFromText(self, text, minprice=None, maxprice=None, page=None):
		if minprice:
			if type(minprice) == int:
				minprice = str(minprice)
		if maxprice:
			if type(maxprice) == int:
				maxprice = str(maxprice)
		if page:
			if type(page) == int:
				page = str(page)
		link = self.amazon_link + '/s?k=' + text.replace(' ', '+')
		if minprice and maxprice:
			link = link + f'&rh=p_36%3A{minprice}00-{maxprice}00'
		if page:
			link = link + f'&page={page}'
		#r = requests.get(link, headers={'User-Agent':'Defined'})
		ur = urllib.request.Request(link)
		uagent = random.choice(useragents)
		ur.add_header('User-Agent', str(uagent))
		r = urllib.request.urlopen(ur).read()
		sp = bs(r, 'lxml')
		navbar = sp.find('span', class_='s-pagination-strip')
		items = sp.find_all('div', {'data-component-type': 's-search-result'})
		results = []
		for x in items:
			try:
			    nameparent = x.find('div', {'class': ['a-section', 'a-spacing-none puis-padding-right-small', 's-title-instructions-style'], 'data-cy': 'title-recipe'})
			    nameparent2 = nameparent.find('h2', {'class': ['a-size-mini', 'a-spacing-none', 'a-color-base', 's-line-clamp-2']})
			    link = nameparent2.find('a', {'class': ['a-link-normal', 's-underline-text', 's-underline-link-text', 's-link-style', 'a-text-normal']})['href']
			    name = nameparent2.find('span', {'class': ['a-size-medium', 'a-color-base', 'a-text-normal']})
			    priceparent = x.find('span', class_='a-price')
			    price = priceparent.find('span', class_='a-offscreen')
			    results.append({'price': price.text, 'itemname': name.text,  'link': self.amazon_link + link})
			    if self.debug:
			    	print(name.text, price.text, self.amazon_link + link)
			except: 
				pass
		return results

	def getSearchResultFromLink(self, link, minprice=None, maxprice=None, page=None):
		if minprice:
			if type(minprice) == int:
				minprice = str(minprice)
		if maxprice:
			if type(maxprice) == int:
				maxprice = str(maxprice)
		if page:
			if type(page) == int:
				page = str(page)
		if minprice and maxprice:
			link = link + f'&rh=p_36%3A{minprice}00-{maxprice}00'
		if page:
			link = link + f'&page={page}'
		#r = requests.get(link, headers={'User-Agent':'Defined'})
		ur = urllib.request.Request(link)
		uagent = random.choice(useragents)
		ur.add_header('User-Agent', str(uagent))
		r = urllib.request.urlopen(ur).read()
		sp = bs(r, 'lxml')
		items = sp.find_all('div', {'data-component-type': 's-search-result'})
		results = []
		for x in items:
			try: 
			    nameparent = x.find('div', {'class': ['a-section', 'a-spacing-none puis-padding-right-small', 's-title-instructions-style'], 'data-cy': 'title-recipe'})
			    nameparent2 = nameparent.find('h2', {'class': ['a-size-mini', 'a-spacing-none', 'a-color-base', 's-line-clamp-2']})
			    link = nameparent2.find('a', {'class': ['a-link-normal', 's-underline-text', 's-underline-link-text', 's-link-style', 'a-text-normal']})['href']
			    name = nameparent2.find('span', {'class': ['a-size-medium', 'a-color-base', 'a-text-normal']})
			    priceparent = x.find('span', class_='a-price')
			    price = priceparent.find('span', class_='a-offscreen')
			    results.append({'price': price.text, 'itemname': name.text, 'link': self.amazon_link + link})
			    if self.debug:
			    	print(name.text, price.text, self.amazon_link + link)
			except:
				pass
		return results

	def getItemResult(self, link):
		#r = requests.get(link, headers={'User-Agent': 'Defined'})
		ur = urllib.request.Request(link)
		uagent = random.choice(useragents)
		ur.add_header('User-Agent', str(uagent))
		r = urllib.request.urlopen(ur).read()
		sp = bs(r, 'lxml')
		item_frame = sp.find('div', {'id': 'centerCol', 'class': 'centerColAlign'})
		if item_frame == None:
			sp = bs(r, 'lxml')
			item_frame = sp.find('div', {'id': 'centerCol', 'class': 'centerColAlign'})
		reviewparent = item_frame.find('span', {'data-action': 'acrStarsLink-click-metrics'})
		priceparentparent = item_frame.find('div', {'id': 'apex_desktop'})
		priceparent = None
		temp = priceparentparent.find('div', {'id': 'corePrice_desktop'})
		if temp:
		    priceparent = temp
		else:
		    temp = priceparentparent.find('div', {'id': 'corePriceDisplay_desktop_feature_div'})
		    if temp:
		        priceparent = temp
		temp = None
		currentprice = None
		wasprice = None
		saveprice = None
		topreviews = []
		if priceparent['id'] == 'corePrice_desktop':
		    for prc in priceparent.find_all('td', {'class': ['a-color-secondary', 'a-size-base', 'a-text-right', 'a-nowrap']}):
		        if prc.text == 'Was:':
		            temp = prc.parent.find('span', {'class': ['a-price', 'a-text-price', 'a-size-base']})
		            temp = temp.find('span', class_='a-offscreen')
		            wasprice = temp.text
		        if wasprice == None:
		        	if prc.text == 'RRP:':
		        		temp = prc.parent.find('span', {'class': ['a-price', 'a-text-price', 'a-size-base']})
		        		temp = temp.find('span', class_='a-offscreen')
		        		wasprice = temp.text
		        if wasprice == None:
		        	if prc.text == 'New price:':
		        		temp = prc.parent.find('span', {'class': ['a-price', 'a-text-price', 'a-size-base']})
		        		temp = temp.find('span', class_='a-offscreen')
		        		wasprice = temp.text
		        if prc.text == 'Price:':
		            temp = prc.parent.find('span', {'class': ['a-price', 'a-text-price', 'a-size-medium', 'apexPriceToPay']})
		            temp = temp.find('span', class_='a-offscreen')
		            currentprice = temp.text
		        if prc.text == '  You Save: ':
		            temp = prc.parent.find('span', {'class': ['a-price', 'a-text-price', 'a-size-base']})
		            temp = temp.find('span', class_='a-offscreen')
		            saveprice = temp.text
		elif priceparent['id'] == 'corePriceDisplay_desktop_feature_div':
		    temp = priceparent.find('span', {'class': ['a-price', 'aok-align-center', 'reinventPricePriceToPayMargin', 'priceToPay']})
		    temp = temp.find('span', {'aria-hidden': 'true'})
		    currentprice = temp.text
		temp = sp.find('div', {'id': 'reviewsMedley'})
		#temp = temp.find('div', {'class': ['a-row', 'cm_cr_grid_center_container']})
		temp = temp.find('span', {'data-hook': 'cr-widget-FocalReviews'})
		#temp = temp.find('div', class_='a-row')
		reviewsparent = sp.find('div', {'id': 'cm-cr-dp-review-list'})
		for rv in reviewsparent.children:
			temp = rv.find('span', {'data-hook': 'review-body'})
			temp = temp.find('div', {'data-hook': 'review-collapsed'})
			rvtext = temp.find('span')
			profilename = rv.find('span', class_='a-profile-name')
			topreviews.append({'name': profilename.text, 'review': rvtext.text})
			temp = None
		temp = None
		reviewcount = reviewparent.find('span', {'class': ['a-size-base', 'a-color-base']})
		if self.debug:
		    print(reviewcount.text, wasprice, currentprice, saveprice)
		return {'rating': reviewcount.text.replace(' ', ''), 'wasprice': wasprice, 'currentprice': currentprice, 'saveprice': saveprice, 'topreviews': topreviews}

if __name__ == '__main__':
	# Run this file for the test code below to run
	# Importing this file in another file wont run this below
	amazon = Amazon()
	result = amazon.getSearchResultFromText('phone', 10, 20)
	result2 = amazon.getMaxPagesBySearchText('phone', 10, 20)
	print(result, result2)