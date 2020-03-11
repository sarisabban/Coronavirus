import sys
import bs4
import time
import datetime
from urllib import request

logo = '''\033[31m╔═╗┌─┐┬─┐┌─┐┌┐┌┌─┐┬  ┬┬┬─┐┬ ┬┌─┐
║  │ │├┬┘│ ││││├─┤└┐┌┘│├┬┘│ │└─┐
╚═╝└─┘┴└─└─┘┘└┘┴ ┴ └┘ ┴┴└─└─┘└─┘
\033[34m╔╦╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
 ║ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
 ╩ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─
\033[33m--------------------------------\033[0m'''

def Coronavirus(country):
	''' Tracks the global coronavirus cases and deaths '''
	# Global Cases
	URL = 'https://www.worldometers.info/coronavirus/'
	web = request.urlopen(URL).read().decode('utf8')
	soup = bs4.BeautifulSoup(web, 'lxml')
	title = soup.find('title').string
	cases = title.split()[3]
	deaths = title.split()[6]
	time = datetime.datetime.now().strftime('%d %B %Y @ %H:%M')
	print('{}\n    Total Global Cases:  \033[1;34m{}\033[0m\n    Total Global Deaths: \033[31m{}\033[0m'\
		.format(time, cases, deaths))
	# Country Cases
	URL = 'https://www.worldometers.info/coronavirus/#countries'
	web = request.urlopen(URL).read().decode('utf8')
	soup = bs4.BeautifulSoup(web, 'lxml')
	table = soup.find("table")
	body = table.find('tbody')
	rows = body.find_all('tr')
	country = country.title()
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		if cols[0] == country:
			if cols[2] == '': new       = 0
			else: new       = cols[2]
			if cols[1] == '': cases     = 0
			else: cases     = cols[1]
			if cols[3] == '': deaths    = 0
			else: deaths    = cols[3]
			if cols[6] == '': active    = 0
			else: active    = cols[6]
			if cols[5] == '': recovered = 0
			else: recovered = cols[5]
	try:
		out = '''    \033[1;36m{}:\033[0m\n        Total Cases         \033[1;34m{}\033[0m\n        Total Deaths        \033[31m{}\033[0m\n        New Cases           \033[35m{}\033[0m\n        Still Active Cases  \033[33m{}\033[0m\n        Total Recovered     \033[32m{}\033[0m'''\
		.format(country, cases, deaths, new, active, recovered)
		print(out)
	except:
		if country == '': pass
		else: print('No cases in {}'.format(country))
	print('----------')

def main():
	print(logo)
	while True:
		Coronavirus(' '.join(sys.argv[1:]))
		time.sleep(180)

if __name__ == '__main__': main()
