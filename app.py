from tkinter import *

class TowerOfHanoi:
	def __init__(self):
		self.poles = {"1": [], "2": [], "3": []}
		self.disks = []
		self.num_disks = len(self.poles) * 2 - 1
		self.initialize_game()
		self.GUI()
		self.selected_pole_1 = ""
		self.selected_pole_2 = ""
		
	def GUI(self):
		def submit_pole_1():
			self.selected_pole_1 = entry.get()
			if self.selected_pole_1 not in self.poles.keys():
				print("Invalid pole number")
		
		def submit_pole_2():
			self.selected_pole_2 = entry.get()
			if self.selected_pole_2 not in self.poles.keys():
				print("Invalid pole number")
			self.move_disk()
   
		
		window = Tk()
		window.geometry("1080x780")
		window.title("Tower of Hanoi")
		
		entry = Entry(window,font=("Arial",50))
		entry.pack()
		
		submit_pole_1_button = Button(window,text="Submit your original pole",command=submit_pole_1)
		submit_pole_2_button = Button(window,text="Submit your destination pole",command=submit_pole_2)
		
		submit_pole_2_button.pack()
		submit_pole_1_button.pack()
		window.mainloop()

	
	def initialize_game(self):
		# Initializing disks
		for i in range(self.num_disks):
			i += 1
			self.disks.append(i)
		
		# Putting the disks on pole number 1
		self.poles["1"] = self.disks
  		# Disks are numbered from 1 - n(disks) from small to big
		# Default is that all the disks are on pole 1 
		# And the destination pole is pole 3
		# The first value(0) of a disk is the highest disk on the pole 	


	def move_disk(self):
		# Check if the move is valid
		if len(self.poles[self.selected_pole_1]) == 0:
			print("There is no disk on the selected pole")
			return
 
		if len(self.poles[self.selected_pole_2]) == 0:
			self.poles[self.elected_pole_2].append(self.poles[self.selected_pole_1].pop())
			return
 
# Create an instance of the game in Python
game = TowerOfHanoi()
print(game.poles)