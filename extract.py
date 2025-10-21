"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""

import csv
import json

from models import CloseApproach, NearEarthObject


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    Args:
        neo_csv_path: A path to a CSV file containing data about near-Earth objects.

    Returns:
        list: A collection of NearEarthObjects.
    """
    neos = []

    with open(neo_csv_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Extract relevant fields
            designation = row["pdes"]
            name = row["name"] if row["name"].strip() else None
            diameter = row["diameter"] if row["diameter"].strip() else None
            hazardous = row["pha"] == "Y"

            # Create NearEarthObject instance
            neo = NearEarthObject(
                designation=designation,
                name=name,
                diameter=diameter,
                hazardous=hazardous,
            )
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    Args:
        cad_json_path: A path to a JSON file containing data about close approaches.

    Returns:
        list: A collection of CloseApproaches.
    """
    approaches = []

    with open(cad_json_path, encoding="utf-8") as file:
        data = json.load(file)

    # Extract fields and data
    fields = data["fields"]
    approach_data = data["data"]

    # Map field names to indices
    des_idx = fields.index("des")
    cd_idx = fields.index("cd")
    dist_idx = fields.index("dist")
    v_rel_idx = fields.index("v_rel")

    for approach_row in approach_data:
        # Extract relevant fields
        designation = approach_row[des_idx]
        time = approach_row[cd_idx]
        distance = approach_row[dist_idx]
        velocity = approach_row[v_rel_idx]

        # Create CloseApproach instance
        approach = CloseApproach(
            designation=designation, time=time, distance=distance, velocity=velocity
        )
        approaches.append(approach)

    return approaches
