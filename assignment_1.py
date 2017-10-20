"""Assignment 1."""

# from assignment_1_eval import evaluate
from assignment_1_eval import evaluate2


def pluralize(sg):
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    plurals = []
    plurals.append(sg + 's')
    return plurals


# evaluate(pluralize)
evaluate2(pluralize)  # more precise evaluation with precision and recall

# accuracy = for how many words did you get all plurals correct?
# precision = of all the things predicted as plurals, how many are correct?
# recall = of all the actual plurals, how many did you include?
