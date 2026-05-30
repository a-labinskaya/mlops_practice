from pathlib import Path
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression


TRAIN_PATH = Path("train") / "preprocessed" / "train_processed.csv"
MODEL_PATH = Path("model.pkl")
TARGET_COLUMN = "label"
RANDOM_STATE = 42


def main() -> None:
    train = pd.read_csv(TRAIN_PATH)
    x_train = train.drop(columns=[TARGET_COLUMN])
    y_train = train[TARGET_COLUMN]

    model = LogisticRegression(
        max_iter=1000,
        random_state=RANDOM_STATE,
    )
    model.fit(x_train, y_train)

    with MODEL_PATH.open("wb") as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    main()
