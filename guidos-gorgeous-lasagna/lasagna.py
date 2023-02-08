# int expected baketime in minutes
EXPECTED_BAKE_TIME = 40
# int preparation time per layer in minutes
PREPARATION_TIME = 2


def bake_time_remaining(actual_minutes_in_oven):
    """Calculate and return the bake time remaining in minutes.

        :param actual_minutes_in_oven: int baking time already elapsed.
        :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - actual_minutes_in_oven


def preparation_time_in_minutes(layers):
    """Calculate and return the preparation time in minutes

        :param layers: int layers of lasagna to prepare
        :return: int total preparation time in minutes derived from PREPARATION_TIME

        Function that takes the number of layers to prepare as an argument and
        returns the total preparation time in minutes based on the 'PREPARATION_TIME'
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate and return the time already spent cooking in minutes

        :param number_of_layers: int layers of lasagna to prepare
        :param elapsed_bake_time: int number of minutes the lasagna has been in the oven.
        :return: the sum of your total preparation time and the time the lasagna has already spent baking in the oven.

        Function that takes the number of layers and elapsed bake time and returns the total time spent cooking in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
