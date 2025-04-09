class Solver:
    
    def __init__(self, num_disks, game_state):
        
        self.game_state = game_state
        self.num_disks = num_disks
        self.move_count = 0
        self.solve()

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
        result = []

        if self.num_disks % 2 == 0:
            pole_2, pole_3 = pole_3, pole_2

        total_moves = (2 ** self.num_disks) - 1
        poles = { '1': list(range(self.num_disks, 0, -1)), '2': [], '3': [] }

        for move in range(1, total_moves + 1):
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
            result.append([origin_pole,destination_pole])
        
        return result

# ----------------------------------------

    def move_disk(self ,game_state ,origin_pole, destination_pole):
        """Moves the disks from the given origin pole to the given destination pole"""

        if len(game_state[destination_pole]) == 0:
            game_state[destination_pole].append(game_state[origin_pole].pop())
            move_count += 1
            return game_state

        elif game_state[origin_pole][-1] < game_state[destination_pole][-1]:
            game_state[destination_pole].append(game_state[origin_pole].pop())
            move_count += 1
            return game_state

        else:
            pass


    def check_win(self,game_state):
        """Checks if all the disks are on the destination pole"""
        if game_state["3"] == list(range(self.num_disks, 0, -1)):
            return True
        else:
            return False


    def dict_to_tuple(dict_game_state):
        """Converts dictionary to tuple of tuples
            
            we do this so we can add the game state to the 'visited' variable
            that is a set and we can only add a hashable item to it
        """
        return tuple((pole, tuple(dict_game_state[pole])) for pole in sorted(dict_game_state))


    def convert_to_instruction(path=list):
        """Converts the 'path' variable that is a list of dicts
            that are the game states"""


    def possible_move_generator(game_state=dict):
        """Generates the possible moves from the given game state"""
        
        possible_moves = []
        # TODO: Calculating and finding the possible moves
        return possible_moves


    def BFS_solve(self):
        """BFS(Breadth-First Search) that works 
            when the disk are NOT in the starting position"""
        
        game_state = self.game_state
        queue = [game_state]
        visited = set()
        path = []

        while queue:
             
            if self.check_win(game_state):
                self.convert_to_instruction(path)
            
            elif self.dict_to_tuple(game_state) not in visited:
                for possible_move in self.possible_move_generator(game_state):
                    if (self.dict_to_tuple(possible_move) not in visited) and (possible_move not in queue):
                        queue.append(possible_move)
                
                visited.add(self.dict_to_tuple(game_state))
                queue.pop[0]
            
                game_state = queue[0]
            
        

# ----------------------------------------

# solver = Solver(3, {"1":[3, 2, 1], "2":[], "3":[]})
# result = solver.solve()
# print(result)




