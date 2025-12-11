from pathlib import Path
from typing import Optional

import pandas as pd


class AQIDataLoader:
    """
    Air Quality (AQI) data loader.

    Responsibilities:
    - Manage the data directory
    - Load a CSV file with air quality / weather data
    - Provide simple preview helpers
    """

    def __init__(self, data_dir: str = "data") -> None:
        self.data_dir = Path(data_dir)
        self.raw_df: Optional[pd.DataFrame] = None

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load a CSV file from the data directory.

        Parameters
        ----------
        filename : str
            Name of the CSV file inside the data directory.

        Returns
        -------
        pd.DataFrame
            Loaded DataFrame.

        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        RuntimeError
            If pandas fails to read the CSV file.
        """
        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        try:
            df = pd.read_csv(file_path)
        except Exception as e:  # generic read error
            raise RuntimeError(f"Failed to read CSV file: {file_path}") from e

        self.raw_df = df
        return df

    def preview(self, n: int = 5) -> None:
        """
        Print a small preview of the loaded DataFrame.
        """
        if self.raw_df is None:
            print("No data loaded yet. Call `load_csv(...)` first.")
            return

        print("\n=== Data preview ===")
        print(self.raw_df.head(n))
        print("\n=== DataFrame info ===")
        print(self.raw_df.info())
