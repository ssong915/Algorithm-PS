n = input()
n_len = len(n)
left_n = []
right_n = []

for i in range(n_len//2):
    left_n.append(int(n[i]))

for i in range(n_len//2 , n_len):
    right_n.append(int(n[i]))

if sum(left_n)==sum(right_n):
    print("LUCKY")
else:
    print("READY")