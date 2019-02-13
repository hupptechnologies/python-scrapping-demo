
import requests
import bs4
import json
import os;

# Set url which need to scrap
res = requests.get("https://www.flipkart.com/search?q=watches&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2&as-pos=0&as-type=RECENT&as-searchtext=wa");
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
	

## Remove old file
os.remove(filename)
## Open new file in `write` mode.
with open(filename, 'w') as f:
    json.dump(watches, f, indent=4)

## Close open file.
f.close()


print("SCARPPING COMPLETE");