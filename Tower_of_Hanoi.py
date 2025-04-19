import tkinter as tk
import tkinter.messagebox as messagebox
from solving_algorithms import Solver
from game_state import GameState

class TowerOfHanoi:
	"""This is the main class that the game runs on"""

	def __init__(self):
		self.move_count = 0	# Moves count
		self.poles = {"1": [], "2": [], "3": []}	# Stores poles and the disks on them
		self.num_disks = 4	# Number of disks that are going to be in the game
		self.get_disk_nums_window = None	# The first window that pops up and gets the number of disk from the user
		self.window = None	# The main window
		self.error_window = None # Error window 
		self.canvas = None	# The canvas that the game is shown on
		self.status_label = None	# Shows the events of the game on the main window under the speed slider
		self.origin_pole = ""	# The pole that we are going to take a disk from
		self.desetination_pole = ""	# The pole that we are going to put the taken disk on
		self.mouse_click_count = 0	# Mouse click count to choose if it is the origin or destination pole that is being selected
		self.animation_speed = 1500	# Speed of the animation
		self.colors = ["purple","blue","cyan","green","yellow","orange","red"]	# Colors for disks
		self.disk_height = 20 # Default height of all the disks
		self.error = False # Error checker
		
		self.getting_num_of_disks_GUI()	# Running the game

# ----------------------------------------

	def initialize_disks(self):
		"""Initializing and putting the disks on the poles"""

		for i in range(self.num_disks, 0, -1):
			self.poles["1"].append(i)
	
# ----------------------------------------
	
	def getting_num_of_disks_GUI(self):
		"""Running the first window to get them numver of disks"""

		self.get_disk_nums_window = tk.Tk()
		msg = tk.Message(self.get_disk_nums_window, text="Enter the number of disks to be in the game: ",width=300)
		first_entry = tk.Entry(self.get_disk_nums_window, font=("Arial", 50))
		msg.pack(pady=10)
		first_entry.pack()
		self.get_disk_nums_window.title("Tower of Hanoi")

		def submit_num_of_disks_func():
			"""Submitting the number of disks"""

			try:
				self.num_disks = int(first_entry.get())
				if self.num_disks in range(1,8):
					self.get_disk_nums_window.destroy()
					self.initialize_disks()
					self.GUI()
				else:
					self.get_disk_nums_window.destroy()
					self.getting_num_of_disks_GUI()
			except:
					self.get_disk_nums_window.destroy()
					self.getting_num_of_disks_GUI()

		# Submit button setup
		submit_num_of_disks_button = tk.Button(self.get_disk_nums_window,text="Submit",command=submit_num_of_disks_func)
		submit_num_of_disks_button.pack(pady=10)
		
		self.get_disk_nums_window.mainloop()

# ----------------------------------------

	def restart(self):
		"""Restarts the game"""

		self.window.destroy()
		TowerOfHanoi()

# ----------------------------------------				
	
	def raise_error(self, error=str):
		"""Raises an error widnow"""
		def exit_button_func():
			self.window.destroy()
			self.error_window.destroy()

		self.error_window = tk.Tk()
		self.error_window.title("Error!!")

		error_msg = tk.Message(self.error_window, text=error)
		error_msg.pack()
		
		error_msg_2 = tk.Message(self.error_window, text="This probably happened because you moved the disks and then pushed the 'Auto Solve' button.", width="400")
		error_msg_2.pack()

		exit_button = tk.Button(self.error_window, text="Exit", command=exit_button_func)
		exit_button.pack()

		restart_button = tk.Button(self.error_window, text="Restart", command=self.restart)
		restart_button.pack()

		self.error_window.mainloop()

