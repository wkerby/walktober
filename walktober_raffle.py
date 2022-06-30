#def sum_lines(lines):
    #sum_list = []
    #for line in lines:
        #sum_list.append(line[-1])
    #return sum(sum_list)
import csv
file_name = '/Users/jefferykerby/Desktop/Python/Excel Data/Walktober 2021 Form as of 10_05_21.csv'
with open(file_name, 'r') as file_object:
    reader = list(csv.reader(file_object))
    raf_list = []
    raf_dict = {}
    supervisor_dict = {}
    for line in reader[1:]:
        if line[0] in raf_list:
            raf_dict[line[0]] += int(line[-2])
        else:
            raf_dict[line[0]] = int(line[-2])
            supervisor_dict[line[0]] = str(line[-3])
        raf_list.append(line[0])
#sum_check = sum(list(raf_dict.values()))
#if sum_check == 1:
    #print("Everything is checking out as it should")
#else:
    #print("Oops! Something's not right!")
print(raf_dict)
import random
grand_raffle_winner = random.choices(list(raf_dict.keys()), weights = (list(raf_dict.values())), k = 1) 
print("The B&G Walktober 2021 $500 raffle winner is " + grand_raffle_winner[0] + "!" + '\n')
print("The winner's supervisor is " + supervisor_dict[grand_raffle_winner[0]] + ".")
del raf_dict[grand_raffle_winner[0]]

for i in list(range(5)):
    small_raffle_winner = random.choices(list(raf_dict.keys()), weights = (list(raf_dict.values())), k = 1)
    if i == 0:
        print("\nThe 1st B&G Walktober 2021 $100 raffle winner is " + small_raffle_winner[0] + "!")
    elif i == 1:
        print("\nThe 2nd B&G Walktober 2021 $100 raffle winner is " + small_raffle_winner[0] + "!")
    elif i == 2:
        print("\nThe 3rd B&G Walktober 2021 $100 raffle winner is " + small_raffle_winner[0] + "!")
    else:
        print("\nThe " + str(i+1) + "th B&G Walktober 2021 $100 raffle winner is " + small_raffle_winner[0] + "!")
    print('\n' + "The winner's supervisor is " + supervisor_dict[small_raffle_winner[0]] + ".")
    del raf_dict[small_raffle_winner[0]]
    #print(list(raf_dict.keys()))
    
