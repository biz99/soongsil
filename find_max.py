# 숫자를 입력받아 리스트에 저장
numbers = input("숫자들을 입력하세요 (공백으로 구분): ").split()

# 입력된 문자열을 정수로 변환
numbers = [int(num) for num in numbers]

# 리스트에서 가장 큰 값을 찾아 출력
max_number = max(numbers)

def find_max_recursive():
    print("")
    
def find_max_interative():
    numbers = [int(data) for num in data]
    max_number = max(numbers)
    
    return max_number
            
print(max_number)