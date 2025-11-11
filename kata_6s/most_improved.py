# Most Improved - Puzzles #4
#
# When being graded in a subject or a course, high marks are focused on the most, but what about most improved? As a computer science teacher, you would like to create a function that calculates the most improved students and ranks them in a list.
#
# Task
#
# Your task is to complete the function to return an array sorted by most improved as percentages.
#
# Input
#
# The input you will receive will be an array of students, students will be objects containing a name and an array of marks (in order of acheived). The marks will be out of 100, a student can however have a mark of null if the test was not attempted (treat this as 0).
#
# Example of student Object: {name:'Henry, Johns',marks:[25,50]}
#
# Output
#
# The output expected will be an array of objects similar to the student object, containing the name and total improvement percentage out of the first and last mark given to calculate the overall improvement percentage. The output array must be sorted by most improved (Round the calculated improvement). If there is a tie in improvements, then order by name (capitals before lowercase).
#
# Example of return Object: {name:'Henry, Johns',improvement:100}

def calculate_improved(students):
    res = []
    for item in students:
        name = item.get("name")
        marks = item.get("marks", [])

        old = marks[0] if marks and marks[0] is not None else 0
        new = marks[-1] if marks and marks[-1] is not None else 0

        if old == 0:
            improvement = 0
        else:
            improvement = round(((new - old) / old) * 100)

        res.append({"name": name, "improvement": int(improvement)})

    res.sort(key=lambda x: (-x["improvement"], x["name"]))
    return res
