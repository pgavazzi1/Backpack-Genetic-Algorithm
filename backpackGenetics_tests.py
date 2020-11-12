# =============================================================================
# 
# backpackGenetics_tests.py
# hw 4, COMP131
# Fall 2020
#
# Simulates unit tests on some funstions of the backpack genetic algorithm 
# search
# 
# =============================================================================

from backpackGenetics import crea_boxes
from backpackGenetics import crea_backpack
from backpackGenetics import crea_initial_pop
from backpackGenetics import print_best_individs
from backpackGenetics import mergesort
from backpackGenetics import fitness_func
from backpackGenetics import culling
from backpackGenetics import select_parents


##################### Tests  #####################

# function name: test_genome
# Parameters: none
# Returns: nothing
# Does: Makes sure all the boxes in the genome have correct weigths and 
#       importance values
def test_genome():
    
    print('\n\n\n      Let us test to make sure our basic genome is correct:')
    
    test_genome = crea_boxes()
    
    for x in range ( 0, 12 ):
        print( "box", x, "has weight: ", test_genome[x][1].weight, 
               " and importance value: ",  test_genome[x][1].importance)

# function name: test_init_pop
# Parameters: none
# Returns: a list containing the sample test population
# Does: tests to make sure that the inital pop function makes right amount of
#       individuals 
def test_init_pop():
    
    print('\n\n\n\n      Let us test to make sure our initial pop is correct:',
           end=" ")
    
    test_pop = crea_initial_pop( 30 )
    
    print( "\ninitial pop level should be 30, and it is:", end=" ")
    if len(test_pop) == 30:
        print( len(test_pop), "Which is correct" )
    else:
        print( len(test_pop), "Which is NOT Correct BOOOOOO" )
        
    return test_pop
    
        

        
        
# function name: test_mergsort
# Parameters: none
# Returns: nothing
# Does: Tests to see that merge sort sorts the regards to fitness value of 
#       individual
def test_mergsort():
    print('\n\n\n\n\n\n     Let us test to make sure mergsort is correct:')
    
    test_pop = []
    
    for x in range( 0, 20 ):
        test_pop.append( crea_backpack() )
    fitness_func( test_pop )
    
    
    print('\nBEFORE SORT', end="")
    print_best_individs( test_pop )
    
    print('\nAFTER SORT', end="")
    mergesort( test_pop )
    print_best_individs( test_pop )
        
        
        
        
# function name: test_culling
# Parameters: a list with the test population
# Returns: a list with the culled population (top 50% of test pop) 
# Does: Makes sure culling function takes highest 50% of test pop
def test_culling( test_pop ):
    print('\n\n\n\n\n      Let us test to make sure culling 50% is correct:')
    
    print('\nBEFORE CULLING 50%')
    print( "initial pop level should be 30, and it is:", end=" ")
    if len(test_pop) == 30:
        print( len(test_pop), "which is correct" )
    else:
        print( len(test_pop), "which is NOT Correct BOOOOOO" )
    
    culled_pop = culling( test_pop )
    print('\nAFTER CULLING 50%')
    print( "initial pop level should be 15, and it is:", end=" ")
    if len(culled_pop) == 15:
        print( len(culled_pop), "which is correct" )
    else:
        print( len(culled_pop), "which is NOT Correct BOOOOOO" )
        
    return culled_pop

  


# function name: test_parents_select
# Parameters: a list with the culled population (top 50% of test pop) 
# Returns: nothing
# Does: Makes sure that the select_parents function randomly picks different
#       parents from test pop
def test_parents_select( culled_pop ):
    print('\n\n\n     Let us test to make sure selecting the parents works'
          'correctly :\n')
    
    for x in range(0, 5):
        test_parents = select_parents( culled_pop )
        print( "Parent 1:", test_parents[0].fit_value, "Parent 2:", 
                test_parents[1].fit_value)
    
  
#####################  Main Function  #####################

# function name: main
# Parameters: none
# Returns: nothing
# Does: Calls function that tests aspects of genetic algorithm
if __name__ == "__main__":

    print('\n\n\nHI THERE! Welcome to the Backpack Genetic Algorithm tests!')
    
    
    test_genome()
    test_pop = test_init_pop()
    test_mergsort()
    culled_pop = test_culling( test_pop )
    test_parents_select( culled_pop )
    

    
    print("\n\n\nAll done, thanks for testing!")
    print("\n\n\n\n\n\n")