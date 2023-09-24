#An Yong Shyan, S10258126B

#Thought Process
#1. Result list and print header
#2. Use split to store the results of respective gamers in a list
#3. Use a nested for loop to check no. of games played,
#   no. of games won and total score
#4. Print the results

#Code

#Result list
results = [[98, 107, 87, 121],
            [88, 111],
            [79, 130, 99],
            [86, 100, 121, 66, 98],
            [108, 79, 92],
            [77, 126, 93, 100, 73, 89]]

# Store the results of respective gamers in variables
Hafu, Toast, Pokimane, Pewdiepie, Ninja, Markiplier = results

# Print header
print('Player       Games Wins Total')

# Iterate over the results
for player, game_results in zip(['Hafu', 'Toast', 'Pokimane', 'Pewdiepie', 'Ninja', 'Markiplier'], results):
    total_games = len(game_results)
    total_wins = sum(1 for result in game_results if result >= 100)
    total_points = sum(game_results)
    print(f'{player:<14} {total_games:<4} {total_wins:<4} {total_points}')
