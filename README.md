# LMS
League Music Switcher

Really quickly put together (like I did this in 2 hours, and it only took that long because I am NOT a GUI guy) python script to change your champ select music.  You can do this on the fly so between games, you can listen to different music in champ select.  There's a few requirements and setup steps so listen up!

### Setup and First Run

* Download and install Python3.4 for windows [here](https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi)
* Don't worry about customizing any install settings, everything should be enabled by default.
* Download lms.py, above.
* Create a directory named 'songs' in the directory that contains lms.py.
* Copy your favorite songs into this folder.
* Double click on lms.py to run it.

### Script Behavior
lms.py will attempt to do the following.  First, it will backup your old champ select music.  Then, it will parse the songs directory for all the .mp3s you placed in there.  At this point you should select ONE entry via the drop down list and click the button.  LMS will then copy your selected music file to the correct location in your league folder.  Finally, queue up and rock out during champ select.

### Troubleshooting...
Honestly if you've configured Python correctly, the only possible thing I can think of that can go wrong is either your League folder is not where lms.py expects it to be, or lms.py doesn't have permissions to write to the League folder.
