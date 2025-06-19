# Sun Temple

Sun Temple is a two-player Python board game created as a foundation year assessment project by James Fothergill. The game challenges players to traverse a randomly-seeded board, collecting valuable gems and avoiding glass beads, with the aim of achieving the highest score by the end of the board.

## Overview

Players take turns moving along a 40-space board, choosing moves from a limited set. Each space may contain a ruby, emerald, diamond, sapphire, or glass bead. The objective is to collect as many valuable gems as possible and minimise the number of glass beads collected. The game ends when the player counter leaves the board, and the player with the highest score wins.

## How to Play

1. Ensure you have [Python 3](https://www.python.org/downloads/) installed.
2. Download or clone the repository to your computer.
3. Open a terminal/command prompt in the project directory.
4. Run the game with:

   ```bash
   python "James Fothergill Assessment Python Gamev.py"
   ```

5. Follow the on-screen instructions to enter player names and play the game.

## Rules

- The board contains 40 spaces, randomly seeded with:
  - 7 Rubies (r)
  - 7 Emeralds (e)
  - 7 Diamonds (d)
  - 7 Sapphires (s)
  - 11 Glass beads (g)
- Players alternate turns, selecting a move value from the available set; each move value can only be used once.
- Landing on a space allows a player to collect the item present, which is added to their goody sack.
- Gems score positively, while glass beads reduce your score.
- The scoring formula for each gem type is:  
  *(number collected) / 2 × (number collected + 1)*  
  For glass beads, the score is subtracted.
- The game ends when the counter leaves the board. The player with the highest total score is the winner.

## Educational Value

This project demonstrates:
- Basic Python programming
- Lists, functions, loops, and user input
- Game logic and turn-based mechanics
- Randomisation for replayability

## Author

- James Fothergill

## Licence

This project is distributed under the GNU General Public License v3.0.  
See the [LICENSE](LICENSE) file for more details.

---

Enjoy traversing the Sun Temple, and may the best collector win!
