import audio_services
import cmd

import sound_lib
import audio_player
player=audio_player.URLStream()
class commandline(cmd.Cmd):
	def help_vd(self):
		print "Turns down the volume of the audio."
	def do_vd(self, line):
		if player.stream.volume<=0.1:
			print "Volume is minimum"
		else:
			player.stream.volume-=0.05
		print "Volume is now "+str(round(player.stream.volume,2))
	def help_v(self):
		print "Specify the volume manually. Range is from 0.05 to 1.0"
	def do_v(self, line):
		if float(line)<0.05 or float(line)>1.0:
			print "Number out of range"
		else:
			player.stream.volume=float(line)
		print "Volume is now "+str(round(player.stream.volume,2))
	def help_vu(self):
		print "Turns up the volume of the audio."
	def do_vu(self, line):
		if player.stream.volume>=1.0:
			print "Volume is maximum"
		else:
			player.stream.volume+=0.05
		print "Volume is now "+str(round(player.stream.volume,2))
	def help_pause(self):
		print "Pauses the audio."
	def do_pause(self, line):
		if player.stream.is_paused==False:
			player.stream.pause()
			print "Paused"
		else:
			player.stream.play()
			print "Playing"

	def do_EOF(self, line):
		return True

cont=0
player=audio_player.URLStream()
text=raw_input("Enter the address.")
print "Attempting to play..."
try:
	player.play(text)
except:
	print "Error. Unable to play."
	cont=1

if cont==0:
	commandline().cmdloop("Audio is playing. Type help for help.")