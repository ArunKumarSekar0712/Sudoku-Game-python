# 🧩 Sudoku Game in Python

## 📄 Description
This project is a **Sudoku game** implemented in Python, providing users with an interactive console-based gameplay experience. The game offers multiple difficulty levels (**Easy**, **Medium**, and **Hard**) and features functionalities to fill the board manually or automatically using random values. It also includes a backtracking algorithm to solve the Sudoku puzzle and ensures valid placement of numbers according to Sudoku rules.

---

## ✨ Features

### 🎮 Interactive Gameplay
- Start a new game with different difficulty levels:  
  - **Easy**: 20 pre-filled values.  
  - **Medium**: 15 pre-filled values.  
  - **Hard**: 10 pre-filled values.
- Manually insert values into the Sudoku board.
- View the current state of the board at any time.

### 🤖 Automatic Features
- Auto-fill the board with random valid numbers for selected difficulty levels.
- Solve the Sudoku puzzle completely using a backtracking algorithm.

### ✅ Validation
- Ensures valid placement of numbers in:
  - Rows
  - Columns
  - 3x3 subgrids

### 📊 Board Statistics
- Track the number of filled and empty cells.

### 🏁 End Game
- Display the fully solved Sudoku board at the end of the game.

---

## 🛠️ How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/ArunKumarSekar0712/Sudoku-Game-python.git
2. Navigate to the project directory:
bash
cd sudoku-game-python
3. Run the game:
bash
python sudoku_game.py

🎲 How to Play
1. Select a difficulty level to start a new game.
2. Use the insert option to manually add values to the board.
3. View the board anytime using the show board option.
4. Complete the game or let the program solve it using the backtracking algorithm.
5. Exit the program when done.