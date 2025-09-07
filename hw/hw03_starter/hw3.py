import random
import time
def generate_lists(size):
    """Generates two lists of random unique integers with a length of size"""
    list1 = random.sample(range(size*2), size)
    list2 = random.sample(range(size*2), size)
    return list1, list2

def find_common(list1, list2):
    """Counts number of common integers between two lists without using Python collections"""
    # count = 0                   
    # for num in list1:     
    #     if num in list2:
    #         count += 1
    # return count
    count = 0
    for index1 in range(len(list1)):
        for index2 in range(len(list2)):
            if list1[index1] == list2[index2]:
                count += 1
    return count

def find_common_efficient(list1, list2):
    """Counts number of common integers between two lists using Python collections"""
    return len(set(list1).intersection(list2))

def measure_time():
    """Measures the time it takes for find_common and find_common_efficient and prints out the results in a table"""
    timing_data = []
    sizes = [10, 100, 1000, 10000, 20000]
    for index in range(len(sizes)):
        start1 = time.time()
        find_common(*generate_lists(sizes[index]))
        end1 = time.time()
        elasped1 = end1 - start1
        start2 = time.time()
        find_common_efficient(*generate_lists(sizes[index]))
        end2 = time.time()
        elasped2 = end2 - start2
        timing_data.append([sizes[index], elasped1, elasped2])
    """This section prints out the header of the table first and then the for loop prints each set of data"""
    print ("List Size   find_common Time (s)   find_common_efficient Time (s)\n---------- ---------------------- -------------------------------")
    for index in range(len(sizes)):
        #print ('%8.0f  |  %18.5f  |  %10.5f'%(timing_data[index][0],timing_data[index][1], timing_data[index][2]))
        print(f"|{timing_data[index][0]: >9}|{timing_data[index][1]:^22.5}|{timing_data[index][2]:^20.5}")


if __name__ == "__main__":
    measure_time()