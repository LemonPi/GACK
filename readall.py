import os
import pickle
from bs4 import BeautifulSoup

def processOne(fil, allplants):
	bs = BeautifulSoup(fil, 'html.parser')

	plantinfo = {}
	plantinfo["name"] = bs.find(class_="contenttitleh1").text
	plantinfo["common"] = bs.find(class_="contenttitlecommonh2").text
	plantinfo["plantnum"] = bs.find(class_="contenttitleplantnumberh3").text.replace("Plant number: ", "")
	plantinfo["usda"] = bs.find(class_="usdatext").text.replace("USDA Zone: ", "")
	plantinfo["desc"] = bs.find(class_="contentdesc").text

	detailstable = bs.find("table", width="390")
	therow = detailstable.find_all("tr")[2]
	thecell = therow.find("td")
	dahtmlstr = [a.strip() for a in str(thecell).split('<div class="smallspace4"></div>')]
	cats = [a[a.find("<strong>") + len("<strong>"):a.find("</strong>")] for a in dahtmlstr]
	values = [[b.strip() for b in BeautifulSoup(a[a.find("</strong") + len("</strong>"):], "html.parser").text.replace("\xa0", " ").split(" or")] for a in dahtmlstr]
	conditions = {}
	for i in range(len(cats)):
		catname = cats[i]
		valueset = values[i]
		conditions[catname] = valueset
	plantinfo["cond"] = conditions
	char = {}
	thecell = therow.find_all("td")[1]
	dahtmlstr = [a.strip() for a in str(thecell).replace("<br><br><strong>Growth Rate</strong>", '<div class="smallspace4"></div><strong>Growth Rate</strong>').split('<div class="smallspace4"></div>')]
	cats = [BeautifulSoup(a[a.find("<strong>") + len("<strong>"):a.find("</strong>")], "html.parser").text for a in dahtmlstr]
	values = [[BeautifulSoup(b, "html.parser").text.replace("\xa0", "").strip() for b in a[a.find("</strong") + len("</strong>"):].split("<br>")] for a in dahtmlstr]
	values = [[a for a in b if not a == ""] for b in values]
	for i in range(len(cats)):
		catname = cats[i]
		valueset = values[i]
		char[catname] = valueset
	plantinfo["char"] = char

	allplants.append(plantinfo)

def main():
	files = os.listdir("plants")
	allplants = []
	i = 0
	for f in files:
		if i % 10 == 0:
			print(i)
		if not f.endswith(".html"):
			continue
		with open("plants/" + f, "rb") as fil:
			processOne(fil.read(), allplants)
		i += 1
	with open("allplants.bin", "wb") as outfile:
		pickle.dump(allplants, outfile)

if __name__ == "__main__":
	main()
