from pathlib import Path
import pickle

import pandas as pd
from sklearn.metrics import accuracy_score


TEST_PATH = Path("test") / "preprocessed" / "test_processed.csv"
MODEL_PATH = Path("model.pkl")
TARGET_COLUMN = "label"

def main() -> None:
    test = pd.read_csv(TEST_PATH)
    x_test = test.drop(columns=[TARGET_COLUMN])
    y_test = test[TARGET_COLUMN]

    with MODEL_PATH.open("rb") as file:
        model = pickle.load(file)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Model test accuracy is: {accuracy:.3f}")


if __name__ == "__main__":
    main()
