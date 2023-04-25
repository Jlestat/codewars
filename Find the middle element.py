def gimme(input_array):
    for i in range(len(input_array)):
        if input_array[i] < max(input_array) and input_array[i] > min(input_array):
            return i
    
