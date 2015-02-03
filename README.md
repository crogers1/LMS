# LMS
League Music Switcher

Really quickly put together (like I did this in 2 hours, and it only took that long because I am NOT a GUI guy) python script to change your champ select music.  You can do this on the fly so between games, you can listen to different music in champ select.  There's a few requirements and setup steps so listen up!

### Setup and First Run

Download Python3.x for windows
Make sure your Environment variable path can find the python folder.
Download lms.py
Create a directory named 'songs' in the directory that contains lms.py
Copy your favorite songs into this folder
Open up a command prompt, navigate to the folder with lms.py in it and run it via the command:
  ```python lms.py```

### Script Behavior
lms.py will attempt to do the following.  First, it will backup your old champ select music.  Then, it will parse the songs directory for all the .mp3s you placed in there.  At this point you should select ONE entry via the drop down list and click the button.  LMS will then copy your selected music file to the correct location in your league folder.  Finally, queue up and rock out during champ select.

### Troubleshooting...
Honestly if you've configured Python correctly, the only possible thing I can of that can go wrong is your League folder is not where lms.py expects it to be, or you didn't give the script enough permissions to write to your League folder.
