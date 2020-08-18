import math
print("Please only use numbers or the program will crash")

x = int(input("How many years"))
cow_to_add_total = 0
y = 0

starting_cows = int(input("How many cows are you starting with? (6)"))#6
cow_sell_price = int(input("How much are the calves going for? (800) "))#800
cow_buy_price = int(input("How much does a calving cow cost? (1200) "))#1200
cow_keep_price = int(input("How much does it cost to keep the a cow? (210) "))#210

while y != x:
    cows = starting_cows + cow_to_add_total
    
    print(str(y + 1))
    print(" Number of Cows: " + str(cows))
    print("")
    print(" Cow cost: " + str(cows * cow_keep_price))
    print(" Cow profit: " + str(cows * cow_sell_price))
    left_over = (cows * cow_sell_price) - (cows * cow_keep_price)
    print(" Cow break even: " + str(left_over))
    print("")
    cow_to_add_total += math.floor(left_over / cow_buy_price)
    cow_to_add_this_gen = math.floor(left_over / cow_buy_price)
    print(" Total cows bught: " + str(cow_to_add_total))
    print(" Cows bought this generation: " + str(cow_to_add_this_gen))

    y += 1

while 1:
    if input("Press any key then enter to end the program"):
        break
