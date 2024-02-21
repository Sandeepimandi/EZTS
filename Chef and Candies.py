import math

# Function to calculate the minimum number of candy packets required
def min_candy_packets(N, X):
    total_candies_needed = N - X
    min_packets = math.ceil(total_candies_needed / 4)
    return min_packets

# Input the number of test cases
T = int(input("Enter the number of test cases: "))

# Iterate through each test case
for _ in range(T):
    N, X = map(int, input().split())
    min_packets = min_candy_packets(N, X)
    print(min_packets)