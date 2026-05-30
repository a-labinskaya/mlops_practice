import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def make_clean_data(seed, n=100):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = 3 * x + 5 + rng.normal(0, 0.5, n)
    return x.reshape(-1, 1), y


def make_noisy_data(seed, n=100):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = rng.normal(0, 20, n)
    return x.reshape(-1, 1), y


def train_model():
    x, y = make_clean_data(1)
    model = LinearRegression()
    model.fit(x, y)
    joblib.dump(model, "lab5/model.pkl")
    return model


def test_model_on_clean_dataset_1():
    model = train_model()
    x, y = make_clean_data(2)
    score = r2_score(y, model.predict(x))
    assert score > 0.90


def test_model_on_clean_dataset_2():
    model = train_model()
    x, y = make_clean_data(3)
    score = r2_score(y, model.predict(x))
    assert score > 0.90


def test_model_on_clean_dataset_3():
    model = train_model()
    x, y = make_clean_data(4)
    score = r2_score(y, model.predict(x))
    assert score > 0.90


def test_model_detects_noisy_dataset():
    model = train_model()
    x, y = make_noisy_data(5)
    score = r2_score(y, model.predict(x))
    assert score < 0.50
