import os

RESULTS_PATH = "./results"

os.makedirs(RESULTS_PATH, exist_ok=True)


def export(spark_df, name):
    pandas_df = spark_df.toPandas()
    export_to_excel(pandas_df, name)
    export_to_tsv(pandas_df, name)


def export_to_excel(pandas_df, name):
    pandas_df.to_excel(f"{RESULTS_PATH}/{name}.xlsx", index=False)


def export_to_tsv(pandas_df, name):
    pandas_df.to_csv(f"{RESULTS_PATH}/{name}.tsv", sep="\t", index=False)
