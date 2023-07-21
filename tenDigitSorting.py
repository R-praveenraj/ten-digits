def tensDigit(number):
    number //= 10
    return number % 10
def tens_digit_sort(array):
    array.sort(key=lambda x: (tensDigit(x), -x))
    return array
    
array=list(map(int,input().split()))
print(tens_digit_sort(array))
