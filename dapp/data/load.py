import pandas as pd

from dapp.constants import RESOURCES_DIR


def load_csv(path):
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    path = RESOURCES_DIR / "data.csv"
    df = load_csv(path)
    print(df)
