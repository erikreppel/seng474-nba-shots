# A library on small functions to help us out
# Normalization functions


# Normalize shot_clock TODO: choose to keep nans or not?
def normalize_shotclock(times):
    times = times / 24.0
    for i, t in enumerate(times):
        if str(t) == 'nan':  # there has to be a better way to do this...
            times[i] = 0.0
    return times


# Normalize locations to numeric value
def normalize_location(locations):
    return [-1 if x == 'A' else 1 for x in locations]


# Maps all value to the range of [0, 1]
def rescale(feature_vector):
    max_value = max(feature_vector)
    min_value = min(feature_vector)
    denominator = max_value - min_value
    return map(lambda x: (x - min_value) / denominator, feature_vector)


def rescale_features(features, df)
    '''
    Params:
        features: a the list of feature names
        df: dataframe that contains the features
    return: a dataframe with the features rescaled
    '''
    for feature in features:
        df[feature] = rescale(df[feature])
    return df
