import os
import sound_lib.stream
import sound_lib.output

output = sound_lib.output.Output()

class SoundObject(object):
 """An object to manage sounds"""
 def __init__(self):
  self.sounds = {}
  super(SoundObject, self).__init__()

 def load_sound(self, name, looping=False, play=False, pan=0, ignore_loaded=False, volume=1.0, key=None):
  if key is None:
   key = name
  if key not in self.sounds or ignore_loaded:
   filename = name
   sound = sound_lib.stream.FileStream(file=filename)
   sound.looping = looping
  else:
   sound = self.sounds[name]
  sound.pan = pan
  sound.volume = volume
  if play:
   sound.play(True)
  self.sounds[key] = sound

 def __del__(self):
  for i in self.sounds:
   self.sounds[i].stop()

 def stop_all_sounds(self):
  for i in self.sounds:
   i.stop()

 def play_all_sounds(self):
  for i in self.sounds:
   i.play()


