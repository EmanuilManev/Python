target = int(input())
current = target - 30
result = 0
count = 0
tries = 0

while current <= target:
    result = int(input())
    count += 1
    tries += 1
    if result > current:
        if current == target:
            print("Tihomir succeeded, he jumped over " + str(current) + "cm after " + str(count) + " jumps.")
            break
        current += 5
        tries = 0
    elif tries == 3:
        print("Tihomir failed at " + str(current) + "cm after " + str(count) + " jumps.")

