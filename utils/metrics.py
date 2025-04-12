def mse(observations, predictions):
    """
    Mean Squared Error
    """
    squared_errors = [
        (observation - prediction) ** 2
        for observation, prediction in zip(observations, predictions)
    ]
    mean_squared_error = sum(squared_errors) / len(squared_errors)
    return mean_squared_error


def mae(observations, predictions):
    """
    Mean Squared Error
    """
    squared_errors = [
        (observation - prediction) ** 2
        for observation, prediction in zip(observations, predictions)
    ]
    mean_squared_error = sum(squared_errors) / len(squared_errors)
    return mean_squared_error
