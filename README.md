# MachineGun Deck
Rapidly create decks and a passive immersion audio file with automation using [pywinauto](https://github.com/pywinauto/pywinauto) for folks using [MIA]().

MachineGun Deck is a process automation tool to quickly generate anki decks as described by Matt from [Matt vs Japan](https://www.youtube.com/user/MATTvsJapan) in this [guide](https://www.youtube.com/watch?v=h2xYKx76-9s).

Currently MachineGun Deck automates the subs2srs process and aditionally generates a passive immersion audio file as described by [this](https://www.youtube.com/watch?v=QOLTeO-uCYU).

While the Anki import, reading and accents generation and definitions generation have been automated I have not included them in the final product since currently pywinauto is undergoing changes for UIA backend applications, with the current version being very slow. However, once the next major realese of pywintauto hits I will implement this functionality. 
## Requirements
* [Mp3Cat](http://www.dmulholl.com/dev/mp3cat.html)
* [Subs2srs](https://sourceforge.net/projects/subs2srs/)
* [Anki](https://apps.ankiweb.net/)(Or any SRS of your choice, as Subs2srs only produces a .tsv file)

## Instalation
This application uses [fbs]('https://pypi.org/project/fbs/') which you will need to install to run the app (no executable is provided for the moment).
```
pip install fbs
```
* I recommend installing in a virtual enviorment to keep your workspace clean, but it's up to you. 

Then to run the app just:
```
fbs run
```

## DISCLAIMER 
I'm not affiliated with MIA in any way, this is just a solo project to help automize my sentence minning. 
