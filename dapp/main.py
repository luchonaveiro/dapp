from dapp.constants import RESOURCES_DIR
from dapp.data.load import load_csv
from dapp.data.transform import transform


def main():
    path = RESOURCES_DIR / "data.csv"
    data = transform(load_csv(path))
    return data


if __name__ == "__main__":
    df1 = main()
    print(df1)
