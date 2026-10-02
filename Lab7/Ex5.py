celebs = ("Taylor Swift", "Christiano Ronaldo", "Trevor Noah", "Dua Lupa", "Jungkook")
ages = (34, 38, 39, 27, 26)

celeb_list = []
for celeb in celebs:
    celeb_list.append(celeb)

# Create a list of ages using a list comprehension
#           value  for loop      if condition
ages_list = [age for age in ages]

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)
