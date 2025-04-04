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
        
# ----------------------------------------        
    
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

    def move_disk(self, origin_pole, destination_pole):
        """Moves the disks from the given origin pole to the given destination pole"""

        if len(self.game_state[destination_pole]) == 0:
            self.game_state[destination_pole].append(self.game_state[origin_pole].pop())
            move_count += 1
            return self.game_state

        elif self.game_state[origin_pole][-1] < self.game_state[destination_pole][-1]:
            self.game_state[destination_pole].append(self.game_state[origin_pole].pop())
            move_count += 1
            return self.game_state

        else:
            pass


    def check_win(self,game_state):
        """Checks if all the disks are on the destination pole"""
        if game_state["3"] == list(range(self.num_disks, 0, -1)):
            return True
        else:
            return False


    def BFS_solve(self):
        """BFS(Breadth-First Search) that works when the disk are NOT in the starting position"""
        pass

# ----------------------------------------

# solver = Solver(3, {"1":[3, 2, 1], "2":[], "3":[]})
# result = solver.solve()
# print(result)




