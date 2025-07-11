# Blind Auction

- A simple terminal-based blind auction game built in Python.
- Participants submit bids without knowing the others' bids, and the highest bidder wins.
- The game includes a countdown timer, random rewards, and a dynamic leaderboard.

## Features

- ASCII art for visual feel
- Real-time countdown for bidding
- Random prize awarded to one participant
- Leaderboard to display top bidders
- Cross-platform screen clearing
- Handles multiple participants interactively

## Tech Stack

- Python 3.X
- Standard libraries: `os`, `time`, `random`

## How It Works

1. Each participant enters their name and places a bid within 10 seconds.
2. After each round, the leaderboard is displayed.
3. The bidding continues until no more participants remain.
4. The highest bidder is declared the winner and a random prize is awarded.

## Setup and Installation

### 1. Clone the repository:
```bash
git clone https://github.com/rampalliprakhar/blind_auction.git
cd blind-auction
```

### 2. Run the program:
```bash
python main.py
```

### 3. Example
```bash
What is your name?: Alice
You have 10 seconds to place your bid!
Enter your bid: $300
Alice placed a bid of $300

--- Leaderboard ---
1. Alice: $300
-------------------

Are there any other bidders? Type 'yes' or 'no': yes
```

### 4. At the end of the game:
```bash
The winner is Alice with a bid of $300.
Congratulations! You won a Gift Card for participating!
```

### 5. Project Structure
```bash
blind-auction/
├── art.py         # Contains ASCII art logo
└── main.py        # Main game logic
```
