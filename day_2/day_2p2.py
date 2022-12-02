#advent of code 2022 day 2

highest_total = 0
running_total = 0
results = {
    'A X' : 3,
    'A Y' : 4,
    'A Z' : 8,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 2,
    'C Y' : 6,
    'C Z' : 7
}
points = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}
def get_score(first, second):
    #a rock
    #b paper
    #c scissors
    #x rock     1
    #y paper    2
    #z scissors 3
    #draw       3
    #win        6
    #x lose 
    #y draw
    #z win
    pass
    
    
running_total = 0 
    
with open('input.txt') as text:
    #data = text.read()
    
    for line in text:
        data = line.strip().split('\n')
        #print(data)
        score = results[data[0]]
        #second_letter = data[0].split(" ")[1]
        #print(f'score of game: {score}')
        #print(f'2nd letter: {second_letter} for {points[second_letter]} points')
        running_total += score
        #running_total += points[second_letter]
        #print(f'running total: {running_total}')
        
    print(f'FINAL TOTAL: {running_total}')
