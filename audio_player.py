import sound_lib
import url_shortener
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