# ----------------------------------------	

	def GUI(self):
		"""The main window that the game runs on"""
		
		# Window setup and parameters
		self.window = tk.Tk()
		self.window.geometry("1280x1024")
		self.window.title("Tower of Hanoi")
		
		# Create canvas for graphical representation
		self.canvas = tk.Canvas(self.window, width=800, height=400, bg="white")
		self.canvas.pack(pady=20)

		def auto_solve():
			"""Auto solve function that gets the 'result' list from the 'solving_algorithm.py' and solves the game"""
			# 'result' variable is a list of list that have 2 numbers: 
			# The first one is the origin pole and the second one is the destionation
			#
			# ATTENTION: The Auto Solve method is NOT garanteed to work if the disks have been moved!
	
			if self.error == True:
				self.raise_error(None)
			
			else:
				auto_solve_game_state = GameState(self.num_disks)
				auto_solve_game_state.poles = [self.poles["1"], self.poles["2"], self.poles["3"]]
				solver = Solver(self.num_disks, auto_solve_game_state)
				result = solver.solve()
				
				def perform_move(index):
						"""A function that performes moves based on the 'result' that is a list of moves"""
						
						if index < len(result):

							if self.error:
								self.raise_error(None)
							else:
								try:
									self.origin_pole = str(result[index][0] + 1)
									self.desetination_pole = str(result[index][1] + 1)
									self.move_disk()
									self.window.after(self.animation_speed, perform_move, index + 1)	
									self.animation_speed = slider.get() * 100
									self.check_win()
								
								except Exception as error:
									self.raise_error(error)
							
				perform_move(0)  # Start the first move
				
			
		# Auto solve button setup	
		auto_solve_button = tk.Button(self.window, text="Auto Solve", command=auto_solve)
		auto_solve_button.pack(pady=5)

		# Restart button setup
		restart_button = tk.Button(self.window, text="Restart", command=self.restart)
		restart_button.pack(pady=5)
		
		# Slider massage 
		slider_msg = tk.Message(self.window, text="Speed of the animation:", width=300)
		slider_msg.pack()

		# Slider setup
		slider = tk.Scale(self.window, from_=20, to=1, orient="horizontal", showvalue=0)
		slider.pack()
		slider.set(20)


		def mouse_click(event):
			"""Mouse click event function"""

			# Cheking if the click is on the canvas
			if 140 <= event.y <= 400 and 130 <= event.x <= 670:
				self.mouse_click_count += 1	
				
				if self.mouse_click_count % 2 != 0:
					# Selecting pole_1 as the origin pole
					if 130 <= event.x <= 270:
						self.origin_pole = "1"
						if self.origin_pole not in self.poles.keys():
							self.show_message("Invalid pole number")
						elif len(self.poles[self.origin_pole]) == 0:
							self.show_message("No disk on the selected pole")
						else:
							self.show_message(f"Selected pole {self.origin_pole}")

					
					# Selecting pole_2 as the origin pole		
					elif 330 <= event.x <= 470:
						self.origin_pole = "2"
						if self.origin_pole not in self.poles.keys():
							self.show_message("Invalid pole number")
						elif len(self.poles[self.origin_pole]) == 0:
							self.show_message("No disk on the selected pole")
						else:
							self.show_message(f"Selected pole {self.origin_pole}")

					
					# Selecting pole_3 ans the origin pole
					elif 530 <= event.x <= 670:
						self.origin_pole = "3"
						if self.origin_pole not in self.poles.keys():
							self.show_message("Invalid pole number")
						elif len(self.poles[self.origin_pole]) == 0:
							self.show_message("No disk on the selected pole")
						else:
							self.show_message(f"Selected pole {self.origin_pole}")
				
					#TODO: adding the drag and drop method

				# ----------------------------------------
				
				else: 
					# Selecting pole_1 as destination pole
					if 130 <= event.x <= 270:
						self.desetination_pole = "1"
						if self.desetination_pole not in self.poles.keys():
							self.show_message("Invalid pole number")
						else:
							self.move_disk()
					
					
					# Selecting pole_2 as destionation pole
					elif 330 <= event.x <= 470:
						self.desetination_pole = "2"
						if self.desetination_pole not in self.poles.keys():
							self.show_message("Invalid pole number")
						else:
							self.move_disk()
					
					
					# Selecting pole_3 as destionation pole
					elif 530 <= event.x <= 670:
						self.desetination_pole = "3"
						if self.desetination_pole not in self.poles.keys():
							self.show_message("Invalid pole number")
						else:
							self.move_disk()
					
					self.check_win() # After each move we check if the game is won or not

	
		# Binding the mouse click event to the window
		self.window.bind("<Button-1>",mouse_click)
	
		# Adding a status label to display messages
		self.status_label = tk.Label(self.window, text="Game status will appear here", font=("Arial", 14))
		self.status_label.pack(pady=10)

		# Display initial state
		self.update_poles_text_status()
		self.draw_game()

		self.window.mainloop()
	
