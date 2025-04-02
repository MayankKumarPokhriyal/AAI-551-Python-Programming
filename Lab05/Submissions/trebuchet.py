# Author: Mayank Kumar Pokhriyal
# Date: 27th Feb 2025
# Description: This program records the distances and keep track of the three trials with the furthest distance


distance = [0,0,0]
trial =[0,0,0]

continue_trial = 'Y'
current_trial = 1

while continue_trial == "Y":
    input_distance = int(input(f'Please enter your distance for {current_trial} :'))

    if input_distance > distance[0]:
        distance = [input_distance,distance[0],distance[1]]
        trial = [current_trial,trial[0],trial[1]]


    elif input_distance > distance[1]:
        distance = [distance[0],input_distance,distance[1]]
        trial = [trial[0],current_trial,trial[1]]

    elif input_distance > distance[2]:
        distance = [distance[0],distance[1],input_distance]
        trial = [trial[0],trial[1],current_trial]

    continue_trial = input(f'Would you like to input another trial? (Y/N):').strip().upper()
    current_trial += 1

print(f'The top three distances for the trebuchet are:')
print(f"{'Trial':5} {'Distance':8}")
for i in range(3):
    print(f"{trial[i]:5} {distance[i]:8}")
