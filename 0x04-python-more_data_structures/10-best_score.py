#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    # Find the maximum value in the dictionary
    b_score = max(a_dictionary.values(), default=None)

    # Iterate over the key-value pairs of the dictionary
    for k, v in a_dictionary.items():
        # Check if the value matches the maximum value
        if v == b_score:
            # Return the key corresponding to the maximum value
            return k

# Example usage:
student_scores = {'John': 85, 'Alice': 92, 'Bob': 78, 'Emily': 92}
print("Student scores:", student_scores)

best_student = best_score(student_scores)
print("Best student:", best_student)

