<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; padding: 2rem;">

  <h1>Tic Tac Toe - Python CLI Game 🎮</h1>

  <p>This is a simple command-line Tic Tac Toe game written in Python. The player plays as <strong>X</strong> and competes against a basic computer opponent playing as <strong>O</strong>.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li>Simple and intuitive CLI interface</li>
    <li>Human vs. Computer gameplay</li>
    <li>Automatic win checking</li>
    <li>Supports replaying without restarting the program</li>
  </ul>

  <h2>💻 How to Play</h2>
  <p>Run the Python script in your terminal:</p>
  <pre><code>python tic_tac_toe.py</code></pre>

  <p>When prompted, choose a tile by typing a 2-letter code:</p>
  <ul>
    <li><strong>tl</strong> = top-left</li>
    <li><strong>tm</strong> = top-middle</li>
    <li><strong>tr</strong> = top-right</li>
    <li><strong>ml</strong> = middle-left</li>
    <li><strong>mm</strong> = center</li>
    <li><strong>mr</strong> = middle-right</li>
    <li><strong>bl</strong> = bottom-left</li>
    <li><strong>bm</strong> = bottom-middle</li>
    <li><strong>br</strong> = bottom-right</li>
  </ul>

  <p>The computer will make a move right after yours. The board is displayed after each turn. The game continues until either player wins or the board is full.</p>

  <h2>🧠 Code Highlights</h2>
  <ul>
    <li><code>robot_pick()</code>: Randomly selects a free spot for the computer's move</li>
    <li><code>check_for_win()</code>: Checks all rows, columns, and diagonals for a win</li>
    <li><code>reset_board()</code>: Clears the board for a new game</li>
    <li><code>continue_game()</code>: Asks the user whether to play again</li>
    <li><code>display_board()</code>: Nicely prints the current state of the board</li>
  </ul>

  <h2>📦 Requirements</h2>
  <p>This game runs on any system with Python 3. No additional libraries are required.</p>

  <h2>📄 License</h2>
  <p>This project is open-source and free to use for learning and personal projects.</p>

</body>
</html>