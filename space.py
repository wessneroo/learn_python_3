print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  k = 0.91
elif planet == 2:
  k = 0.38
elif planet == 3:
  k = 2.34
elif planet == 4:
  k = 1.06
elif planet == 5:
  k = 0.92
elif planet == 6:
  k = 1.19
else:
  print("No data in library for the selected planet.")

otherworldly_weight = weight * k
print(otherworldly_weight)
