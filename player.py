import audio_services
import url_shortener
import sound_lib
output=sound_lib.output.Output()

class URLStream(object):
 def __init__(self,url=None):
  self.url = url
  self.prepared = False

 def prepare(self, url):
  self.prepared = False
  self.url = url_shortener.unshorten(url)
  if self.url != None:
   transformer = audio_services.find_url_transformer(self.url)
   self.url = transformer(self.url)
   self.prepared = True
  else:
   self.url = url
   self.prepared = True

 def play(self, url=None, volume=0.3, stream=None):
  if url != None:
   self.prepare(url)
  elif stream != None:
   self.stream=stream
  if self.prepared == True:
   self.stream = sound_lib.stream.URLStream(url=self.url)
  if hasattr(self,'stream'):
   self.stream.volume = float(volume)
   self.stream.play()

 def stop_audio(self,delete=False):
  if hasattr(self, "stream"):
   self.stream.stop()
  else:
   return False

player=URLStream()
text=raw_input("Enter the address.")
player.play(text)
while True:
	stuff=raw_input("Do what")
	if stuff=="pause":
		if player.stream.is_paused==False:
			player.stream.pause()
			print "Paused"
		else:
			player.stream.play()
			print "Playing"
	if stuff=="vu":
		if player.stream.volume>=1.0:
			print "Volume is maximum"
		else:
			player.stream.volume+=0.05
		print "Volume is now "+str(round(player.stream.volume,2))
	if stuff=="vd":
		if player.stream.volume<=0.1:
			print "Volume is minimum"
		else:
			player.stream.volume-=0.05
		print "Volume is now "+str(round(player.stream.volume,2))
	if stuff=="quit":
		break