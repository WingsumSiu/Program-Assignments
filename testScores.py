student_scores = {"Bob": [75, 65, 42, 73], "Helen": [62, 65, 67, 79], "Vic": [13, 17, 19, 17]}

def score_printer(student):
    if student not in student_scores:
        return "No data on student."
    if student == "Bob":
        return student_scores["Bob"]
    if student == "Helen":
        return student_scores["Helen"]
    if student == "Vic":
        return student_scores["Vic"]

print(score_printer("Vic"))