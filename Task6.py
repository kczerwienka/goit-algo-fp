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



def dynamic_programming(w, items, n):
    # create a table K to store the optimal values of the subtasks
    K = [[0 for w in range(w + 1)] for i in range(n + 1)]
    R = [[{k:0 for k in items.keys()} for w in range(w + 1)] for i in range(n + 1)]

    # build table K from the bottom up
    for i in range(n + 1):
        for w in range(w + 1):
            for item in items:
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif items[item]["cost"] <= w:
                    K[i][w] = max(items[item]["calories"] + K[i - 1][w - items[item]["cost"]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

    return K[n][w]

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

n = 10
print(dynamic_programming(amount, items, n))