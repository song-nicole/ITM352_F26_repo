celebs = ("Taylor Swift", "Christiano Ronaldo", "Trevor Noah", "Dua Lupa", "Jungkook")
ages = (34, 38, 39, 27, 26)

#method using for loops
celeb_list = []
for celeb in celebs:
    celeb_list.append(celeb)

ages_list = []
for age in ages:
    ages_list.append(age)

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)


#method using list comprehension
celeb_list = [celeb for celeb in celebs]

#           value  for loop      if condition
ages_list = [age for age in ages]

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)
