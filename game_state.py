import copy
class GameState:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.poles = [[],[],[]]
    
    def __eq__(self, game_state):

        if self.poles == game_state.poles:
            return True
        else:
            return False
        
    def init_first_state(self):
        self.poles[0] = list(range(self.num_disks, 0, -1))
        self.poles[1], self.poles[2] = [], []
        
    def set_values(self, game_state):
        self.poles = copy.copy(game_state.poles)
        self.num_disks = game_state.num_disks

    def is_first_state(self):
        """Checks that whether the disk are in the starting position or not"""
        
        if self.poles[0] == list(range(self.num_disks, 0, -1)):
            return True
        else:
            return False
        
    def check_win(self):
        """Checks if all the disks are on the destination pole"""

        if self.pole[2] == list(range(self.num_disks, 0, -1)):
            return True
        else:
            return False
   
    def move_disk(self,origin,dest):
        if len(self.poles[origin]) == 0:
            return False
        
        elif len(self.poles[dest]) == 0:
            disk = self.poles[origin].pop()
            self.poles[dest].append(disk)
            return True

        else:
            if self.poles[origin][-1] > self.poles[dest][-1]:
                return False
            
            disk = self.poles[origin].pop()
            self.poles[dest].append(disk)
            return True

    def is_movable(self,origin, dest):
        if len(self.poles[origin]) == 0:
            return False
        
        elif len(self.poles[dest]) == 0:
            return True

        else:
            if self.poles[origin][-1] > self.poles[dest][-1]:
                return False
            
            return True


    def possible_move_generator(self):
        possible_move = []

        for origin in range(0,3):
            for dest in range(0,3):
                if origin != dest and self.is_movable(origin, dest):

                    new_game_state = GameState(self.num_disks)
                    new_game_state.set_values(self)
                    new_game_state.move_disk(origin,dest)

                    possible_move.append(new_game_state)

        return possible_move
                    
            

            
