user_points = {}
language_submission = {}

data = input()

while not data == "exam finished":
    split_data = data.split("-")

    if split_data[1] == "banned":
        user = split_data[0]
        del user_points[user]
    else:
        user, language, points = split_data
        points = int(points)
        if user in user_points:
            if user_points[user] < points:
                user_points[user] = points
        else:
            user_points[user] = points
        if language not in language_submission:
            language_submission[language] = 0
        language_submission[language] += 1

    data = input()

# sorted_user_points = sorted(user_points.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))

print("Results:")
for user, points in user_points.items():
# for user, points in sorted_user_points:
    print(f"{user} | {points}")
# sorted_language_submissions = sorted(language_submission.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
print("Submissions:")
# for lang, submissions in sorted_language_submissions:
for lang, submissions in language_submission.items():
    print(f"{lang} - {submissions}")
