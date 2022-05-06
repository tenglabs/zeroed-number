import random

#Generating random list
def generate_list(max_num):
    
    max_num = max_num+1
    a = random.sample(range(1,max_num), max_num-1)
    print(f'Generated Random List {a}')
    r = random.randint(1, max_num)
    print(f'zeroing {a[r]}')
    a[r] = 0
    print(f'new list(array) is {a}')
    return a


# sorting, iterating
def sorted_iteration(a):
    b = len(a)
    a.insert(b, b+1) 
    a.sort()
    

    for i,x in enumerate(a):
        
        if x != i:
            
            missing_num = i
            print(f'{i} != {x} missing {missing_num}')
            return missing_num


#traversing
def traversing_array(a):
    
    b = len(a)

    for i in range(b):
        if a[abs(a[i])-1] > 0:
            a[abs(a[i])-1] = -a[abs(a[i])-1]

              
    for i in range(b):
        if a[i]>0:
            missing_num = i + 1
            print(f"missing {missing_num} traversing")
            return missing_num


#XOR
def xor_array(a):
    b = len(a)
    global x
    x = 0

    xor1 = a[0]

    for i in range(1, b):
        xor1 = xor1 ^ a[i]

    for i in range(1, b + 1):
        xor1 = xor1 ^ i
      

    set_bit_no = xor1 & ~(xor1 - 1)
      

    for i in range(b):
        if (a[i] & set_bit_no) != 0:
              

            x = x ^ a[i]

              
    for i in range(1, b + 1):
        if (i & set_bit_no) != 0:
              

            x = x ^ i
    print(f'missing {x} XOR')