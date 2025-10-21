"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(
        self, designation="", name=None, diameter=float("nan"), hazardous=False
    ):
        """Create a new NearEarthObject.

        Args:
            designation: The primary designation of the NEO (required).
            name: The IAU name of the NEO (optional).
            diameter: The diameter in kilometers (optional, use float('nan') if unknown).
            hazardous: Whether the NEO is potentially hazardous.
        """
        # Assign information from the arguments passed to the constructor
        self.designation = str(designation) if designation else ""
        self.name = name if name and name.strip() else None
        self.diameter = (
            float(diameter) if diameter and str(diameter).strip() else float("nan")
        )
        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO.

        Returns:
            str: The full name combining designation and IAU name.
        """
        if self.name:
            return f"{self.designation} ({self.name})"
        return self.designation

    def __str__(self):
        """Return string representation of this NEO.

        Returns:
            str: Human-readable description of the NEO.
        """
        hazardous_text = (
            "is potentially hazardous"
            if self.hazardous
            else "is not potentially hazardous"
        )
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and {hazardous_text}."

    def serialize(self):
        """Return a dictionary representation of this NEO for serialization.

        Returns:
            dict: Dictionary containing NEO data for JSON/CSV export.
        """
        return {
            "designation": self.designation,
            "name": self.name if self.name else "",
            "diameter_km": self.diameter
            if not (self.diameter != self.diameter)
            else float("nan"),  # Check for NaN
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation="", time=None, distance=0.0, velocity=0.0):
        """Create a new CloseApproach.

        Args:
            designation: The primary designation of the NEO making the approach.
            time: The time of close approach (NASA format string).
            distance: The nominal approach distance in astronomical units.
            velocity: The relative approach velocity in kilometers per second.
        """
        # Assign information from the arguments passed to the constructor
        self._designation = str(designation) if designation else ""
        self.time = cd_to_datetime(time) if time else None
        self.distance = float(distance) if distance else 0.0
        self.velocity = float(velocity) if velocity else 0.0

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this CloseApproach's approach time.

        The value in self.time should be a Python datetime object. While a
        datetime object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The datetime_to_str method converts a datetime object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.

        Returns:
            str: Formatted datetime string.
        """
        return datetime_to_str(self.time) if self.time else ""

    def __str__(self):
        """Return string representation of this CloseApproach.

        Returns:
            str: Human-readable description of the close approach.
        """
        neo_name = self.neo.fullname if self.neo else self._designation
        return f"On {self.time_str}, '{neo_name}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def serialize(self):
        """Return a dictionary representation of this CloseApproach for serialization.

        Returns:
            dict: Dictionary containing close approach data for JSON/CSV export.
        """
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
            "neo": self.neo.serialize()
            if self.neo
            else {
                "designation": self._designation,
                "name": "",
                "diameter_km": float("nan"),
                "potentially_hazardous": False,
            },
        }
