def maksimum(*args):

    
    max_num = 0  # Mengambil angka pertama sebagai nilai awal maksimum

    for num in args:
        if num > max_num:
            max_num = num  # Memperbarui nilai maksimum jika ditemukan angka yang lebih besar
    
    return max_num

# Test Case 1
result1 = maksimum(1, 2, 4, 6, 9, 3, 1, 9, -10)
print(result1)  # Output: 10

# Test Case 2
result2 = maksimum(0, 1, 90, -430, 23, 212, 34)
print(result2)  # Output: 430
# Fungsi ini akan menginisialisasi max