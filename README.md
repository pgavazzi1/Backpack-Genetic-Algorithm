# Backpack-Genetic-Algorithms
* Comp 131
* By Patrick Gavazzi (pgavaz01)



## Assignment Questions:

1. For this Genetic Algorithm, each individual will a backpack that has a weight, a genome (which is a collection of boxes), and a fitness value. The fitness value will be the sum of the importance values of all boxes that are included in that specific backpack. Each generation, there will be a set of backpacks that will make children by culling 50% of the pop.
    
2. Genome will be a series of an array of ordered pairs. The first item in each pair will be a binary number telling the program if the element is included in the function or not (where a 1 means the  corresponding box included and a 0 means it is not). The second item in the ordered pairs will be the box object itself.
    
3. Fringe Operations: I used two a Fringe operations to make a new population...
                          
- I first used a one-point crossover to make a new backpack that was a mix of two parents. I made the crossover point be  somewhere within the middle of the individual so that new backpack was a better mix of the two parents. I also randomly removed boxes from the backpack's genome if it weight exceeded 250
                            
- I also used a Multi-point mutation on some individuals based on a random chance. Once again, I would only add the mutation to the genome if the total weight would not exceed 250 
    
    
    
## Acknowledgments:

I used the following website to help me implment mergesort: https://www.educative.io/edpresso/merge-sort-in-python
    

## Files:

backpackGenetics.py: contains the implmentation for the genetic algorithm, as well as functions that set up the problem and two classes for boxes and backpacks.
    
backpackGenetics_tests.py: Contains some unit tests on the functions in the genetic algorithm and its setup





## Run: 

To run the gentic algorithm, run:
    
        python backpackGenetics.py
     
Then specify the number of individuals you want to be in the search population by entering a value from 20-100. After that, the program will print out some details about the initial population and the first search in the gentic algorithm. 
    
After each step of the gentic algorithm, there will be details printed out about the top 5 individuals in the population as well as the average  fitness for an individual in the population. You can either continue the search for another round or quit out of the simulation.
    
Program will end automatically once we reach an individual with fitness 44.





## Asumptions/Comments:

I made the corss over point be within the range 1 - 10. This is because the genome has index's 0-11, so I aleast wanted each child to have 
      
For each subsequent population, I kept the best n individuals out of the combined existing population and the newly generated (and possibly mutated) children 

I used a Multi-point Mutation instead of a single-point one since it helps keep the generations diverse and also helps get algorthim unstuck if it keeps spitting out the same local maximum
      
I ended the search once we found an individual with fitness 44 and weight 250 because that is the most maximized individual we can creat during the search.
      
The algorithm is not optimal, so sometimes will get stuck on 


## Testing:  
    
1) I wrote some unit test in the file backpackGenetics_tests.py, run it to see messages printed out telling you how operations were preformed. Run with:
       
           python backpackGenetics_tests.py
