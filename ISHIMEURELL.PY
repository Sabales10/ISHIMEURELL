player_ishi = 0
player_yanie = 0

treasure_x = 15
treasure_y = 3

game_running = True
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:

    move = input("Enter move (up/down/left/right): ").lower()
    if move == 'up':
        player_ishi += 1
    elif move == 'down':
        player_ishi -= 1
    elif move == 'left':
        player_yanie -= 1
    elif move == 'right':
        player_yanie += 1
    else:
        print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")
        continue

    if player_yanie == treasure_x and player_ishi == treasure_y:
        print(f"Congratulations! You found the treasure at ({player_x}, {player_y})!")
        game_running = False
    else:
        print(f"Player position: ({player_yanie}, {player_ishi})")
