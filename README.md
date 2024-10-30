# Tic-Tac-Toe AI with Minimax by Delmond

This is a Tic-Tac-Toe AI developed as part of the CS50 AI course, implementing the Minimax algorithm for optimal gameplay. The AI plays as the 'O' player, making moves that minimize losses and maximize potential wins.

## Features

- **Unbeatable AI**: Implements the Minimax algorithm to ensure optimal decisions in any given game state.
- **Interactive Gameplay**: Allows you to play against the AI, experiencing dynamic, real-time decision-making.
- **Terminal-based**: Built to run directly in the terminal, providing a clean and focused gaming experience.

## Getting Started

### Prerequisites

- Python 3.x is required to run this AI.
- Basic familiarity with terminal commands and navigating directories.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LuisDelmo/MiniMax_TicTactoe.git
   cd tictactoe-minimax-ai
   
2. **Run the game**:
   ```bash
   python tictactoe.py
   
### How to Play

- The game prompts you to make a move by entering row and column indices (0, 1, or 2).
- Once your move is made, the AI will respond with its calculated move.

### Minimax Algorithm

- The Minimax algorithm is a decision rule for minimizing the possible loss while maximizing the potential gain. This AI evaluates each possible game state and picks moves that lead to a guaranteed win or draw.
