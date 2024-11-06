def peaks_in_arrays(array):
    peaks_num = []
    index = 0
    for i in array[1:]:
        index += 1
        if i < array[index - 1] and i < array[index + 1]:
            peaks_num.append(index)
    return peaks_num


print(peaks_in_arrays([5, 2, 3, 4, 3, 5, 6, 5, 7, 1, 9, 8, 10]))
