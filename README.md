# midtermproject
The place of action of this game - the "universe" - is a surface or plane marked into cells - boundless,
bounded, or closed (in the limit, an infinite plane).

The distribution of living cells at the beginning of the game is called the first generation.

Each cell on this surface can be in two states: to be "alive" (filled)
or be "dead" (empty). A cell has eight neighbors surrounding it.

Each next generation is calculated based on the previous one according to the following rules:
    * in an empty (dead) cell, next to which there are exactly three living cells, life is born;
    * if a living cell has two or three living neighbors, then this cell continues to live;
    * otherwise, if there are less than two or more than three neighbors, the cell dies (“from loneliness”
    * or "from overcrowding")
The game ends if
    * not a single "living" cell will remain on the field
    * the configuration at the next step will exactly (without shifts and turns) repeat itself on
    * one of the earlier steps (there is a periodic configuration)
    * at the next step, none of the cells changes its state (a stable configuration is formed;
    * previous rule, degenerated to one step back)

The player does not directly participate in the game, but only arranges or generates the initial configuration of "live" cells,
which then interact according to the rules already without his participation (he is an observer).
