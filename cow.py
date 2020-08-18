import math
x = int(input("How many years"))
cow_to_add_total = 0
y = 0

cow_sell_price = 800
cow_buy_price = 1200
cow_keep_price = 210


while y != x:
    cows = 6 + cow_to_add_total
    
    print(str(y))
    print(" Number of Cows: " + str(cows))
    print("")
    print(" Cow cost: " + str(cows * cow_keep_price))
    print(" cow profit: " + str(cows * cow_sell_price))
    left_over = (cows * cow_sell_price) - (cows * cow_keep_price)
    print(" cow break even: " + str(left_over))
    print("")
    cow_to_add_total += math.floor(left_over / cow_buy_price)
    cow_to_add_this_gen = math.floor(left_over / cow_buy_price)
    print(" Total cows bught: " + str(cow_to_add_total))
    print(" Cows bought this generation: " + str(cow_to_add_this_gen))

    y += 1
