import tkinter as tk
import tkinter.messagebox as messagebox
from solving_algorithm import solving

class TowerOfHanoi:
	def __init__(self):
		self.count = 0	# moves count
		self.poles = {"1": [], "2": [], "3": []}	# stores poles and the disks on them
		self.num_disks = 4	# the number of disks that are going to be in the game
		self.get_disk_nums_window = None	# the first window that pops up and gets the number of disk from the user
		self.window = None	# the main window that everything is on it
		self.canvas = None	# the canvas that the game is shown on
		self.status_label = None	# shows the events of the game on the main window under the speed slider
		self.selected_pole_1 = ""	# the pole that we are going to take a disk from
		self.selected_pole_2 = ""	# the pole that we are going to put the taken disk on
		self.mouse_click_count = 0	# mouse click count to choose if it is the origin or destination pole that is being selected
		self.animation_speed = 1500	# speed of the animation
		self.colors = ["purple","blue","cyan","green","yellow","orange","red"]	# colors for disks
		self.getting_num_of_disks_GUI()

	def initialize_game(self):
		# Initializing disks
		for i in range(self.num_disks, 0, -1):
			self.poles["1"].append(i)
	

	# getting the number of disks that are going to be in the game from the user
	def getting_num_of_disks_GUI(self):
		self.get_disk_nums_window = tk.Tk()
		msg = tk.Message(self.get_disk_nums_window, text="Enter the number of disks to be in the game: ",width=300)
		first_entry = tk.Entry(self.get_disk_nums_window, font=("Arial", 50))
		msg.pack(pady=10)
		first_entry.pack()
		self.get_disk_nums_window.title("Tower of Hanoi")
		# submitting the number of disks
		def submit_num_of_disks():
			try:
				self.num_disks = int(first_entry.get())
				if self.num_disks in range(1,8):
					self.get_disk_nums_window.destroy()
					self.initialize_game()
					self.GUI()
				else:
					self.get_disk_nums_window.destroy()
					self.getting_num_of_disks_GUI()
			except:
					self.get_disk_nums_window.destroy()
					self.getting_num_of_disks_GUI()

		submit_num_of_disks_button = tk.Button(self.get_disk_nums_window,text="Submit",command=submit_num_of_disks)
		submit_num_of_disks_button.pack(pady=10)
		
		self.get_disk_nums_window.mainloop()
			

	def GUI(self):
		
		# auto solve button function
		def auto_solve():
			result = solving(self.num_disks)
			
			def perform_move(index):
				if index < len(result):
					self.selected_pole_1 = result[index][0]
					self.selected_pole_2 = result[index][1]
					self.move_disk()
					self.window.after(self.animation_speed, perform_move, index + 1)
					self.animation_speed = slider.get() * 100
			
			perform_move(0)  # Start the first move

		self.window = tk.Tk()
		self.window.geometry("1280x1024")
		self.window.title("Tower of Hanoi")
		
		# Create canvas for graphical representation
		self.canvas = tk.Canvas(self.window, width=800, height=400, bg="white")
		self.canvas.pack(pady=20)

		auto_solve_button = tk.Button(self.window, text="Auto Solve", command=auto_solve)
		slider = tk.Scale(self.window, from_=1, to=20, orient="horizontal")
		slider_msg = tk.Message(self.window, text="Speed of the animation:", width=300)
		# mouse click function
		def mouse_click(event):
			# cheking if the click is on the canvas
			if 140 <= event.y <= 400 and 130 <= event.x <= 670:
				self.mouse_click_count += 1
				if self.mouse_click_count % 2 != 0:
					# selecting pole_1 as the origin pole
					if 130 <= event.x <= 270:
						print("pole_1 selected as selected_pole_1",event.x)
						self.selected_pole_1 = "1"
						if self.selected_pole_1 not in self.poles.keys():
							self.show_message("Invalid pole number")
						elif len(self.poles[self.selected_pole_1]) == 0:
							self.show_message("No disk on the selected pole")
						else:
							self.show_message(f"Selected pole {self.selected_pole_1}")

					# selecting pole_2 as the origin pole		
					elif 330 <= event.x <= 470:
						print("pole_2 selected as selected_pole_1",event.x)
						self.selected_pole_1 = "2"
						if self.selected_pole_1 not in self.poles.keys():
							self.show_message("Invalid pole number")
						elif len(self.poles[self.selected_pole_1]) == 0:
							self.show_message("No disk on the selected pole")
						else:
							self.show_message(f"Selected pole {self.selected_pole_1}")

					# selecting pole_3 ans the origin pole
					elif 530 <= event.x <= 670:
						print("pole_3 selected as selected_pole_1",event.x)
						self.selected_pole_1 = "3"
						if self.selected_pole_1 not in self.poles.keys():
							self.show_message("Invalid pole number")
						elif len(self.poles[self.selected_pole_1]) == 0:
							self.show_message("No disk on the selected pole")
						else:
							self.show_message(f"Selected pole {self.selected_pole_1}")
#-----------------------------------------------------------------------------------------------------------------------------------------
				else: 
					# selecting pole_1 as destination pole
					if 130 <= event.x <= 270:
						self.selected_pole_2 = "1"
						if self.selected_pole_2 not in self.poles.keys():
							self.show_message("Invalid pole number")
						else:
							self.move_disk()
					
					# selecting pole_2 as destionation pole
					elif 330 <= event.x <= 470:
						self.selected_pole_2 = "2"
						if self.selected_pole_2 not in self.poles.keys():
							self.show_message("Invalid pole number")
						else:
							self.move_disk()
					
					#selecting pole_3 as destionation pole
					elif 530 <= event.x <= 670:
						self.selected_pole_2 = "3"
						if self.selected_pole_2 not in self.poles.keys():
							self.show_message("Invalid pole number")
						else:
							self.move_disk()

			
		
		# binding the mouse click event to the window
		self.window.bind("<Button-1>",mouse_click)
		
		auto_solve_button.pack(pady=10)
		slider_msg.pack()
		slider.pack()

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
   
			# Draw the count of the moves
			self.canvas.create_text(
				400, 50,
				text=f"Moves: {self.count}",
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
					# Calculate disk dimentions
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
			self.count += 1
			if self.check_win():
				return
		elif self.poles[self.selected_pole_1][-1] < self.poles[self.selected_pole_2][-1]:
			self.poles[self.selected_pole_2].append(self.poles[self.selected_pole_1].pop())
			self.show_message(f"Moved disk from pole {self.selected_pole_1} to pole {self.selected_pole_2}")
			self.count += 1
			if self.check_win():
				return
		else:
			self.show_message("Invalid move")
		
		# Update the graphic
		self.draw_game()

	def check_win(self):
		if self.poles["3"] == list(range(self.num_disks, 0, -1)):
			self.show_message("Game won!")
			messagebox.showinfo("Congratulations", "Game won!")
			self.window.after(1000,self.window.destroy())
			return True
		else:
			return False
 
# Create an instance of the game in Python
game = TowerOfHanoi()
