A, B = map(str, input().split())
temp_a = int(A[0]) + int(A[1]) * 10 + int(A[2]) * 100
temp_b = int(B[0]) + int(B[1]) * 10 + int(B[2]) * 100
print(temp_a if temp_a > temp_b else temp_b)
