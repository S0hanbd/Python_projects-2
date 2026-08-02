score = []

for i in range(8):
    n = int(input(f"score of student {i+1}: "))
    score.append(n)

sum_no =0
min_no = score[0]
max_no = score[0]
for i in score:
    sum_no += i
    if min_no > i:
        min_no = i
    if max_no < i:
        max_no = i

ave = sum_no / len(score)
print(f"MIn = {min_no} Max = {max_no} Average = {ave}")