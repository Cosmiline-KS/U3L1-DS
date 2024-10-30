def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num-1)
    print(f"Returning; num = {num}")
    return

sample(5)
def while_substitue(num):
    loop2 = num
    print("\nWhile loop: \n")
    while num >= 1:
        print(f"Recursing; num = {num}")
        num -= 1
    print("\nBASE CASE REACHED\n")
    while num < 5:
        num += 1
        print(f"Returning; num = {num}")
            
        
   


while_substitue(5)