import papermill as pm
from pathlib import Path
from utils import RESULTS_PATH


def main():
    print("Hello from apache-spark-demo!")

    output_dir = Path(RESULTS_PATH)
    notebook_files = Path(".").glob("*.ipynb")
    for nb_file in notebook_files:
        output_path = output_dir / nb_file.name
        print(f"Running notebook: {nb_file}")
        pm.execute_notebook(
            input_path=str(nb_file),
            output_path=str(output_path),
            parameters=dict(plant="9"),
        )


if __name__ == "__main__":
    main()
