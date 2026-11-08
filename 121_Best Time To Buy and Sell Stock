prices = [2,4,1]

def maxProfit(prices):
    ...
    l = 0
    r = 1
    profit = 0
    
    while (r < len(prices)):
        if (prices[l]>prices[r]):
            l = r
            r = r + 1
            
        else: 
            profit = max(prices[r]-prices[l], profit)
            r = r+1
            
    return profit
        
            
    
    
print (maxProfit(prices))
                
    