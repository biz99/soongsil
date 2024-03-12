data = input().split()
data_len = len(int(data))
temp = 0

def find_max_recursive():
    print("")
    
def find_max_interative():
    for i in range(1, data_len):
        if data[0] < data[i]:
            data[i] = temp
            data[i] = data[0]
            data[0] = temp
    return data[9]
        
            
print(find_max_interative())