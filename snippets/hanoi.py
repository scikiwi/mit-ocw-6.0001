# Code I wrote from my memory after 
# watching example in Lecture 6 and
# Reducible's video: https://www.youtube.com/watch?v=rf6uf3jNjbo

# Prints move in the format "start -> end"
def move(start, end):
    print(start, "->", end) 
    
def hanoi(n, start, end):
    if n == 1:
        move(start, end)
    else:
        spare = 6 - (start + end) # Neat way to avoid user-inputting spare from Reducible's video
        hanoi(n-1, start, spare)
        hanoi(1, start, end)
        hanoi(n-1, spare, end)
        
# Will take inputs n = number of discs,
# start: starting position and
# end = ending position
        
n = int(input("n: "))
start = int(input("start: "))
end = int(input("end: "))
hanoi(n, start, end)
