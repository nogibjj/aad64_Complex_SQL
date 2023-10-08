"""
ETL-Query script
"""
import fire
from mylib.data import run_queries_from_file


def final():
    """runs the final query"""
    run_queries_from_file("data.sql", "results.md")


if __name__ == "__main__":
    fire.Fire(final)
