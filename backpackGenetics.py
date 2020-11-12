# =============================================================================
# 
# backpackGenetics.py
# hw 4, COMP131
# Fall 2020
#
# Simulates a genetic algorithm on a population of backpack to find what the
# best arrangment of boxes within that backpack would be. 
# 
# =============================================================================

import random

#################### Classes #######################

class Box:
    
    # function name: constructor
    # Parameters: An int representing the box's weight and another int 
    #             representing the box's importance value
    # Does: Gives the box a weight and an importance value
    def __init__(self, box_weight, box_importance) :
        
    
        self.weight       = box_weight
        self.importance   = box_importance
        
        
class Backpack:    
    
    # function name: constructor
    # Parameters: An list of ordered pairs the represents the genome of out
    #             problem and an int with the box's total weigth
    # Returns: nothing
    # Does: Gives the Backpack a genome of boxe's, set's it's fitness
    #       value to 0, and also gives it a weight
    def __init__(self, box_list, sum_weight) :
        
        self.genome      = box_list
        self.fit_value   = 0
        self.weight      = sum_weight 












#####################  Genetic Algoritm Search  #####################


# function name: fitness_func
# Parameters: a list that contains the population of backpacks 
# Returns: nothing
# Does: Goes through each value in the given population and callculates it's
#       fitness total by adding up the importance values of all of the boxes
#       in a backpack
def fitness_func( pop ):
    
    for individual in pop:
        
        # Make sure to rest it every time we calculate fitness to take into 
        # Account any mutations
        individual.fit_value == 0
        
        # Add up all of the importance values of boxes in the backpack
        for i in range (0, 12):
            if individual.genome[i][0] == 1:
                individual.fit_value += individual.genome[i][1].importance
        

# function name: mergesort
# Parameters: An unsorted sorted list of the populations
# Returns: A sorted list of the populations
# Does: Preforms merg sort on a population of backpacks based on their 
#       importance values
def mergesort( pop ):

    # Base case, skip steps and return if the population is only a single 
    # element
    if len(pop) > 1:
        mid_index = len(pop) // 2
        
        # Recuse 
        left_pop = mergesort( pop[ 0:mid_index ] )
        right_pop = mergesort( pop[ mid_index:len(pop) ] )
        
        # Base case if list are empty
        if  left_pop == None and right_pop == None:
            return 

        r = 0
        l = 0
        remaining = 0
        
        # Iterate over the lists
        for i in range (0, ( len(left_pop) + len(right_pop) ) ):
            
            # Makr sure we stay in bounds
            if r == len(right_pop) or l == len(left_pop):
                remaining = i
                break 
            
            # Add next item in lists
            if left_pop[l].fit_value > right_pop[r].fit_value:
                pop[i] = left_pop[l]
                l += 1
            else:
                pop[i] = right_pop[r]
                r += 1
        
        # Add all the remaining values in which ever list still has items 
        # left
        while l < len(left_pop):
            pop[remaining] = left_pop[l]
            l += 1
            remaining += 1
        while r < len(right_pop):
            pop[remaining] = right_pop[r]
            r += 1
            remaining += 1
            
    return pop



# function name: reproduce
# Parameters: two backpack opjects that will be the parents of the new 
#             individual
# Returns: A new back pack child
# Does: Picks a random pivot point between index's 1 and 8 to use as a 
#       crossover point to take genes from bothe parents
def reproduce( parent_1, parent_2):
   
    # Start the crossover somewhere in the middle of the gene
    cross_point = random.randint ( 1 , 10 )
    
    child_genome = crea_boxes()
    sum_weight   = 0
    
    # Make new child of two parents
    for x in range( 0, 12):
        if x < cross_point:
            child_genome[x][0] = parent_1.genome[x][0]
        else:
            child_genome[x][0] = parent_2.genome[x][0]
        
        #  Calculate the childrens weight 
        if child_genome[x][0] == 1:
            sum_weight += child_genome[x][1].weight

    # Random pick genom's to help decrease weight if child is over 250 weight
    while sum_weight > 250:
        decrease_point = random.randint ( 0 , 11 )
        if child_genome[decrease_point][0] == 1:
            child_genome[decrease_point][0] = 0
            sum_weight -= child_genome[decrease_point][1].weight
    
    # print(sum_weight)
    return Backpack( child_genome, sum_weight )
 
    
 
# function name: select_parents
# Parameters: A lust of acceptiable parent backpack objects to pick from
# Returns: an pair of backpack objects
# Does: Randomly picks two backpack objects to return and makes sure they
#       are not the same object
def select_parents( parents ):
    
    parent_1 = random.randint ( 0 , len(parents) - 1 )
    parent_2 = random.randint ( 0 , len(parents) - 1 )
        
    # Make sure we select different index's for parents
    while parent_1 == parent_2:
        parent_2 = random.randint ( 0 , len(parents) - 1 )
    
    return  [ parents[parent_1], parents[parent_2] ]



