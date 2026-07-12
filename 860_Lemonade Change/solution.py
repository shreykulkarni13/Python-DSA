bills = [5,5,10,10,20]

def lemonadeChange(bills):

    five = 0
    ten = 0
    twenty = 0

    for i in range (0, len(bills)):

        if (bills[i] == 5):
            five = five + 5

        elif (bills[i] == 10):
            if (five >= 5):
                ten = ten + 10
                five = five - 5
            
            elif (five == 0):
                return False
            

        elif (bills[i] == 20):
            if (five>=5 and ten>=10):
                # twenty = twenty + 20
                five = five - 5
                ten = ten - 10

            elif (five >= 15):
                # twenty = twenty + 20
                five = five - 15

            else :
                return False
        
    return True

print(lemonadeChange(bills))