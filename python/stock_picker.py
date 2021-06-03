def picker(prices):
    # PSEUDOCODE
    # Iterate through a list, return a pair of indices with the greatest difference 
    # of their respective values with the lower value with lower index 
    # e.g. [3,6,6,3,15] lowest index 0, highest index 4
    # Skip index 0 when searching for high value(sell)

# You need to buy before you can sell
# Pay attention to edge cases like when the lowest day is the last day or the highest day is the first day.# 
    
    low      = 0
    high     = 0
    low_idx  = 0
    high_idx = 0
    price    = 0
    buy_sell = []
    blah = []

  
    for day, price in enumerate(prices):
        # buy first finding lowest price, get status [searching, bought, maybe, sold] 
        if price > high and day >= 1:
            high = price
            high_idx = day
            # sell
            for day, price in enumerate(prices[0:high]):

                if price <= low:
                    low = price
                print('prices:', prices[0:high]) 

        # if price > high:
        #     high = price
    # print('price:', price)       
    # print('high:', high)
        # else:
        #     continue
        # another for loop
        # for price in range(0, high):
        #     if price <= low:
        #         low = price
        #         print('high:', high, 'low:',low)
        # print('day:',day, 'price: $',price)
    # print('low:', low)       
    # print('high:', high)   

    return prices

# print(picker([8,3,6,4,1]))
# print(picker([6,4,1]))
print(picker([17,3,6,9,15,8,6,1]))