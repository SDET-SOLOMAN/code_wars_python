# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples

# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

def ips_between(start, end):
    
    s1, s2 = [int(x) for x in start.split(".")], list(map(int, end.split(".")))
    total = 0
    
    for num in range(len(s1)):
        
        s1_n = s1[num]
        s2_n = s2[num]
        
        if s1_n == s2_n:
            continue
        
        diff = s2_n - s1_n
        
        if num == 0:
            diff *= 256 ** 3
        elif num == 1:
            diff *= 256 ** 2
        elif num == 2:
            diff *= 256
        else:
            diff *= 1
        total += diff
        
    return total