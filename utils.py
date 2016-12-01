from sklearn.model_selection import cross_val_score
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
    return map(lambda x: float(x - min_value) / denominator, feature_vector)


def rescale_features(features, df, non_scaled=[]):
    '''
    Params:
        features: a the list of feature names
        df: dataframe that contains the features
        non_scaled: (default=[]) features to not scale
    return: a dataframe with the features rescaled
    '''
    for feature in features:
        if feature not in non_scaled:
            df[feature] = rescale(df[feature])
    return df


def get_cross_validated_score(X, y, clf, n_permutations=5):
    '''
    Wraps sklearn cross_val_score by properly reshaping the matrix and computing average.
    Params:
        X - matrix of feature values (df[features])
        y - vector of target values (df[target])
        clf - the classifier to test against
        n_permutations - number of splits to run
    Return:
        mean - the mean score for the classifier
        std - the standard deviation of the dataset
    '''
    y = y.as_matrix()
    y = y.reshape(y.shape[0],)
    scores = cross_val_score(clf, X, y, cv=n_permutations)
    return scores.mean(), scores.std()



def make_advanced_data(shots_data, players_data, features):
    '''
    Grabs the features of interest from the player data
    '''
    advanced_data = {f: [] for f in features}
    for index, shot in shots_data.iterrows():
        pid = shot['player_id']
        player = players_data[players_data['PLAYER_ID'] == pid]
        for feature in features:
            print player[feature]
            advanced_data[feature].append(player[feature].values[0])
    for key, val in advanced_data.items():
        shots_data[key] = val
    return shots_data

