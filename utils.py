import os

RESULTS_PATH = "./results"

os.makedirs(RESULTS_PATH, exist_ok=True)


def build_result_filename(name, extension="tsv"):
    return f"{RESULTS_PATH}/{name}.{extension}"


def export(spark_df, name):
    pandas_df = spark_df.toPandas()
    export_to_excel(pandas_df, name)
    export_to_tsv(pandas_df, name)


def export_to_excel(pandas_df, name):
    pandas_df.to_excel(build_result_filename(name, extension="xlsx"), index=False)


def export_to_tsv(pandas_df, name):
    pandas_df.to_csv(build_result_filename(name), sep="\t", index=False)


def read(session, name):
    return session.read.csv(build_result_filename(name), sep="\t", header=True)
