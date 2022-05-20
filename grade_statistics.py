#-- Functions --#


def student_results():
    # This function asks the user for results from different students
    # on the course.
    combined_results_string = ""
    while True:
        result = input("Exam points and exercises completed: ")
        if result == "":
            break
        else:
            combined_results_string += result + " "
    return combined_results_string


def exam_points_array(combined_results_string: str):
    # This functions splits the string of exam and exercise points and
    # places the exam points into the exam array.
    split_list = combined_results_string.split()
    exam_points_array = []
    count = 0
    for number in split_list:
        if count % 2 == 0:
            exam_points_array.append(int(number))
            count += 1
        else:
            count += 1
    return exam_points_array


def exercise_points_array(combined_results_string: str):
    # This functions splits the string of exam and exercise points and
    # places the exercise points into the exercise array.
    split_list = combined_results_string.split()
    exercise_points_array = []
    count = 0
    for number in split_list:
        if count % 2 == 0:
            count += 1
        else:
            exercise_points_array.append(int(number))
            count += 1
    return exercise_points_array


def exercise_points_result(exercise_points_array: list):
    exercise_points_result = []
    for number in exercise_points_array:
        exercise_points_result.append(number//10)
    return exercise_points_result


def sum_of_points(exam_array: list, exercise_points_results: list):
    sum_of_points = []
    for index in range(len(exam_array)):
        sum_of_points.append(
            exam_array[index] + exercise_points_results[index])
    return sum_of_points


def pass_or_fail(exam_array: list):
    pass_or_fail = []
    for number in exam_array:
        if number < 10:
            pass_or_fail.append(0)
        else:
            pass_or_fail.append(1)
    return pass_or_fail


def average(sum_of_points: list):
    count = 0
    index = 0
    for number in sum_of_points:
        count += number
    return count / len(sum_of_points)


def pass_percentage(sum_of_points: list, pass_or_fail: list):
    count = 0
    index = 0
    for number in sum_of_points:
        if number >= 15 and pass_or_fail[index] > 0:
            count += 1
            index += 1
        else:
            index += 1
    return (count/len(sum_of_points))*100


def distribution(sum_of_points: list, pass_or_fail: list):
    first_row = "  5: "
    second_row = "  4: "
    third_row = "  3: "
    fourth_row = "  2: "
    fifth_row = "  1: "
    sixth_row = "  0: "
    index = 0

    for number in sum_of_points:
        if number <= 14 or pass_or_fail[index] == 0:
            sixth_row += "*"
            index += 1
        elif number >= 15 and number <= 17 and pass_or_fail[index] > 0:
            fifth_row += "*"
            index += 1
        elif number >= 18 and number <= 20 and pass_or_fail[index] > 0:
            fourth_row += "*"
            index += 1
        elif number >= 21 and number <= 23 and pass_or_fail[index] > 0:
            third_row += "*"
            index += 1
        elif number >= 24 and number <= 27 and pass_or_fail[index] > 0:
            second_row += "*"
            index += 1
        elif number >= 28 and number <= 30 and pass_or_fail[index] > 0:
            first_row += "*"
            index += 1
        else:
            index += 1
    print(first_row)
    print(second_row)
    print(third_row)
    print(fourth_row)
    print(fifth_row)
    print(sixth_row)


def main():
    my_list = student_results()
    exam_array = exam_points_array(my_list)
    exercise_array = exercise_points_array(my_list)
    exercise_points_results = exercise_points_result(exercise_array)
    total_points = sum_of_points(exam_array, exercise_points_results)
    average_points = average(total_points)
    pass_percent = pass_percentage(total_points, pass_or_fail(exam_array))
    print("Statistics:")
    print(f"Points average: {average_points}")
    print(f"Pass percentage: {pass_percent:.1f}")
    print("Grade distribution:")
    distribution(total_points, pass_or_fail(exam_array))


main()
