foo = []  # pep violation: should be laced below imports part

# pep violation: both imports should be placed at the top of the file
# relative import `from .models import Expense` can break easily when a module is moved,
# absolute imports also make it explicit what module is being used
# from .models import Expense
# it's nice (regarding pep8) when imports are sorted in a groups: first import Python std lib modules,
# then import 3rd party modules and at the end import project-related dependencies
from collections import namedtuple


MyExpense = namedtuple('F', ['type_', 'amount'])


# test data
foo.append(MyExpense('food', 4))
foo.append(MyExpense('food', 3))
foo.append(MyExpense('var', 3))
foo.append(MyExpense('dog', 1))


# it is worth to use Python annotations: min_amount: int, input: List[str, int]
# `input` parameter name shadows Python builtin `input` method
def summarizeExpenses(min_amount, input):  # pep violation: use snake case instead of camel case
    # missing docstring
    expenses = {}
    # hint: checkout defaultdict and how to group list of objects
    for expense in input:
        if expense.amount >= min_amount:
            # will break here: 1. MyExpense does not have `type` attribute, it has `type_`
            # however change to `if not expense.type_` won't help here. Expenses is a dictionary of Expense objects,
            # expense.type_ is a string. Comparison between string and object would fail here.

            if not expense.type in expenses:
                # it seems to be inconsistent to use string in Expense class and integer here
                expenses[expense.type_] = 0
            expenses[expense.type_] = expenses[expense.type_] + expense.amount

    # unnecessary parenthesis, `sorted` method's reverse if False by default - can be skipped
    # summarize_expenses would be more reusable if it only return `expense` as a result
    # printing could be done by another method (so for example it can be formatted in different formats
    for (expense, amount) in sorted(expenses.items(), key=lambda e: e[1], reverse=False):
        # print is not a statement (used to be in old times in Python 2), it's a function,
        # pass parameters within parenthesis: `print(expense.type_, amount)`
        print(expense.type_, amount)



summarizeExpenses(2, foo)
