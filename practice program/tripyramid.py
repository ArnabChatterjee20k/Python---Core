def tripyramid(rows):
    for i in range(rows):
        for space in range(rows-i-1):
            print(end=" ")
        for star in range(i+1):
            print("*",end=" ")
        print()
        
tripyramid(5)


