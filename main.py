import numpy as np
import random
import os
import time
from utils import *
from genome import Genome
# Training in a square matrix for simplification 

# ---------------------



width_height = 20
goal_pos = [2, 19] 
player_pos = [9, 1]

mutation_rate = 0.1
population_size = 50
max_moves = manhattan_dist(goal_pos, player_pos) + 2

max_gen = 100

# ---------------------


def main():

   # -------------------------
   # Initialization of population
   population = []
   for i in range(0, population_size):
      population.append(Genome(max_moves, player_pos, mutation_rate))
   # -------------------------


   # -------------------------
   # Selection 
   top_fit_gen = 0
   top_ai_gen = None

   generation = 1

   while max_gen > generation:

      for pop in population:
         pop.calculate_fitness(goal_pos)
         if top_fit_gen < pop.fitness:
            
            top_fit_gen = pop.fitness
            top_ai_gen = pop
            print(f"{pop.pos}: {pop.fitness}, {top_ai_gen.pos}: {top_ai_gen.fitness}")

      mating_pool = []
      for pop in population:
         for i in range(0, int(pop.fitness * 1000)):
            mating_pool.append(pop)

      
      for i in range(0, population_size):
         parent_a = top_ai_gen
         parent_b = random.choice(mating_pool)

         child = parent_a.crossover(parent_b)

         child.mutate()
         population[i] = child

      top_ai_gen_pos = player_pos.copy()

      for move in top_ai_gen.moves:
         for i in range(width_height):
            for j in range(width_height):
               if (top_ai_gen_pos[0] == i and top_ai_gen_pos[1] == j):

                  print("P", end="")
               elif (goal_pos[0] == i and goal_pos[1] == j):
                  print("O", end="")
               else:
                  print("*", end="")
            print("\n")
         
         time.sleep(1)
         os.system('cls')
         top_ai_gen_pos[0] += move.value[0]
         top_ai_gen_pos[1] += move.value[1]

      
      generation += 1
      if (top_fit_gen == 1):
         break
   # -------------------------

if __name__ == "__main__":
   
    main()