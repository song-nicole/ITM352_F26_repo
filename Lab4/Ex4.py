#Try to append to a tuple < it won't work
#Name: Nicole Song
#Date: Sept. 16, 2026

survey_respondents = (1012, 1035, 1021, 1053)
#survey_respondents.append(1011)

print(survey_respondents)

survey_respondents = survey_respondents + (1011,)
print("Updated survey respondents: ", survey_respondents)