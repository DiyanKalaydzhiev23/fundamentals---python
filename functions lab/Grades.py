grade = float(input())


def grade_check():
    if 2 <= grade < 3:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    elif 5.50 <= grade <= 6:
        return "Excellent"


print(grade_check())
