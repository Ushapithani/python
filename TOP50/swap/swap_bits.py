def swap_bits(n, p1, p2):
    
    bit1 = (n >> p1) & 1
    bit2 = (n >> p2) & 1

    if bit1 != bit2:
        mask = (1 << p1) | (1 << p2)
        
        n ^= mask

    return 
n = 31  # Binary: 00011111
p1 = 2
p2 = 6
result = swap_bits(n, p1, p2)
print(f"Result: {result} (Binary: {bin(result)})")