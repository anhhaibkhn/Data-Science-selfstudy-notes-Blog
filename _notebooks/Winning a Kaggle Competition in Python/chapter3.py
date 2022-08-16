""" Run this file to understand How Target Encoding works """
from sklearn.model_selection import KFold
import pandas as pd
import numpy as np 
import os


def test_mean_target_encoding(train, test, target, categorical, alpha=5):
    # Calculate global mean on the train data
    global_mean = train[target].mean()
    
    # Group by the categorical feature and calculate its properties
    train_groups = train.groupby(categorical)
    category_sum = train_groups[target].sum()
    category_size = train_groups.size()
    
    # Calculate smoothed mean target statistics
    train_statistics = (category_sum + global_mean * alpha) / (category_size + alpha)
    
    # Apply statistics to the test data and fill new categories
    test_feature = test[categorical].map(train_statistics).fillna(global_mean)
    return test_feature.values


def train_mean_target_encoding(train, target, categorical, alpha=5):
    # Create 5-fold cross-validation
    kf = KFold(n_splits=5,random_state=123, shuffle=True)
    train_feature = pd.Series(index=train.index, dtype='float')
    
    # For each folds split
    for train_index, test_index in kf.split(train):
        cv_train, cv_test = train.iloc[train_index], train.iloc[test_index]
        
        # Calculate out-of-fold statistics and apply to cv_test
        cv_test_feature = test_mean_target_encoding(cv_train, cv_test, target, 
                                                    categorical, alpha)
        
        # Save new feature for this particular fold
        train_feature.iloc[test_index] = cv_test_feature
    return train_feature.values


def mean_target_encoding(train, test, target, categorical, alpha=5):
    # Get the train feature
    train_feature = train_mean_target_encoding(train, target, categorical, alpha)
    
    # Get the test feature
    test_feature = test_mean_target_encoding(train, test, target, categorical, alpha)
    
    # Return new features to add to the model
    return train_feature, test_feature



if __name__ == "__main__":
    #Get Current working Directory
    currentFileDirectory = os.path.dirname(os.path.abspath(__file__))

    bryant_shots = pd.read_csv(currentFileDirectory +'/datasets/bryant_shots.csv')

    # Create 5-fold cross-validation
    kf = KFold(n_splits=5, random_state=123, shuffle=True)

    # For each folds split
    for train_index, test_index in kf.split(bryant_shots):
        cv_train, cv_test = bryant_shots.iloc[train_index].copy(), bryant_shots.iloc[test_index].copy()
        
        # Create mean target encoded feature
        cv_train['game_id_enc'], cv_test['game_id_enc'] = mean_target_encoding(train=cv_train,
                                                                            test=cv_test,
                                                                            target='shot_made_flag',
                                                                            categorical='game_id',
                                                                            alpha=5)
        
        # Look at the encoding
        print(cv_train[['game_id', 'shot_made_flag', 'game_id_enc']].sample(n=1))