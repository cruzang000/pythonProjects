import copy
import random


class Hat:

    def __init__(self, **colors):
        """
        takes 1 or more color associative arguments then creates list of contents with colors
        :param colors: 1 or more color=occurrence arguments
        """
        self.contents = [color for color, count in colors.items() for x in range(count)]

    def draw(self, ballsToDraw):
        """
        takes an argument for number of balls to draw, then loops through contents list drawing a ball and adding to
        list of picked balls to return, if number of balls to draw is more than len of contents, return all clear list
        :param ballsToDraw: number of balls to draw from list
        :type ballsToDraw: int
        :return: list of picked balls
        :rtype: list
        """
        pickedBalls = []

        # if len of contents if suffice draw balls and remove from list as removed else return and clear list
        if ballsToDraw < len(self.contents):
            for ball in range(ballsToDraw):
                pickedBall = random.choice(self.contents)
                pickedBalls.append(pickedBall)
                self.contents.remove(pickedBall)
        else:
            pickedBalls = self.contents
            self.contents = []

        return pickedBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    run experiments to determine probability of returning specified number of colored balls
    :param hat: hat object containing list of colored balls
    :type hat: hat object
    :param expected_balls: group of balls to check probability of drawing
    :type expected_balls: dictionary
    :param num_balls_drawn: number of balls to draw from hat each experiment
    :type num_balls_drawn:
    :param num_experiments:
    :type num_experiments:
    :return:
    :rtype:
    """
    expectedResultCount = 0

    # for each experiment make copy of hat draw balls and check color counts added to result count if found
    # return probability after running experiments
    for currentExperiment in range(num_experiments):
        ballsDrawn = copy.deepcopy(hat).draw(num_balls_drawn)

        foundCount = 0 + sum([1 for color in expected_balls if ballsDrawn.count(color) >= expected_balls[color]])

        expectedResultCount = expectedResultCount + (1 if foundCount == len(expected_balls) else 0)

    return float(expectedResultCount / num_experiments)
