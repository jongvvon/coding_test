# N is num of brother, S is current location
# locations are brother locations
N, S = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

if min(locations) == max(locations) == S:
    print(0)
elif locations[0] >= S:
    print(max(locations) - S)
elif locations[-1] <= S:
    print(S - min(locations))
else:
    if max(locations) - S > S - min(locations):
        print(S-min(locations))
    else:
        print(max(locations)-S)