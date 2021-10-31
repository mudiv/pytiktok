import requests,webbrowser,json
class Tikvideo:
	def tiktok(self,url,Type):
		self.urlV =requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={url}&key=godownloader.com").json()
		try: 		
			self.link=self.urlV["video_no_watermark"]
			self.res=json.loads('{"ok":"true","link":"'+self.link+'","rights": "@ruks3 : @DIBIBl"}')			
			self.daw = requests.get(self.link).content
			with open(f"/sdcard/pytiktok-ruks.mp4", 'wb') as f:
				f.write(self.daw)
				f.flush()			
			if Type ==True:
				webbrowser.open(self.link)
		except: 
			self.res =json.loads('{"ok":"false","error":"There is an error in the link","message":"You can contact us via Telegram @ruks3 ,@DIBIBl"}')			
		return self.res 