from tkinter import *
import tkinter.messagebox as messagebox

class TowerOfHanoi:
	def __init__(self):
		self.poles = {"1": [], "2": [], "3": []}
		self.disks = []
		self.num_disks = len(self.poles) * 2 - 1
		self.initialize_game()
		self.window = None
		self.status_label = None
		self.selected_pole_1 = ""
		self.selected_pole_2 = ""
		self.GUI()
		
	def GUI(self):
		def submit_pole_1():
			self.selected_pole_1 = entry.get()
			if self.selected_pole_1 not in self.poles.keys():
				self.show_message("Invalid pole number")
			elif len(self.poles[self.selected_pole_1]) == 0:
				self.show_message("No disk on the selected pole")
			else:
				self.show_message(f"Selected pole {self.selected_pole_1}")
				entry.delete(0, END)
   		
		def submit_pole_2():
			self.selected_pole_2 = entry.get()
			if self.selected_pole_2 not in self.poles.keys():
				self.show_message("Invalid pole number")
			else:
				entry.delete(0, END)
				self.move_disk()

		self.window = Tk()
		self.window.geometry("1080x780")
		self.window.title("Tower of Hanoi")
		
		entry = Entry(self.window, font=("Arial", 50))
		entry.pack()
		
		submit_pole_1_button = Button(self.window, text="Submit your original pole", command=submit_pole_1)
		submit_pole_2_button = Button(self.window, text="Submit your destination pole", command=submit_pole_2)
		
		submit_pole_2_button.pack()
		submit_pole_1_button.pack()
		
		# Add a status label to display messages
		self.status_label = Label(self.window, text="Game status will appear here", font=("Arial", 14))
		self.status_label.pack()
		
		# Display initial state
		self.update_poles_display()
		
		self.window.mainloop()
	
	def show_message(self, message):
		if self.status_label:
			self.status_label.config(text=message)
		self.update_poles_display()
		
	def update_poles_display(self):
		# Update the display of poles
		poles_text = f"Pole 1: {self.poles['1']}\nPole 2: {self.poles['2']}\nPole 3: {self.poles['3']}"
		
		try:
			if hasattr(self, 'poles_display'):
				self.poles_display.config(text=poles_text)
			else:
				self.poles_display = Label(self.window, text=poles_text, font=("Arial", 12))
				self.poles_display.pack()
		except:
			pass
	
	def initialize_game(self):
		# Initializing disks
		for i in range(self.num_disks, 0, -1):
				self.disks.append(i)
		
		# Putting the disks on pole number 1
		self.poles["1"] = self.disks
		# Disks are numbered from 1 - n(disks) from small to big
		# Default is that all the disks are on pole 1 
		# And the destination pole is pole 3
		# The first value(0) of a disk is the highest disk on the pole 	

	def move_disk(self):  
		if len(self.poles[self.selected_pole_2]) == 0:
			self.poles[self.selected_pole_2].append(self.poles[self.selected_pole_1].pop())
			self.show_message(f"Moved disk from pole {self.selected_pole_1} to pole {self.selected_pole_2}")
			if self.check_win():
				return
		elif self.poles[self.selected_pole_1][-1] < self.poles[self.selected_pole_2][-1]:
			self.poles[self.selected_pole_2].append(self.poles[self.selected_pole_1].pop())
			self.show_message(f"Moved disk from pole {self.selected_pole_1} to pole {self.selected_pole_2}")
			if self.check_win():
				return
		else:
			self.show_message("Invalid move")

	def check_win(self):
		if self.poles["3"] == [5, 4, 3, 2, 1]:
			self.show_message("You won!")
			messagebox.showinfo("Congratulations", "You won the game!")
			return True
		else:
			return False
 
# Create an instance of the game in Python
game = TowerOfHanoi()
print(game.disks)