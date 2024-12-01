import os

import pandas as pd
from sqlalchemy import create_engine


def db_uri():
    return os.getenv(
        "PG_URIS",
        "postgresql://relation_id_4:iDj09jAbl7qBQTgs@10.152.183.178:5432/card-transactions"
    )


if __name__ == "__main__":

    df = pd.read_csv("./data/creditcard_2023.csv", sep=",", index_col="id")
    print(df.shape)
    df = df.head(5000)
    print(df.head())

    db_url = os.getenv(
        "PG_URIS",
        "postgresql://relation_id_4:iDj09jAbl7qBQTgs@10.152.183.178:5432/card-transactions"
    )

    try:
        engine = create_engine(db_url)
        table_name = "transactions"

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=True,
            chunksize=1000,
            method="multi",
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
