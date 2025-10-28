from nbclient import NotebookClient
import nbformat
from pathlib import Path


def main():
    print("Hello from apache-spark-demo!")

    notebook_files = Path(".").glob("*.ipynb")
    for nb_file in notebook_files:
        print(f"Running notebook: {nb_file}")
        nb = nbformat.read(nb_file, as_version=4)
        client = NotebookClient(nb)
        client.execute()
        nbformat.write(nb, nb_file.open("w", encoding="utf-8"))


if __name__ == "__main__":
    main()
