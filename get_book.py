import requests, sys
from bs4 import BeautifulSoup

"""
Download books from website.
Modify
	2019-03-11
"""
class downloader(object):
	def __init__(self):
		self.server = 'http://www.biqukan.com/'
		self.target = 'http://www.biqukan.com/1_1094/'
		self.names = [] #save title name
		self.urls = [] #save title links
		self.numbs = 0 #save title number


	def get_downloader_url(self):
		req = requests.get(url = self.target)
		html = req.text
		div_bf = BeautifulSoup(html, features='html.parser')
		div = div_bf.find_all('div', class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]), features='html.parser')
		a = a_bf.find_all('a')
		self.nums = len(a[16:])
		for each in a[16:]:
			self.names.append(each.string)
			self.urls.append(self.server + each.get('href'))


	def get_contents(self, target):
		req = requests.get(url = target)
		html = req.text
		bf = BeautifulSoup(html, features='html.parser')
		texts = bf.find_all('div', class_ = 'showtxt')
		texts = texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

	def writer(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding = 'utf-8') as f:
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')


if __name__ == '__main__':
	dl = downloader()
	dl.get_downloader_url()
	print('It begins to download')
	for i in range(dl.nums):
		dl.writer(dl.names[i], 'book.txt', dl.get_contents(dl.urls[i]))
		#sys.stdout.write("Has already download:%.3f%%" % float(i/dl.nums) + '\r')
		sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
		sys.stdout.flush()
	print('Finish')
























