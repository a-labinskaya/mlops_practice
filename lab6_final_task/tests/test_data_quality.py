import os
import pandas as pd


DATA_PATH = os.path.join("lab6_final_task", "data", "iris.csv")


def test_dataset_exists():
    assert os.path.exists(DATA_PATH)


def test_dataset_has_no_missing_values():
    df = pd.read_csv(DATA_PATH)
    assert df.isna().sum().sum() == 0


def test_dataset_has_target_column():
    df = pd.read_csv(DATA_PATH)
    assert "target" in df.columns


def test_dataset_has_expected_columns():
    df = pd.read_csv(DATA_PATH)
    expected_columns = {
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "target"
    }
    assert expected_columns.issubset(set(df.columns))


def test_dataset_has_enough_rows():
    df = pd.read_csv(DATA_PATH)
    assert len(df) >= 100
