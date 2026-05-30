from pathlib import Path

import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


RANDOM_STATE = 42
TEST_SIZE = 0.2
TRAIN_DIR = Path("train")
TEST_DIR = Path("test")


def main() -> None:
    TRAIN_DIR.mkdir(exist_ok=True)
    TEST_DIR.mkdir(exist_ok=True)

    digits = load_digits()
    df = pd.DataFrame(digits.data, columns=[f"pixel_{i}" for i in range(64)])
    df["label"] = digits.target

    train, test = train_test_split(
        df,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["label"],
    )

    train.to_csv(TRAIN_DIR / "train.csv", index=False)
    test.to_csv(TEST_DIR / "test.csv", index=False)


if __name__ == "__main__":
    main()
