import amazonlib

# Initialize amazon scrape lib
# For debugging use Amazon(dbg=True)
amz = amazonlib.Amazon()

'''
Searching for items
getSearchResultFromText(
 text=str,		(for example 'Samsung Galaxy S24')
 minprice=int,	(for example 0)
 maxprice=int,	(for example 100)
 page=int		(for example 5)
) -> returns list of jsons, each json contains price, itemname and link. get by calling jsonResult['price']/['itemname']/['link']

getSearchResultFromLink(
 link=str,		(for example 'https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Android-Smartphone/dp/B09QH3JT6P')
 minprice=int,	(for example 0)
 maxprice=int,	(for example 100)
 page=int 		(for example 5)
) -> returns list of jsons, each json contains price, itemname and link. get by calling jsonResult['price']/['itemname']/['link']

Getting info of an item
getItemResult(
 link=str		(for example 'https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Android-Smartphone/dp/B09QH3JT6P')
) -> returns a json which contains rating, wasprice, currentprice, saveprice and topreviews (where topreviews is a list containing jsons, each json contains name and review)

Getting max page for search result
getMaxPagesBySearchText(
 text=str,		(for example 'Samsung Galaxy S24')
 minprice=int,	(for example 0)
 maxprice=int,	(for example 100)
) -> returns int. get max pages of a specific search

getMaxPagesBySearchLink(
 link=str,		(for example 'https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Android-Smartphone/dp/B09QH3JT6P')
 minprice=int,	(for example 0)
 maxprice=int,	(for example 100)
) -> returns int. get max pages of a specific search

example usage:
amazon = amazonlib.Amazon()
itemlink = 'https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Android-Smartphone/dp/B09QH3JT6P'
searchlink = 'https://www.amazon.co.uk/s?k=Samsung+Phone'
=========================== Getting search result from text
amazon.getSearchResultFromText('samsung phone', 5, 100)		<- search text, minimum price, max price
amazon.getSearchResultFromText('samsung phone', page=5)		<- setting search text and page only without min/max price
amazon.getSearchResultFromText('samsung phone', 5, 100, 5)	<- search text, min and max price, page
=========================== Getting search result from link
amazon.getSearchResultFromLink(searchlink, 5, 100)		<- search link, minimum price, max price
amazon.getSearchResultFromLink(searchlink, page=5)		<- setting search link and page only without min/max price
amazon.getSearchResultFromLink(searchlink, 5, 100, 5)		<- search link, min and max price, page
=========================== Getting max pages
amazon.getMaxPagesBySearchText('samsung phone', 5, 100)		<- search text, minimum price, max price
amazon.getMaxPagesBySearchLink(searchlink, 5, 100)				<- search link, min and max price
=========================== Getting item info
amazon.getItemResult(itemlink)

example script:
import amazonlib
amz = amazonlib.Amazon()

search = 'Samsung Phone'
maxpages = amz.getMaxPagesBySearchText(search)
for x in range(maxpages):
	searchresult = amz.getSearchResultFromText(search, page=x)
	for item in searchresult:
		print(item['itemname'], item['price'], item['link'])
		iteminfo = amz.getItemResult(item['link'])
		print(iteminfo['rating'], iteminfo['wasprice'], iteminfo['currentprice'], iteminfo['saveprice'], iteminfo['topreviews'])

'''

search = 'Samsung Phone'
maxpages = amz.getMaxPagesBySearchText(search)
phoneresult = amz.getSearchResultFromText(search, page=5)
print(phoneresult[0]['itemname'])