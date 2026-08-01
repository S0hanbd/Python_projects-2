voul = "aeiouAEIOU"

s = input("type word or sentence: ")
voul_count = 0

for i in s:
  if i in voul:
    voul_count += 1

print(f"Number of vowels: {voul_count}")