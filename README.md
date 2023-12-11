# spot-it-generator
Program to generate an arbitary "Spot It!" like deck.

## About the game
The game of "Spot It!" (https://www.spotitgame.com/games/spot-it-classic/) is a game where you take a pair of cards from the deck, you show it to all the players, and the first person to guess the matching symbol wins.
This deck has the property of.
- Every two pairs of cards have a unique symbol.

The deck consist of 55 cards and 57 symbols. Every card has 8 symbols.

The game is also known as _Dobble_ in Europe (https://www.dobblegame.com/en/games/dobble-classic/) .

This program generates a generalized version of this game, generealized as follows. We say that the size of the _game_ is the number of symbols per card. 
The "Spot It!" game has size 8. Then, the generalized version of this game is a deck with cards of _n_ symbols.

The construction of the generalized game itself is based on MOLS (Mutually Ortogonaly Latin Squares). For more details about the algorithm visit
the following link (in spanish) [spot-it-algorithm.pdf](./spot-it-algorithm.pdf)

# Usage
```bash
python3 main.py
```
