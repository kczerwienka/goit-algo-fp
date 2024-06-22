def greedy_algorithm(items, amount):
    
    

    # sorting the list
    
    sorteditems = {}
    tmp = []
    for k, v in items.items():
        tmp.append([k,v["calories"]/v["cost"]])
    tmp.sort(key=lambda x: x[1], reverse=True)
    
    for t in tmp:
        sorteditems[t[0]] = items[t[0]]
    # print (sorteditems)

    #storage of results
    result = {k:0 for k in items.keys()}

    print(sorteditems,"\n")

    #solution
    kcal = 0
    for k, v in sorteditems.items():
        while amount >= v["cost"]:
            result[k] += 1
            amount -= v["cost"]
            kcal += v["calories"]

    return result , amount, kcal



# def find_min_coins(value, count, amount) -> dict:
#     return_change = {1 : 0, 2 : 0, 5 : 0, 10 : 0, 25 : 0, 50 : 0} 
    
#     i = 5

#     while amount > 0:

#         if amount >= value[i] and count[i] > 0:
        
#             amount -= value[i]
#             return_change[value[i]] += 1
        
#         else:
#             i -= 1

#     return return_change

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
amount = 100

print(greedy_algorithm(items, amount))
