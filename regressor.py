u"""
author: atreya
desc:
"""

from __future__ import absolute_import
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

target_variable = [u"Sales"]


def train_model_ridge(dataframe):
    model_object = {}
    print u"Training Ridge Regression"
    print dataframe.columns.tolist()
    ridge = linear_model.Ridge(alpha=0.5)
    X_train, X_test, y_train, y_test = train_test_split(dataframe.drop(target_variable, axis=1),
                                                        dataframe.Sales)
    model = ridge.fit(X_train, y_train)
    model.fit(X_train, y_train)
    model_object[u"model"] = model
    model_object[u"training_features"] = X_train.columns.tolist()
    return model_object


def train_model_with_grid_search(dataframe):
    print u"Training Ridge Regression"
    print dataframe.columns
    ridge = linear_model.Ridge()
    params_grid = {
        u"alpha": [0.01, 0.05, 0.1, 0.5]
    }
    X_train, X_test, y_train, y_test = train_test_split(dataframe.drop(target_variable, axis=1),
                                                        dataframe.Sales)
    model = GridSearchCV(ridge, param_grid=params_grid, verbose=2, cv=5, refit=True, n_jobs=5)
    model.fit(X_train, y_train)
    return model.best_estimator_


def train_random_forest(dataframe):
    X_train, X_test, y_train, y_test = train_test_split(dataframe.drop(target_variable, axis=1),
                                                        dataframe.Sales)
    print u"Training Random Forest"
    rf = RandomForestRegressor(n_estimators=100, criterion=u'mse', n_jobs=5,verbose=2)
    rf.fit(X_train, y_train)
    return rf


def test_model_ridge(dataframe,model):
    df = dataframe.drop(target_variable, axis=1)
    return model.predict(df)

if __name__ == u'__main__':
    pass
