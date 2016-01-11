import sound_lib
import audio_services
import audio_player
cont=0
player=audio_player.URLStream()
text=raw_input("Enter the address.")
print "Attempting to play..."
try:
	player.play(text)
except:
	print "Error. Unable to play."
	cont=1
while True:
	if cont==1:
		break
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