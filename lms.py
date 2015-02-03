import tkinter
import os
import shutil

CHAMP_SEL_MUSIC="C:\\Riot Games\\League of Legends\\RADS\\projects\\lol_air_client\\releases\\0.0.1.127\\deploy\\assets\\sounds\\ambient\\"
class MusicSwitcher(tkinter.Frame):
	def __init__(self, master=tkinter.Tk()):
		master.minsize(width=200, height=200)
		tkinter.Frame.__init__(self, master)
		self.var_list = []
		self.master = master
		self.parse_songs()
		self.create_widgets()

	def parse_songs(self):
		folder = ".\\songs"
		self.song_names = os.listdir(folder)
		for i in range(len(self.song_names)):
			self.var_list.append(tkinter.BooleanVar())

	def create_widgets(self):
		self.butt = tkinter.Button(self.master, command=self.on_click, width=25, text="Click me!")
		self.list = tkinter.Menubutton(self.master, text="Choose a song", relief=tkinter.RAISED)
		self.list.menu = tkinter.Menu(self.list, tearoff=0)
		self.list['menu'] = self.list.menu
		i = 0
		for song in self.song_names:
			self.list.menu.add_checkbutton(label=song, onval=True, offval=False, variable=self.var_list[i])
			i+=1
		self.butt.pack()  #Giggity
		self.list.pack()


	#Screw symlinks just copy the file!
	def on_click(self):
		for i in range(len(self.var_list)):
			if self.var_list[i].get():
				shutil.copyfile(".\\songs\\"+self.song_names[i],CHAMP_SEL_MUSIC+"ChmpSlct_DraftMode.mp3")				


ms = MusicSwitcher()
ms.master.title('League Champ Select Music Switcher')
ms.mainloop()


