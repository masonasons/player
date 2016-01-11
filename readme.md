#Player
A command line interface to the blind twitter client built-in audio players.

Uses bits of sourcecode from TWBlue, by Manuel Cortez.
#Usage
run player.py

it asks you for a URL. Type in a valid URL, whether it be SNDUP or an audio stream.
Then, type one of these commands.

pause: Play/pause currently playing stream.

vd: decrease volume by 5 percent.

vu: Increase volume by 5 percent.

quit: Exit.

#Building
You will need the following to build Player. These can be gotten from Pip. pip install packagename

##Windows

setuptools

py2exe

type setup.py py2exe

##mac

setuptools

py2app

Type setup.py py2app