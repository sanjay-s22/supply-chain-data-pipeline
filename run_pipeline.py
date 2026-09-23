import subprocess
import sys


def run_step(name, command, cwd="."):
    print(f"\n{'=' * 60}")
    print(f"RUNNING: {name}")
    print(f"{'=' * 60}\n")

    result = subprocess.run(command, cwd=cwd)

    if result.returncode != 0:
        print(f"\n {name} failed.")
        sys.exit(result.returncode)

    print(f"\n {name} completed.")


def main():
    run_step(
        "PySpark ETL",
        [sys.executable, "-m", "src.main"],
    )

    run_step(
        "Snowflake Load",
        [sys.executable, "src/load_snowflake.py"],
    )

    run_step(
        "dbt Build",
        ["dbt", "build"],
        cwd="dbt_supply_chain",
    )

    print("\n" + "=" * 60)
    print(" PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()