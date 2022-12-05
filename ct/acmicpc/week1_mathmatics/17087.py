# N is num of brother, S is current location
# locations are brother locations
import math

N, S = map(int, input().split())
locations = list(map(int, input().split()))

array = []
for i in range(N):
    array.append(abs(S-locations[i]))

gcd = array[0]
for j in range(1, N):
    gcd = math.gcd(gcd, array[j])

print(gcd)