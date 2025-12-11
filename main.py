from src.data_loader.aqi_loader import AQIDataLoader


def main() -> None:
    """
    Entry point for the project.

    For now:
    - Load a single CSV file from the data/ folder
    - Print a small preview
    """
    loader = AQIDataLoader(data_dir="data")

    # TODO: later we will replace this with a real Iran/Tehran AQI dataset.
    # For now, you can copy any CSV (e.g., AirQualityUCI.csv) into data/
    csv_filename = "AirQualityUCI.csv"  # change this name to your actual file

    try:
        loader.load_csv(csv_filename)
        loader.preview(n=5)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
    except RuntimeError as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
