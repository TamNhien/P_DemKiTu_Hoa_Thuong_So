string = input("Nhập chuỗi : ")
upper_count = sum(1 for char in string if char.isupper())
lower_count = sum(1 for char in string if char.islower())
digit_count = sum(1 for char in string if char.isdigit())

print("Số ký tự in hoa trong chuỗi là : ", upper_count)
print("Số ký tự in thường trong chuỗi là : ", lower_count)
print("Số ký tự số trong chuỗi là : ", digit_count)

