def tenDigit(number):
    number //= 10
    return number % 10

def tens_digit_sort(array):
    array.sort(key=lambda x: (tens_digit(x), -x))
    return array

array=list(map(int,input().split()))
print(tenDigit(array))