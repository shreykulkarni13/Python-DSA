n = 124

def maxProduct(n):
    product = 0
    s = str(int(n))
    for i in range (0, len(s)-1):
        j = 0
        while (j < len(s)):
            dot = (int(s[i])*int(s[j]))
            j = j+1
            if (product >= dot):
                continue
            else:
                product = dot 

    return max(product,dot)

print(maxProduct(n))