# function name: culling
# Parameters: an unsorted population of backpack objects
# Returns: the top 50% of backpack objects to make children from
# Does: Sorts a population and returns a list with the top 50% of individuals
def culling( pop ):
    
    # Sort based on fitness function and get top 50% of parents to make kids
    mergesort( pop )
    mid_index = len(pop) // 2
    
    # available_parents = start_pop[0:start_pop]
    available_parents = []
    for x in range( 0,mid_index ):
        available_parents.append( pop[x] )
    
    return available_parents




# function name: single_mutation
# Parameters: a backpack object
# Returns: nothing
# Does: Choses a point in the backpack genome to mutate into including or 
#       excluding a box
def single_mutation( backpack ):
    mutation_point = random.randint ( 0 , 11 )
    
    # Remove a box if it is in the backpack
    if backpack.genome[mutation_point][0] == 1:
        backpack.genome[mutation_point][0] = 0
        backpack.weight -= backpack.genome[mutation_point][1].weight
        
    # Include the box if it is not in the backpack yet
    if backpack.genome[mutation_point][0] == 0:
        if backpack.weight + backpack.genome[mutation_point][1].weight < 250:
            backpack.genome[mutation_point][0] = 1
            backpack.weight += backpack.genome[mutation_point][1].weight
        
    
    
# function name: genetic_alg
# Parameters: a starting populations
# Returns: a final sorted population based off of fitness value that is a 
#          combination of our starting population and the children that were
#          made during the genetic algorithm
# Does: Creats children from the top 50% of parents by single point 
#       crossover, mutates the child based on a random chance, and 
def genetic_alg( start_pop )  :
    
    new_pop = []
    available_parents = culling( start_pop )
    
    # Make as many children as there are individuals in current pop
    for i in range( 0, len(start_pop) ):
        curr_parents = select_parents( available_parents )
        child = reproduce( curr_parents[0], curr_parents[1])
        
        # Preform a multi point mutation on 3 different spots if the chance 
        # comes up
        if 1 == random . randint (1 , 25):
            single_mutation( child )
            single_mutation( child )
            single_mutation( child )

        new_pop.append(child)
     
    # Give fitness values to the new pop and combine the two pop then sort 
    # and return the best n individuals. 
    fitness_func( new_pop )
    end_pop = start_pop + new_pop  
    mergesort( end_pop )
    
    return end_pop
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#####################  Problem Start-up  #####################


# function name: crea_initial_pop
# Parameters: a int with the number of individuals to include in our pop
# Returns: an initial population
# Does: 
def crea_initial_pop( pop_lev ) :
    
    print('\n\n\nINITIAL POPULATION:')
    
    init_pop = []
    
    # Create as many backpacks as specified by user
    for x in range( 0, pop_lev ):
        init_pop.append( crea_backpack( ) )
    
    # Give fitness values and sort inital pop
    fitness_func( init_pop )
    mergesort( init_pop )
    
    # Print out state of current pop
    print_best_individs( init_pop )
    print_fitness( init_pop )

        
    return init_pop



# function name: crea_backpack
# Parameters: None
# Returns: a new backpack object
# Does: Creates a backpack by initialzing a genome of boxes and adds a box to 
#       that backpack based on a 1/15 chance (as long as the backpack does not
#       reach weight over 250)
def crea_backpack():
    
    new_genome = crea_boxes()
    
    # Randomly include some back_packs by switching their binary value , also
    # make sure weight does not exceed 250
    sum_weight = 0
    for x in range( 0, 12 ):
        chance = random . randint (1 , 50)
        if chance == 1 and (sum_weight + new_genome[x][1].weight) < 250 :
            new_genome[x][0] = 1
            sum_weight += new_genome[x][1].weight
            
     
    new_individual = Backpack( new_genome, sum_weight )
     
     
    return new_individual



# function name: crea_boxes
# Parameters: none
# Returns: A genome for the box population
# Does: creates the genome for a back pack
def crea_boxes() :
    
    box_1   = Box( 20 , 6 )
    box_2   = Box( 30 , 5 )
    box_3   = Box( 60 , 8 )
    box_4   = Box( 90 , 7 )
    box_5   = Box( 50 , 6 )
    box_6   = Box( 70 , 9 )
    box_7   = Box( 30 , 4 )
    box_8   = Box( 30 , 5 )
    box_9   = Box( 70 , 4 )
    box_10  = Box( 20 , 9 )
    box_11  = Box( 20 , 2 )
    box_12  = Box( 60 , 1 )
    
    genome = [ [0,box_1], [0,box_2], [0,box_3], [0,box_4], 
               [0,box_5], [0,box_6], [0,box_7], [0,box_8], 
               [0,box_9], [0,box_10], [0,box_11],[0,box_12] ]
    
    return genome
      
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
#####################  Functions that get input and print info  #####################


