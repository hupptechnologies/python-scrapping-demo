
import requests
import bs4
import json
import os;

# Url prefix
_URL = 'https://www.flipkart.com'

# Set url which need to scrap
res = requests.get(_URL+"/search?q=watches&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2&as-pos=0&as-type=RECENT&as-searchtext=wa&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DFossil");
type(res);

## Load site data in `lxml` format
soup = bs4.BeautifulSoup(res.text,'lxml')

## Filename
filename = 'data/details.json';
checkExist = os.path.exists(filename);
if checkExist is False:
	f = open(filename, "a");
	json.dump([], f, indent=4)
	f.close()

## Open file & load json data in watches variable
with open(filename, 'r+') as f:
	watches = json.load(f);


## Set blank array for watches variable
watches = []

## Fetch all data of give class name
loops = soup.select('._3O0U0u._288RSE');

## Iterate all array which comes from website
for x in loops:
	y = x.select('._2LFGJH')
	obj = {};
	for yTitle in y:
		# Product title
		title = yTitle.select('._2B_pmu')
		obj['title'] = title[0].text;
		# Product type
		productType = yTitle.select("a._2mylT6")
		obj['productType'] = productType[0].text

		price = yTitle.select('._1vC4OE');
		obj['price'] = price[0].text
		watches.append(obj)
	

nextLink = soup.select('._3fVaIS');
print(nextLink[0]['href'])

## Remove old file
os.remove(filename)
## Open new file in `write` mode.
with open(filename, 'w') as f:
    json.dump(watches, f, indent=4)

## Close open file.
f.close()


print("SCARPPING COMPLETE");