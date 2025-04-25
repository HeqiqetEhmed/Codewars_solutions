def find_outlier(integer):
    #Creating a list of odd numbers from the input list
    count_o = [x for x in integer if x % 2 != 0]
    
    #Creating a list of even numbers from the input list
    count_e = [x for x in integer if x % 2 == 0]
    
    # If the list of odd numbers has fewer elements, return the first odd number (the outlier)
    # Otherwise, return the first even number (the outlier)
    return count_o[0] if len(count_o) < len(count_e) else count_e[0]
