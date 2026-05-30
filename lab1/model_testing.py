from pathlib import Path
import pickle

import pandas as pd
from sklearn.metrics import accuracy_score


TEST_PATH = Path("test") / "preprocessed" / "test_processed.csv"
MODEL_PATH = Path("model.pkl")
TARGET_COLUMN = "label"
MIN_ACCURACY = 0.90


def main() -> None:
    test = pd.read_csv(TEST_PATH)
    x_test = test.drop(columns=[TARGET_COLUMN])
    y_test = test[TARGET_COLUMN]

    with MODEL_PATH.open("rb") as file:
        model = pickle.load(file)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)

    if accuracy < MIN_ACCURACY:
        raise RuntimeError(
            f"Model accuracy {accuracy:.4f} is lower than required {MIN_ACCURACY:.2f}"
        )

    print(f"Model test accuracy is: {accuracy:.3f}")


if __name__ == "__main__":
    main()
