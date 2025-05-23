from game_state import GameState
class Solver:
    
    def __init__(self, num_disks, game_state:GameState):
        
        self.game_state = GameState(num_disks)
        self.game_state.set_values(game_state)
        self.num_disks = num_disks
        self.move_count = 0
        self.instructions = []
        self.result = []

# ----------------------------------------    

    def solve(self):
        """Solver that is being called in the main program"""
    
        if self.game_state.is_first_state():
            # Create a fresh game state to work with
            fresh_state = GameState(self.num_disks)
            fresh_state.init_first_state()
            self.game_state = fresh_state
            return self.algo_solve()
            
        else:
            return self.BFS_solve()

# ----------------------------------------

    def algo_solve(self):
        """Algortihm solve that only works when the disks are all on the first pole"""
        
        pole_1, pole_2, pole_3 = 0, 1, 2
        self.result = []

        if self.num_disks % 2 == 0:
            pole_2, pole_3 = pole_3, pole_2

        self.move_count = (2 ** self.num_disks) - 1

        for move in range(1, self.move_count + 1):
            if move % 3 == 1:
                if self.game_state.poles[pole_1] and (not self.game_state.poles[pole_3] or self.game_state.poles[pole_1][-1] < self.game_state.poles[pole_3][-1]):
                    origin_pole = pole_1
                    destination_pole = pole_3
                else:
                    origin_pole = pole_3
                    destination_pole = pole_1
            elif move % 3 == 2:
                if self.game_state.poles[pole_1] and (not self.game_state.poles[pole_2] or self.game_state.poles[pole_1][-1] < self.game_state.poles[pole_2][-1]):
                    origin_pole = pole_1
                    destination_pole = pole_2
                else:
                    origin_pole = pole_2
                    destination_pole = pole_1
            else:
                if self.game_state.poles[pole_2] and (not self.game_state.poles[pole_3] or self.game_state.poles[pole_2][-1] < self.game_state.poles[pole_3][-1]):
                    origin_pole = pole_2
                    destination_pole = pole_3
                else:
                    origin_pole = pole_3
                    destination_pole = pole_2
            
            if not self.game_state.move_disk(origin_pole, destination_pole):
                raise Exception("invalid game move in algo_solve")
            
            self.result.append((origin_pole,destination_pole))
        
        return self.result

# ----------------------------------------

    def game_state_to_tuple(self,game_state):
        """Converts dictionary to tuple of tuples
            
            we do this so we can add the game state to the 'visited' variable
            that is a set and we can only add a hashable item to it
        """
        return tuple((i,tuple(x)) for i, x in enumerate(game_state.poles))

    def BFS_solve(self):
        """BFS(Breadth-First Search) that works 
            when the disk are NOT in the starting position"""

        current_game_state = GameState(self.num_disks)
        current_game_state.set_values(self.game_state)
        queue = [current_game_state]
        visited = set()

        # While queue has something it will run the BFS
        while queue:    
            
            # Poping the the current game state that is being looked on from the queue
            current_game_state = queue[0]
            queue.pop(0)

            # Checking of the game is done
            if current_game_state.check_win(): 
                print("GAME WON")

                # Adding the current game_state to the visisted var
                visited.add(self.game_state_to_tuple(current_game_state))

                self.move_count = len(current_game_state.instructions)

                return current_game_state.instructions
                
                # return self.instruction_extractor(visited)
                

            # Doing the main BFS part and adding game state to the queue
            elif self.game_state_to_tuple(current_game_state) not in visited:
                
                # Adding the current game_state to the visisted var
                visited.add(self.game_state_to_tuple(current_game_state))
                
                # Adding the possible moves to the queue
                for possible_move in current_game_state.possible_move_generator():
                    if (self.game_state_to_tuple(possible_move) not in visited) and (possible_move not in queue):
                        queue.append(possible_move)

    
        
# ----------------------------------------

# game_state = GameState(5)
# game_state.init_first_state()
# # game_state.move_disk(0,2)
# solver = Solver(5, game_state)
# result = solver.solve()
# print(result)
# print(len(result))

