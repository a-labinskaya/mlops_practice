from pathlib import Path

import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler


TRAIN_PATH = Path("train") / "train.csv"
TEST_PATH = Path("test") / "test.csv"
TRAIN_PREPROCESSED_DIR = Path("train") / "preprocessed"
TEST_PREPROCESSED_DIR = Path("test") / "preprocessed"
SCALER_PATH = Path("scaler.pkl")
TARGET_COLUMN = "label"


def split_features_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    return df.drop(columns=[TARGET_COLUMN]), df[TARGET_COLUMN]


def build_processed_dataframe(
    features: pd.DataFrame,
    target: pd.Series,
    feature_columns: list[str],
) -> pd.DataFrame:
    processed = pd.DataFrame(features, columns=feature_columns)
    processed[TARGET_COLUMN] = target.to_numpy()
    return processed


def main() -> None:
    TRAIN_PREPROCESSED_DIR.mkdir(exist_ok=True)
    TEST_PREPROCESSED_DIR.mkdir(exist_ok=True)

    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)

    x_train, y_train = split_features_target(train)
    x_test, y_test = split_features_target(test)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    build_processed_dataframe(x_train_scaled, y_train, list(x_train.columns)).to_csv(
        TRAIN_PREPROCESSED_DIR / "train_processed.csv",
        index=False,
    )
    build_processed_dataframe(x_test_scaled, y_test, list(x_test.columns)).to_csv(
        TEST_PREPROCESSED_DIR / "test_processed.csv",
        index=False,
    )
    with SCALER_PATH.open("wb") as file:
        pickle.dump(scaler, file)


if __name__ == "__main__":
    main()
