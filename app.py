from tkinter import *
class TowerOfHanoi:
	def __init__(self):
		self.poles = {"1": [], "2": [], "3": []}
		self.disks = []
		self.num_disks = len(self.poles) * 2 - 1
		self.initialize_game()
		self.GUI()
		self.selected_pole_1 = 0
		self.selected_pole_2 = 0
		# self.get_pole_input()
		
	def GUI(self):
		def submit():
			self.selected_pole_1 = entry.get()
			print(self.selected_pole_1)
		
		window = Tk()
		window.geometry("1080x780")
		window.title("Tower of Hanoi")
		
		entry = Entry(window,font=("Arial",50))
		entry.pack()
		
		submit_button = Button(window,text="Submit your picked pole",command=submit)
		submit_button.pack()
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
		
	def get_pole_input(self):
		selected_pole_1 = input("Enter the pole you want to pick a disk from: ")
		selected_pole_2 = input("Enter the pole you want to put the disk on: ")
		if selected_pole_1 not in self.poles.keys() or selected_pole_2 not in self.poles.keys():
			print("Invalid pole number")

# Create an instance of the game in Python
game = TowerOfHanoi()
print(game.selected_pole_1)