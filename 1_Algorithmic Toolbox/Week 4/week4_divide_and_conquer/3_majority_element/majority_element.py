def majority_element(array):
    array.sort()
    count = 1
    max_num = -1
    temp = array[0]
    
    for i in range(1,len(array)):
        if temp == array[i]:
            count += 1
        else:
            count = 1
            temp = array[i]
        if max_num < count:
            max_num = count
            majority = array[i]
            if max_num > len(array) // 2:
                return 1
            
    return 0 

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))