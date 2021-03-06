# MidtermProject
# Game of Life
The Game of Life, also known simply as life, is a cellular automaton developed by the British mathematician Conway in 1970. This is a 0 player game, which means that its evolution is determined by its initial state, requiring no further input. A person interacts with the Game of Life, creating an initial configuration and watching how it develops. It is Turing complete and can simulate a universal constructor or any other Turing machine.

# Rules
The place of action of this game - the "universe" - is a surface or plane marked into cells - boundless,
bounded, or closed (in the limit, an infinite plane).

The distribution of living cells at the beginning of the game is called the first generation.

Each cell on this surface can be in two states: to be "alive" (filled)
or be "dead" (empty). A cell has eight neighbors surrounding it.

Each next generation is calculated based on the previous one according to the following rules:

    - in an empty (dead) cell, next to which there are exactly three living cells, life is born;
    - if a living cell has two or three living neighbors, then this cell continues to live;
    - otherwise, if there are less than two or more than three neighbors, the cell dies (“from loneliness”
    - or "from overcrowding")
    
The game ends if

    - not a single "living" cell will remain on the field
    - the configuration at the next step will exactly (without shifts and turns) repeat itself on
    - one of the earlier steps (there is a periodic configuration)
    - at the next step, none of the cells changes its state (a stable configuration is formed;
    - previous rule, degenerated to one step back)

The player does not directly participate in the game, but only arranges or generates the initial configuration of "live" cells,
which then interact according to the rules already without his participation (he is an observer).

# Screenshots
![gameoflifescreen2](https://user-images.githubusercontent.com/102854080/162586180-f735876f-6927-4f71-a522-b6dc1f796b19.png)
![gameoflifescreen1](https://user-images.githubusercontent.com/102854080/162586221-b2a195dc-3465-4853-aceb-b6437d1271d9.png)
![tkintergameoflife](https://user-images.githubusercontent.com/102854080/162618682-1a343254-e025-4e79-9026-82d6be6dd18c.png)



