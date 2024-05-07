from utils import *
import random 

### ------------------------------------------------
# Logic:
#
# Each genome has a limited amount of moves (parametre*distance_to_goal) 
# and a distance to the goal
# 
# 
### ------------------------------------------------


class Genome():

    def __init__(self, max_moves, pos, mutation_rate):
        
        self.pos = pos
        self.initial_pos = pos
        self.moves = []

        self.fitness = 0
        self.max_moves = max_moves

        self.mutation_rate = mutation_rate

        # initiate moves
        for i in range(0, self.max_moves):
            self.moves.append(random.choice(list(Dir)))
        

    # returns fitness normalized
    def calculate_fitness(self, pos_goal):
        final_pos = self.pos.copy()

        for i in range(0, len(self.moves)):
            
            final_pos[0] = final_pos[0] + self.moves[i].value[0]
            final_pos[1] = final_pos[1] + self.moves[i].value[1]


        dist = euclidean_dist(final_pos, pos_goal)
        if dist != 0:
            self.fitness = (1/(dist))**1.5 
        else:
            self.fitness = 1
    def mutate(self):
        for i in range(0, len(self.moves)):
            if random.random() < self.mutation_rate:
                self.moves[i] = random.choice(list(Dir))
        
    def crossover(self, partner):
        child = Genome(self.max_moves, self.initial_pos, self.mutation_rate)

        midpoint = random.randint(int(self.max_moves/2 + 5), self.max_moves)
        child.moves[0:midpoint] = self.moves[0:midpoint]
        child.moves[midpoint+1:len(self.moves)] = partner.moves[midpoint+1:len(self.moves) - 1]

        return child

    def print_moves(self):
        for move in self.moves:
            print(move.value)
    
