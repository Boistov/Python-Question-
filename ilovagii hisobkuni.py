def calculate_football(wins,draws, losses,):

    return 3 * wins + 1 * draws
wins = int(input())
draws = int(input())
losses = int(input())

sum = calculate_football(wins, draws, losses)
print(sum)