# ----------------------------------------

	def show_message(self, message):
			"""Shows the status massage"""

			if self.status_label:
				self.status_label.config(text=message)

			
			self.update_poles_text_status()
			self.draw_game()
		
# ----------------------------------------

	def update_poles_text_status(self):
		"""Updates the pole status that is shown on the main window"""
		
		poles_text = f"Pole 1: {self.poles['1']}\nPole 2: {self.poles['2']}\nPole 3: {self.poles['3']}"
		
		try:
			if hasattr(self, 'poles_display'):
				self.poles_display.config(text=poles_text)
			else:
				self.poles_display = tk.Label(self.window, text=poles_text, font=("Arial", 12))
				self.poles_display.pack()
		except:
			pass

# ----------------------------------------

	def draw_disk(self,disk_size,x,y):
		"""Draws the disks"""

		# Calculate disk dimentions
		width = 25 + disk_size * 15

				
		# Draw disk
		self.canvas.create_rectangle(
			x - width/2, y - self.disk_height,
			x + width/2, y,
			fill=self.colors[disk_size-1]
		)

		# Add text label showing disk size
		self.canvas.create_text(
			x, y - self.disk_height/2,
			text=str(disk_size),
			fill="black",
			font=("Arial", 10, "bold")
		)

# ----------------------------------------

	def draw_game(self):
		"""Drawing the main game on the canvas"""

		if self.canvas:
			# Clear canvas
			self.canvas.delete("all")
   
			# Draw the count of the moves
			self.canvas.create_text(
				400, 50,
				text=f"Moves: {self.move_count}",
				fill="black",
				font=("Arial", 20, "bold")
			)
			
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
					self.draw_disk(disk_size, x=pole_x[pole_i],y = y_base - (i + 1) * self.disk_height)
					
					
# ----------------------------------------

	def move_disk(self):
		"""Moves disk from the origin to the destination pole"""  

		if len(self.poles[self.desetination_pole]) == 0:
			self.poles[self.desetination_pole].append(self.poles[self.origin_pole].pop())
			self.show_message(f"Moved disk from pole {self.origin_pole} to pole {self.desetination_pole}")
			self.move_count += 1

		elif self.poles[self.origin_pole][-1] < self.poles[self.desetination_pole][-1]:
			self.poles[self.desetination_pole].append(self.poles[self.origin_pole].pop())
			self.show_message(f"Moved disk from pole {self.origin_pole} to pole {self.desetination_pole}")
			self.move_count += 1

		else:
			self.show_message("Invalid move")
			self.error = True
		
		self.draw_game()	# Update the graphic

# ----------------------------------------

	def check_win(self):
		"""Checks if all the disks are on the destination pole"""

		if self.poles["3"] == list(range(self.num_disks, 0, -1)):
			self.show_message("Game won!")
			self.window.update_idletasks()
			messagebox.showinfo("Congratulations", "Game won!")
			self.window.after(1000,self.window.destroy())
			return True
		else:
			return False
 
towerofHanoi = TowerOfHanoi()	# Create an instance of the game in Python
