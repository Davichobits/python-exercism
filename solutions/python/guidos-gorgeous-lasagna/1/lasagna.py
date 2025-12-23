EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """
    Return the remaining bake time (in minutes) based on the elapsed bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Return the preparation time (in minutes) based on the number of layers.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return the total elapsed cooking time (in minutes),
    including preparation and bake time.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    bake_time = bake_time_remaining(elapsed_bake_time)
    return elapsed_bake_time + preparation_time + bake_time*0