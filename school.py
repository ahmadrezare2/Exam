import json

correct_answer = {
    ("what is the output?", 4),
    ("Is earth flat?", 1),
    ("how much money do they have?", 2),
}
correct_answer_dict = dict()
for question, answer in correct_answer:
    correct_answer_dict[question] = answer

student_submissions = {
    "Helen": [
        {"what is the output?": 4},
        {"Is earth flat?": 2},
        {"how much money do they have?": 3},
    ],
    "Hana": [
        {"what is the output?": 3},
        {"Is earth flat?": 1},
        {"how much money do they have?": 3},
    ],
    "Helma": [
        {"what is the output?": 4},
        {"Is earth flat?": 1},
        {"how much money do they have?": 2},
    ],
}

result = {"Helen": 50, "Hana": -20, "Helma": -33}
correct_answer_student = incorrect_answer_student = 0
for student in student_submissions:
    for student_answers in student_submissions[student]:
        for question in student_answers:
            if student_answers[question] == correct_answer_dict[question]:
                correct_answer_student += 1
            else:
                incorrect_answer_student += 1

    result[student] = ((correct_answer_student * 3) - incorrect_answer_student) / (
        (correct_answer_student + incorrect_answer_student) * 3
    )

    correct_answer_student = incorrect_answer_student = 0

result = json.dumps(result)
with open("Ahmadreza.txt", "w+") as f:
    f.writelines(result)
