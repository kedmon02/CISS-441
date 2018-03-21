import urllib.request

myzips = list()
myzips.append(['cd','https://www.walmart.com/'])
myzips.append(['zi','https://www.walmart.com/cp/electronics/3944'])
for myzipdata in myzips:

	mytype, mypageurl = myzipdata
	response = urllib.request.urlopen (mypageurl)
	html = response.read()
	print(mytype, mypageurl, html[0:100])