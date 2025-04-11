class Solver:
    
    def __init__(self, num_disks, game_state):
        
        self.game_state = game_state
        self.num_disks = num_disks
        self.move_count = 0
        self.state_instructions = []
        self.result = []

# ----------------------------------------    

    def is_first_state(self):
        """Checks that whether the disk are in the starting position or not"""
        
        if self.game_state["1"] == list(range(self.num_disks, 0, -1)):
            return True
        else:
            return False
   
    
    def solve(self):
        """Solver that is being called in the main program"""
        
        if self.is_first_state():
            return self.algo_solve()
            
        else:
            return self.BFS_solve()

# ----------------------------------------

    def algo_solve(self):
        """Algortihm solve that only works when the disks are all on the first pole"""
        
        pole_1, pole_2, pole_3 = '1', '2', '3'
        self.result = []

        if self.num_disks % 2 == 0:
            pole_2, pole_3 = pole_3, pole_2

        self.move_count = (2 ** self.num_disks) - 1
        poles = { '1': list(range(self.num_disks, 0, -1)), '2': [], '3': [] }

        for move in range(1, self.move_count + 1):
            if move % 3 == 1:
                if poles[pole_1] and (not poles[pole_3] or poles[pole_1][-1] < poles[pole_3][-1]):
                    origin_pole = pole_1
                    destination_pole = pole_3
                else:
                    origin_pole = pole_3
                    destination_pole = pole_1
            elif move % 3 == 2:
                if poles[pole_1] and (not poles[pole_2] or poles[pole_1][-1] < poles[pole_2][-1]):
                    origin_pole = pole_1
                    destination_pole = pole_2
                else:
                    origin_pole = pole_2
                    destination_pole = pole_1
            else:
                if poles[pole_2] and (not poles[pole_3] or poles[pole_2][-1] < poles[pole_3][-1]):
                    origin_pole = pole_2
                    destination_pole = pole_3
                else:
                    origin_pole = pole_3
                    destination_pole = pole_2

            disk = poles[origin_pole].pop()
            poles[destination_pole].append(disk)
            self.result.append([origin_pole,destination_pole])
        
        return self.result

# ----------------------------------------

    def check_win(self,game_state):
        """Checks if all the disks are on the destination pole"""
        if game_state["3"] == list(range(self.num_disks, 0, -1)):
            return True
        else:
            return False


    def dict_to_tuple(self,dict_game_state):
        """Converts dictionary to tuple of tuples
            
            we do this so we can add the game state to the 'visited' variable
            that is a set and we can only add a hashable item to it
        """
        return tuple((pole, tuple(dict_game_state[pole])) for pole in sorted(dict_game_state))


    def move_disk(self ,game_state ,origin_pole, destination_pole):
        """Moves the disks from the given origin pole to the given destination pole"""
        new_game_state = {pole: game_state[pole][:] for pole in game_state}

        if len(new_game_state[origin_pole]) != 0:
            if len(new_game_state[destination_pole]) == 0:
                new_game_state[destination_pole].append(new_game_state[origin_pole].pop())
                return new_game_state

            elif new_game_state[origin_pole][-1] < new_game_state[destination_pole][-1]:
                new_game_state[destination_pole].append(new_game_state[origin_pole].pop())
                return new_game_state


    def possible_move_generator(self, game_state=dict):
        """Generates the possible moves from the given game state"""
    
        possible_moves = []
        poles = ["1", "2", "3"]
        new_game_state = {}

        for origin in poles:
            for destination in poles:
                new_game_state = self.move_disk(game_state, origin, destination)
                if new_game_state and new_game_state not in possible_moves:
                    possible_moves.append(new_game_state)
                    self.state_instructions.append([origin,destination])
                new_game_state = None
            
        return possible_moves
    

    def instruction_extractor(self,changes_list=list):
        """Extracts the instructions from the moves the program did"""
        
        # Getting the current game state and its instruction
        current_game_state = changes_list.pop()
        current_instruction = self.state_instructions.pop()

        for i in range(0,11):
        # while current_game_state != self.game_state:
            # Giving these infos to the 'move_disk' func to redo the  
            self.move_disk(current_game_state,current_instruction[1],current_instruction[0])
            
            self.result.append([current_instruction[1],current_instruction[0]])
            print(changes_list,"\n",self.state_instructions)

        return self.result



    def BFS_solve(self):
        """BFS(Breadth-First Search) that works 
            when the disk are NOT in the starting position"""
        
        game_state = self.game_state
        queue = [game_state]
        visited = set()
        all_moves = set()
        changes_list = []

        # While queue has something it will run the BFS
        while queue:    
            
            # Poping the the current game state that is being looked on from the queue
            queue.pop(0)

            # Checking of the game is done
            if self.check_win(game_state): 
                print("GAME WON")
                return self.instruction_extractor(changes_list)
                

            # Doing the main BFS part and adding game state to the queue
            elif self.dict_to_tuple(game_state) not in visited:
                
                queue_len_before = len(queue)

                # Adding the possible moves to the queue
                for possible_move in self.possible_move_generator(game_state):
                    if (self.dict_to_tuple(possible_move) not in visited) and (possible_move not in queue):
                        queue.append(possible_move)
                        
                queue_len_after = len(queue)

                # Checking to see whether ther is a game state added to queue or not
                if queue_len_before == queue_len_after:
                    self.state_instructions.pop()
                queue_len_before, queue_len_after = 0, 0

                all_moves.add(self.dict_to_tuple(game_state))  
                print("--- all game states checked: ", len(all_moves),"---\n")
                
                # Adding the current game_state to the visisted var
                visited.add(self.dict_to_tuple(game_state))

                # Making the first one one the queue the game state so that the 
                game_state = queue[0]
                changes_list.append(queue[0])
        
        print("\n\n\n\n\n",changes_list)
        print(self.state_instructions)
        
    

        
# ----------------------------------------

solver = Solver(1, {"1":[], "2":[1], "3":[]})
result = solver.solve()
print(result)
# print(solver.BFS_solve({"1":[], "2":[2], "3":[1]}))
# print(solver.dict_to_tuple({"1":[], "2":[2], "3":[1]}))

