def transform(df):
    df.sex = df.sex.str.upper()
    df.salary = df.salary.astype(int)
    return df
