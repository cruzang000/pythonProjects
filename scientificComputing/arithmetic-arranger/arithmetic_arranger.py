

#  -----------------------------------------------
#   function will take a list of problems and a show answers
#   boolean and convert each problem in the list into a stacked
#   version of the problem.
#  -----------------------------------------------
def arithmetic_arranger(problems, showAnswers=False):
    try:
        # check if there are more than 5 problems, return error
        if len(problems) > 5:
            raise ValueError("Error: Too many problems.")

        firstRowString = ""
        secondRowString = ""
        thirdRowString = ""
        fourthRowString = ""

        # dictionary of possible answers
        operators = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
        }

        # loop through length of problems
        for index in range(len(problems)):

            # split the current problem into first number, operator, second number
            problemParts = problems[index].split()

            # if not addition or subtraction return error
            if (problemParts[1] in operators) is False:
                raise ValueError("Error: Operator must be '+' or '-'.")
            # if either number is not numeric return error
            elif problemParts[0].isnumeric() is False or problemParts[2].isnumeric() is False:
                raise ValueError("Error: Numbers must only contain digits.")
            # if either number is longer than 4 digits return error
            elif len(problemParts[0]) > 4 or len(problemParts[2]) > 4:
                raise ValueError("Error: Numbers cannot be more than four digits.")

            # get length of current problem longest number
            longestNumberLength = len(
                problemParts[0] if len(problemParts[0]) >= len(problemParts[2]) else problemParts[2]
            )

            # build problem rows, justify right and add spaces to match length of longest number if needed
            firstRow = problemParts[0].rjust(longestNumberLength + 2)  # first number in problem
            secondRow = problemParts[1] + " " + problemParts[2].rjust(longestNumberLength)  # second number in problem

            # build third dashed row the length of the second row
            thirdRow = "-" * (len(secondRow))  # dashed line

            # build fourth row problem answer, look up formula in operators dictionary passing in 2 numbers returns
            # answers, convert to string and justify right
            fourthRow = str(
                    operators[problemParts[1]](int(problemParts[0]), int(problemParts[2]))
                ).rjust(longestNumberLength + 2)

            # add to row string and add 4 spaces at end if not the last problem
            firstRowString += firstRow + ("" if index >= len(problems) - 1 else "    ")
            secondRowString += secondRow + ("" if index >= len(problems) - 1 else "    ")
            thirdRowString += thirdRow + ("" if index >= len(problems) - 1 else "    ")
            fourthRowString += fourthRow + ("" if index >= len(problems) - 1 else "    ")

        # return final string of all math problem rows
        return firstRowString + "\n" + secondRowString + "\n" + thirdRowString + (("\n" + fourthRowString) if showAnswers else "")

    except ValueError as error:
        return error.args[0]
