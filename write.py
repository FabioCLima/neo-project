"""Write a stream of close approaches to CSV or to JSON.

This module exports functions for writing close approach data to files,
including streaming-friendly JSON output and improved error handling.

The main functions are write_to_csv and write_to_json, each of
which accept a results stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the limit
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.
"""

import csv
import json
import sys
from collections.abc import Iterable
from pathlib import Path


def write_to_csv(results: Iterable, filename: str | Path) -> None:
    """Write an iterable of CloseApproach objects to a CSV file.

    The precise output specification is in README.md. Roughly, each output row
    corresponds to the information in a single close approach from the results
    stream and its associated near-Earth object.

    Args:
        results: An iterable of CloseApproach objects.
        filename: A Path-like object pointing to where the data should be saved.

    Raises:
        IOError: If the file cannot be written.
        ValueError: If the data cannot be serialized.
    """
    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for approach in results:
                try:
                    data = approach.serialize()
                    # Flatten the nested neo data for CSV
                    row = {
                        "datetime_utc": data["datetime_utc"],
                        "distance_au": data["distance_au"],
                        "velocity_km_s": data["velocity_km_s"],
                        "designation": data["neo"]["designation"],
                        "name": data["neo"]["name"],
                        "diameter_km": data["neo"]["diameter_km"],
                        "potentially_hazardous": data["neo"]["potentially_hazardous"],
                    }
                    writer.writerow(row)
                except (AttributeError, KeyError) as e:
                    print(f"Warning: Skipping invalid approach data: {e}", file=sys.stderr)
                    continue
    except OSError as e:
        raise OSError(f"Failed to write CSV file {filename}: {e}") from e


def write_to_json(results: Iterable, filename: str | Path) -> None:
    """Write an iterable of CloseApproach objects to a JSON file.

    The precise output specification is in README.md. Roughly, the output is a
    list containing dictionaries, each mapping CloseApproach attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    Args:
        results: An iterable of CloseApproach objects.
        filename: A Path-like object pointing to where the data should be saved.

    Raises:
        IOError: If the file cannot be written.
        ValueError: If the data cannot be serialized.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("[\n")
            first = True

            for approach in results:
                try:
                    if not first:
                        file.write(",\n")
                    else:
                        first = False

                    data = approach.serialize()
                    json.dump(data, file, indent=2, separators=(',', ': '))
                except (AttributeError, TypeError) as e:
                    print(f"Warning: Skipping invalid approach data: {e}", file=sys.stderr)
                    continue

            file.write("\n]")
    except OSError as e:
        raise OSError(f"Failed to write JSON file {filename}: {e}") from e


def write_to_json_streaming(results: Iterable, filename: str | Path) -> None:
    """Write an iterable of CloseApproach objects to a JSON file using streaming.

    This function writes data incrementally, making it memory-efficient for
    large datasets. The output is a JSON array with each approach as a separate
    object.

    Args:
        results: An iterable of CloseApproach objects.
        filename: A Path-like object pointing to where the data should be saved.

    Raises:
        IOError: If the file cannot be written.
        ValueError: If the data cannot be serialized.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("[\n")
            first = True

            for approach in results:
                try:
                    if not first:
                        file.write(",\n")
                    else:
                        first = False

                    data = approach.serialize()
                    json.dump(data, file, indent=2, separators=(',', ': '))
                    file.flush()  # Ensure data is written immediately
                except (AttributeError, TypeError) as e:
                    print(f"Warning: Skipping invalid approach data: {e}", file=sys.stderr)
                    continue

            file.write("\n]")
    except OSError as e:
        raise OSError(f"Failed to write streaming JSON file {filename}: {e}") from e
