print(20 - 5 + 3)
print(2 + 3 ** 2)

name = "Nicole"
age = 19
hometown = "Honolulu"
major = "Accounting"
print("My name is ", name, ", I am from ", hometown, ", and I am currently majoring in ", major, ".")

age_in_days = age * 365
print("I have been alive for ", age_in_days, "days.")

weekly_spending = 55
monthly_expenses = weekly_spending * 52 / 12
print("My monthly expenses total about $", monthly_expenses, ".")

hours_alive = age * 365 * 24
print("I have been alive for ", hours_alive, " hours.")

gpa_4_point_scale = 3.97
gpa_100_point_scale = gpa_4_point_scale * 25
print("My GPA on a 100-point scale is ", gpa_100_point_scale, ".")

years_before_100 = 100 - age
print("I have ", years_before_100, " more years before I turn 100.")

first_year_of_college = 2024
this_year = 2026
print("I have completed ", this_year - first_year_of_college, " years of college.")

expected_graduation_year = first_year_of_college + 4
print("I expect to graduate in ", expected_graduation_year, ".")

weekly_watering = 3
yearly_watering = weekly_watering * 52
print("I water my plants about ", yearly_watering, " times a year.")

daily_cat_food_consumption = 0.8
monthly_cat_food_consumption = daily_cat_food_consumption * 30
print("My cats eat about ", monthly_cat_food_consumption, " cups of food a month.")

professional_email_signature = name + " " + major + " " + str(expected_graduation_year)

address = "2500 Campus Road, Honolulu, HI 96822"
address2 = '''2500 Campus Road,
Honolulu, HI 96822'''

initials = "N. S."
birth_year = 2006
social_media_username = initials + str(birth_year)

hobby1 = "felting"
hobby2 = "gardening"
hobby3 = "wire crafts"
hobby4 = "jewelry making"
goal = "graduate peacefully from college and find a fulfilling career in accounting"
about_me = f"My name is {name}, I am {age} years old, and I am from {hometown}. My hobbies include a variety of activities, including {hobby1}, {hobby2}, {hobby3}, and {hobby4}. My current goal is simply to {goal}."

print(age >= 18)
print(age >= 21)
print(age >= 25)
print(gpa_4_point_scale >= 3.0)

ics101 = True
bus311 = True
print(ics101 and bus311 and gpa_4_point_scale >= 3.0)

class_standing = "Junior"
print(class_standing and gpa_4_point_scale >= 3.0)

budget = 250
cost_of_laptop = 300
cost_of_ipad = 170
print(budget >= cost_of_laptop)
print(budget >= cost_of_ipad)

semester_tuition = 5880
semester_fees = 457
credit_hours = 18
housing = 3000
meals = 1052
total_semester_cost = (semester_tuition + semester_fees) * credit_hours + (housing + meals)

homework_avg = 98
exam_avg = 93
grade = (homework_avg * 0.3) + (exam_avg * 0.7)

income = 9000
rent = 2000
utilities = 200
groceries = 320
entertainment = 28
monthly_budget = income - (rent + utilities + groceries + entertainment)

hours_per_week = 20
number_of_courses = 6
study_time = hours_per_week / number_of_courses
print(study_time > 18)