import tkinter as tk
import tkinter.messagebox as messagebox

class TowerOfHanoi:
	def __init__(self):
		self.poles = {"1": [], "2": [], "3": []}
		self.num_disks = 5
		self.initialize_game()
		self.window = None
		self.status_label = None
		self.selected_pole_1 = ""
		self.selected_pole_2 = ""
		self.canvas = None
		self.colors = ["red", "orange", "yellow", "green", "blue"]  # Colors for disks
		self.GUI()
		
	def initialize_game(self):
		# Initializing disks
		for i in range(self.num_disks, 0, -1):
			self.poles["1"].append(i)
	
	def GUI(self):
		def submit_pole_1():
			self.selected_pole_1 = entry.get()
			if self.selected_pole_1 not in self.poles.keys():
				self.show_message("Invalid pole number")
			elif len(self.poles[self.selected_pole_1]) == 0:
				self.show_message("No disk on the selected pole")
			else:
				self.show_message(f"Selected pole {self.selected_pole_1}")
				entry.delete(0, tk.END)
		
		def submit_pole_2():
			self.selected_pole_2 = entry.get()
			if self.selected_pole_2 not in self.poles.keys():
				self.show_message("Invalid pole number")
			else:
				entry.delete(0, tk.END)
				self.move_disk()

		self.window = tk.Tk()
		self.window.geometry("1280x1024")
		self.window.title("Tower of Hanoi")
		
		# Create canvas for graphical representation
		self.canvas = tk.Canvas(self.window, width=800, height=400, bg="white")
		self.canvas.pack(pady=20)
		
		entry = tk.Entry(self.window, font=("Arial", 50))
		entry.pack(pady=20)
		
		submit_pole_1_button = tk.Button(self.window, text="Submit as original pole", command=submit_pole_1)
		submit_pole_2_button = tk.Button(self.window, text="Submit as destination pole", command=submit_pole_2)
		
		submit_pole_2_button.pack(pady=10)
		submit_pole_1_button.pack(pady=10)
		
		# Add a status label to display messages
		self.status_label = tk.Label(self.window, text="Game status will appear here", font=("Arial", 14))
		self.status_label.pack(pady=10)
		
		# Display initial state
		self.update_poles_display()
		self.draw_game()
		
		self.window.mainloop()
	
	def show_message(self, message):
		if self.status_label:
			self.status_label.config(text=message)
		self.update_poles_display()
		self.draw_game()
		
	def update_poles_display(self):
		# Update the text display of poles
		poles_text = f"Pole 1: {self.poles['1']}\nPole 2: {self.poles['2']}\nPole 3: {self.poles['3']}"
		
		try:
			if hasattr(self, 'poles_display'):
				self.poles_display.config(text=poles_text)
			else:
				self.poles_display = tk.Label(self.window, text=poles_text, font=("Arial", 12))
				self.poles_display.pack()
		except:
			pass

	def draw_game(self):
		if self.canvas:
			# Clear canvas
			self.canvas.delete("all")
			
			# Draw the base
			self.canvas.create_rectangle(100, 350, 700, 380, fill="brown")
			
			# Draw the poles
			pole_x = [200, 400, 600]  # x positions for the 3 poles
			for x in pole_x:
				self.canvas.create_rectangle(x-10, 150, x+10, 350, fill="gray")
			
			# Draw disks for each pole
			for pole_i, pole_num in enumerate(["1", "2", "3"]):
				x = pole_x[pole_i]
				y_base = 350  # Base y-position
				
				for i, disk_size in enumerate(self.poles[pole_num]):
					# Calculate disk dimensions
					width = 25 + disk_size * 15
					height = 20
					y = y_base - (i + 1) * height
					
					# Draw disk
					self.canvas.create_rectangle(
						x - width/2, y - height,
						x + width/2, y,
						fill=self.colors[disk_size-1]
					)
     
					# Add text label showing disk size
					self.canvas.create_text(
						x, y - height/2,
						text=str(disk_size),
						fill="black",
						font=("Arial", 10, "bold")
					)

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
		
		# Update the graphical
		self.draw_game()

	def check_win(self):
		if len(self.poles["3"]) == self.num_disks and self.poles["3"] == list(range(self.num_disks, 0, -1)):
			self.show_message("You won!")
			messagebox.showinfo("Congratulations", "You won the game!")
			return True
		else:
			return False
 
# Create an instance of the game in Python
game = TowerOfHanoi()
