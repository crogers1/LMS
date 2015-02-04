# LMS
League Music Switcher

Really quickly put together (like I did this in 2 hours, and it only took that long because I am NOT a GUI guy) python script to change your champ select music.  There's a few requirements and setup steps so listen up!

### Setup and First Run

* Download and install Python3.4 for windows [here](https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi)
* For whatever reason, Python sometimes doesn't set up your environment path correctly.  It's really easy, I'll walk you through it:
* - Right click my computer -> Properties -> Advanced -> Environment Variables
* - Go to system and find the PATH (sometimes 'Path') variable and edit.
* - Go to the very end of the line (don't remove anything) and add this: ;C:\python34
* - Explanation: The semi-colon separates the entries from each other, and the remainder is just the path to your python folder.
* Download lms.py, [here] (https://raw.githubusercontent.com/crogers1/LMS/master/lms.py)
* Create a directory named 'songs' in the directory that contains lms.py.
* Copy your favorite songs into this folder.
* Double click on lms.py to run it.
* Select a song from the drop down list and click the button to copy it to your League folder.

### Script Behavior
lms.py will attempt to do the following.  First, it will backup your old champ select music.  Then, it will parse the songs directory for all the .mp3s you placed in there.  At this point you should select ONE entry via the drop down list and click the button.  LMS will then copy your selected music file to the correct location in your league folder.  Finally, queue up and rock out during champ select.

### Troubleshooting...
Honestly if you've configured Python correctly, the only possible thing I can think of that can go wrong is either your League folder is not where lms.py expects it to be, or lms.py doesn't have permissions to write to the League folder.

### Known Issues
Due to the way I assume the League client manages its music files, switching your champ select music on the fly is not possible.  Without seeing the source I can't know for sure, but here's my guess as to what's happening.  Going to try and figure out a workaround but I have little hope hahaha.

When you enter draft pick champ select for the first time, the League client will open the music file ChmpSlct_DraftMode and read it into memory (aka, 'caching').  If the file doesn't exist, it caches nothing.  Now, every time you go into draft mode, the client will play whatever music is has cached in memory, instead of trying to open the ChmpSlct file again.  So if you use the app to copy in another song without exiting the client, the client will never use that file.  This seems dumb, but it's actually not a bad design choice.  In the event you never do draft pick, no memory gets allocated for the music (saves some space).  And if all you play is draft, it only ever had to do 1 file operation (since reading from disk is expensive and slow).
