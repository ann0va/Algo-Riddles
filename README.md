# Algo-Riddles
 Program that simply outputs which cats have hats at the end

## Task 

**You have 100 cats**

One day you decide to arrange all your cats in a giant circle. 
Initially, none of your cats have any hats on. 
You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

    In The first round, you stop at every cat, placing a hat on each one.
    In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
    In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
    You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat). 

Write a program that simply outputs which cats have hats at the end.

***Optional: Make a function that can calculate hats with any amount of rounds and cats.***
 


## Pseudocode

~~~
function getCatsWithHat(numCats, rounds):
    // Initialize a list catsArr with numCats elements, all set to False
    catsArr = [False] * numCats

    // Loop through each round from 1 to rounds
    for step in range(1, rounds+1):
        // For each round, loop through the cats using a step of round
        for catInd in range(step, numCats+1, step):
            // Toggle the hat status of the cats at the respective indices
            // If the cat's index is divisible by the current round, change its hat status from False to True, or vice versa
            catsArr[catInd-1] = not catsArr[catInd-1]

    // Create a new list hatsOnCats that contains the indices of cats (1-indexed) with hats (having True hat status)
    hatsOnCats = []
    for ind from 0 to numCats-1:
        if catsArr[ind] is True:
            hatsOnCats.append(ind+1)

    // Return the hatsOnCats list
    return hatsOnCats

// Call the getCatsWithHat function with arguments 100 (numCats) and 100 (rounds)
result = getCatsWithHat(100, 100)

// Print the result
print(result)
~~~

## Complexity of the algorithm 

The complexity of the algorithm is O(n * m), where n is the number of cats (numCats), and m is the number of rounds (rounds).


    
