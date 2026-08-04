n = 124

def maximumProduct(n):
    s = str(int(n))
    i = 0
    j = 1
    product = 0
    while (i <= j):
        if (i >= len(s)-1):
            break
        if (j <= (len(s)-1)):
            dot = int(s[i])*int(s[j])
            product = max(product,dot)
            j += 1
        elif(j >= len(s)):
            i += 1
            j = (i+1)

    return product

print(maximumProduct(n))