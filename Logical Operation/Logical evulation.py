val1 = input("first boolean value (True/False): ")
val1 = val1.lower() == 'true'

val2 = input("second boolean value (True/False): ")
val2 = val2.lower() == 'true'

print(f"Result of AND : {val1 and val2}")
print(f"Result of OR : {val1 or val2}")
print(f"Result of NOT first : {not val1}")
print(f"Result of NOT Second : {not val2}")