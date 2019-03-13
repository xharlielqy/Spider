import requests, json, time, sys
from contextlib import closing


class get_photos(object):
	def __init__(self):
		self.photos_id = []
		self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
		self.target = 'http://unsplash.com/napi/photos'
		self.headers = {'ugid':'????'}
	def get_ids(self):
		req = requests.get(url=self.target, headers=self.headers, verify=False)
		html = json.loads(req.text)
		for each in html:
			the_id = each['id']
			print('图片ID:',each['id'])
			self.photos_id.append(the_id)
		 #time.sleep(1)

	def download(self, photo_id, filename):
		headers = {'user-agent':'???','ugid':'???'}
		target = self.download_server.replace('xxx', photo_id)
		with closing(requests.get(url=target, stream=True, verify = False, headers = self.headers)) as r:
			with open('%d.jpg' % filename, 'ab+') as f:
				for chunk in r.iter_content(chunk_size = 1024):
					if chunk:
						f.write(chunk)
						f.flush()

if __name__ == '__main__':
	gp = get_photos()
	print('获取图片中：')
	gp.get_ids()
	print("图片下载中")
	for i in range(len(gp.photos_id)):
		print('downloading%dpicture'%(i+1))
		gp.download(gp.photos_id[i], (i+1))
