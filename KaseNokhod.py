n = int(input())
swap = [list(map(int , input().split()))for i in range(n)] 

def find_location (n , swap) :
    location = 1

    for a , b in swap :
        if location == a :
            location = b
        elif location == b :
            location = a

    return location

location = find_location(n , swap)
print(location)


    

