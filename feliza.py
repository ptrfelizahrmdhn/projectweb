def insertion_sort(arr):
    n = len(arr)
    steps = []  # Untuk menyimpan langkah-langkah pengurutan
    for i in range(1, n):
        key = arr[i]  # Simpan nilai saat ini untuk membandingkan
        j = i - 1
        # Pindahkan elemen-elemen array yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            steps.append(list(arr))  # Simpan langkah pengurutan
        arr[j + 1] = key  # Tempatkan key di posisi yang benar
        steps.append(list(arr))  # Simpan langkah pengurutan setelah penempatan key
    return steps

# Contoh penggunaan
arr = [4, 3, 2, 10, 12, 1, 5, 6]

print("Array sebelum pengurutan:", arr)
sorting_steps = insertion_sort(arr)

# Menampilkan langkah-langkah pengurutan
print("\nLangkah-langkah pengurutan:")
for step in sorting_steps:
    print(step)
