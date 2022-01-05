a, b, c = map(int, input().split())
count = 0

for index in range(a, b + 1):
    if c % index == 0:
        count += 1

print(count)