# function name: get_input
# Parameters: none
# Returns: 'search' if the user wants to search again, 'quit' if they want 
#          to stop the genetic algorithm
# Does: Get's user input on if they want to see another round of the genetic
#       algorithm
def get_input():
    
    # Get input for puzzle and make sure it is correct
    print('\n\n     Would you like to run another generation?') 
    puzzle_diffculty = input('     (search/quit): ')
    correct_response = False
    
    while correct_response == False:
        if puzzle_diffculty == 'search' :
            return 'search'
        elif puzzle_diffculty == 'quit' :
            return 'quit'
        else :
            puzzle_diffculty = input('     Please enter valid input?'
                                     '\n     (search/quit): ')
            continue
        correct_response = True



# function name: get_pop_level
# Parameters: none
# Returns: an int with a user specified population level
# Does: Ask the user for a population level until they give one in the
#       correct range
def get_pop_level():
    
    #get a battery level from the user
    print('\n\n\n\nHow much individuals would you like in the population?')
    User_pop_lev = input('Enter an interger from 20 to 100 please: ')
    
    got_correct_number = False
    while not  got_correct_number:
    
        # Run checks to make sure that first the input is a integer
        if isinstance(User_pop_lev, str) and not User_pop_lev.isdigit():
            print('\n\nThe population level', User_pop_lev, 'is not an int.'
                  ' Please try again and enter a number this time!')
            User_pop_lev = input('Enter an interger from 20 to 100 please: ')
            continue
        
    
        # Convert to an integer and make sure it is in the correct range
        User_pop_lev = int(User_pop_lev)
        if User_pop_lev < 20 or User_pop_lev > 100:
            print('\n\nThe population level:', User_pop_lev, 'Does not fit' 
                  ' into the valid range of 20-100 for this genetic algorithm'
                  ', please try again.')
            User_pop_lev = input('Enter an interger from 20 to 100 please: ')
            continue 

        got_correct_number = True
    return User_pop_lev
   
    
   
# function name: print_best_individs
# Parameters: a population of backpacks in sorted order by fitness value
# Returns: nothing
# Does: prints info about top five backpack objects in the current population
def print_best_individs( pop ):
    
    print ('\nTop five individuals:')
    print ('(Rank 1) fitness:',pop[0].fit_value , 'and weight:',
           pop[0].weight )
    print ('(Rank 2) fitness:',pop[1].fit_value , 'and weight:',
           pop[1].weight )
    print ('(Rank 3) fitness:',pop[2].fit_value , 'and weight:',
           pop[2].weight )
    print ('(Rank 4) fitness:',pop[3].fit_value , 'and weight:',
           pop[3].weight )
    print ('(Rank 5) fitness:',pop[4].fit_value , 'and weight:',
           pop[4].weight )



# function name: print_fitness
# Parameters: a population of backpacks in sorted order by fitness value, and     
# Returns: nothing
# Does: prints the average fitness value for the 
def print_fitness( pop ):
    
    fitness_sum = 0
    for x in range(0, len(pop) ):
        fitness_sum += pop[x].fit_value
        
    fitness_sum = fitness_sum / len(pop)
        
        
    print ('\nAverage Fitness Level:', fitness_sum)
     










     
#####################  Main Function  #####################

# function name: main
# Parameters: none
# Returns: nothing
# Does: Calls function that creat initial population, then prints out 
#       useful informationand and calls functions that preforn the genetic
#       algorithm
if __name__ == "__main__":

    print('\n\n\nHI THERE! Welcome to the Backpack Genetic Algorithm program!') 
    
    
    # Set up initial population
    pop_lev = get_pop_level()
    init_pop = crea_initial_pop( pop_lev )
    
    # Set up variable for search
    curr_pop   = init_pop
    fitness_func( curr_pop )
    command    = 'search'
    num_search = 1
    
    print('\n\n\nSTARTING SEARCH:')
    # Run user sepcified number of generationd
    while command == 'search':
        
        print ('\n\n\n SEARCH #', num_search)
        next_pop = genetic_alg( curr_pop )
        
        # Check if we have found the greatest individual there can be and end
        # search
        if next_pop[0].fit_value == 44:
            print ('\nFound Best individual there can be with fitness:',
                   next_pop[0].fit_value , 'and weight:',next_pop[0].weight )
            break
        
        # Change the next pop to the current one by carrying on the  
        # best half of the next_pop generation's population
        curr_pop = []
        for x in range( 0, pop_lev ):
            curr_pop.append(next_pop[x])
        
        # Print info about current generation
        print_best_individs( curr_pop )
        print_fitness( curr_pop )
        
        # Get user input and set up for next generation by carrying on the  
        # best half of the current generations population
        command  = get_input()
        num_search += 1
    
      
    print("\n\n\nAll done now, have a great day!")
    print("\n\n\n\n\n\n")
    
