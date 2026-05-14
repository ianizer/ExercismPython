"""Functions for organizing and calculating student exam scores."""

FAILING_SCORE = 40
NUMBER_OF_LETTER_GRADES = 4  # A B C D


def round_scores(student_scores: list[float | int]) -> list[int]:
    """Round all provided student scores.

    Parameters:
        student_scores (list[float|int]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    rounded_scores = []

    # We must "consume" student_scores, and make a new list according to the problem.
    # So, we shall pop every value from the scores list and add it to a new list.
    while student_scores:
        rounded_scores.append(round(student_scores.pop()))

    return rounded_scores


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    num_failures = 0

    for score in student_scores:
        if score <= FAILING_SCORE:
            num_failures += 1

    return num_failures


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]:  Integer scores that are at or above the "best" threshold.
    """

    best_scores = []

    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)

    return best_scores


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest: int - value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grade_separation_amount = (highest - FAILING_SCORE) // NUMBER_OF_LETTER_GRADES

    grade_thresholds = []

    for multiplier in range(NUMBER_OF_LETTER_GRADES):
        grade_thresholds.append(
            1 + FAILING_SCORE + (multiplier * grade_separation_amount)
        )

    return grade_thresholds


def student_ranking(
    student_scores: list[int | float], student_names: list[str]
) -> list[str]:
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]:  Strings in format ["<rank>. <student name>: <score>"].
    """

    student_rank_name_grade_strings = []

    for index, score in enumerate(student_scores):
        student_rank_name_grade_strings.append(
            f"{index + 1}. {student_names[index]}: {score}"
        )

    return student_rank_name_grade_strings


def perfect_score(student_info: list[list[str | int]]) -> list[str | int]:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """

    for student in student_info:
        score = student[1]
        if score == 100:
            return student

    return []
