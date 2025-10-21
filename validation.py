"""Command-line argument validation utilities.

This module provides robust validation functions for command-line arguments,
ensuring data integrity and providing helpful error messages.
"""

import argparse
import datetime
import pathlib
import sys


class ValidationError(Exception):
    """Raised when validation fails."""

    pass


def validate_date_range(start_date: datetime.date | None, end_date: datetime.date | None) -> None:
    """Validate that start_date is not after end_date.

    Args:
        start_date: The start date to validate.
        end_date: The end date to validate.

    Raises:
        ValidationError: If start_date is after end_date.
    """
    if start_date and end_date and start_date > end_date:
        raise ValidationError(
            f"Start date {start_date} cannot be after end date {end_date}"
        )


def validate_distance_range(
    min_distance: float | None, max_distance: float | None
) -> None:
    """Validate that min_distance is not greater than max_distance.

    Args:
        min_distance: The minimum distance to validate.
        max_distance: The maximum distance to validate.

    Raises:
        ValidationError: If min_distance is greater than max_distance.
    """
    if min_distance is not None and max_distance is not None:
        if min_distance > max_distance:
            raise ValidationError(
                f"Minimum distance {min_distance} cannot be greater than "
                f"maximum distance {max_distance}"
            )
        if min_distance < 0:
            raise ValidationError(f"Minimum distance {min_distance} cannot be negative")
        if max_distance < 0:
            raise ValidationError(f"Maximum distance {max_distance} cannot be negative")


def validate_velocity_range(
    min_velocity: float | None, max_velocity: float | None
) -> None:
    """Validate that min_velocity is not greater than max_velocity.

    Args:
        min_velocity: The minimum velocity to validate.
        max_velocity: The maximum velocity to validate.

    Raises:
        ValidationError: If min_velocity is greater than max_velocity.
    """
    if min_velocity is not None and max_velocity is not None:
        if min_velocity > max_velocity:
            raise ValidationError(
                f"Minimum velocity {min_velocity} cannot be greater than "
                f"maximum velocity {max_velocity}"
            )
        if min_velocity < 0:
            raise ValidationError(f"Minimum velocity {min_velocity} cannot be negative")
        if max_velocity < 0:
            raise ValidationError(f"Maximum velocity {max_velocity} cannot be negative")


def validate_diameter_range(
    min_diameter: float | None, max_diameter: float | None
) -> None:
    """Validate that min_diameter is not greater than max_diameter.

    Args:
        min_diameter: The minimum diameter to validate.
        max_diameter: The maximum diameter to validate.

    Raises:
        ValidationError: If min_diameter is greater than max_diameter.
    """
    if min_diameter is not None and max_diameter is not None:
        if min_diameter > max_diameter:
            raise ValidationError(
                f"Minimum diameter {min_diameter} cannot be greater than "
                f"maximum diameter {max_diameter}"
            )
        if min_diameter < 0:
            raise ValidationError(f"Minimum diameter {min_diameter} cannot be negative")
        if max_diameter < 0:
            raise ValidationError(f"Maximum diameter {max_diameter} cannot be negative")


def validate_limit(limit: int | None) -> None:
    """Validate that limit is a positive integer.

    Args:
        limit: The limit value to validate.

    Raises:
        ValidationError: If limit is not a positive integer.
    """
    if limit is not None and limit <= 0:
        raise ValidationError(f"Limit {limit} must be a positive integer")


def validate_file_path(file_path: str | pathlib.Path, must_exist: bool = False) -> pathlib.Path:
    """Validate that a file path is valid and optionally exists.

    Args:
        file_path: The file path to validate.
        must_exist: Whether the file must exist.

    Returns:
        pathlib.Path: The validated path object.

    Raises:
        ValidationError: If the path is invalid or doesn't exist when required.
    """
    try:
        path = pathlib.Path(file_path)
    except (TypeError, ValueError) as e:
        raise ValidationError(f"Invalid file path '{file_path}': {e}") from e

    if must_exist and not path.exists():
        raise ValidationError(f"File '{path}' does not exist")

    if must_exist and not path.is_file():
        raise ValidationError(f"Path '{path}' is not a file")

    return path


def validate_output_file_path(file_path: str | pathlib.Path) -> pathlib.Path:
    """Validate that an output file path is valid and writable.

    Args:
        file_path: The output file path to validate.

    Returns:
        pathlib.Path: The validated path object.

    Raises:
        ValidationError: If the path is invalid or not writable.
    """
    try:
        path = pathlib.Path(file_path)
    except (TypeError, ValueError) as e:
        raise ValidationError(f"Invalid output file path '{file_path}': {e}") from e

    # Check if parent directory exists and is writable
    parent_dir = path.parent
    if not parent_dir.exists():
        try:
            parent_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise ValidationError(f"Cannot create directory '{parent_dir}': {e}") from e

    if not parent_dir.is_dir():
        raise ValidationError(f"Parent path '{parent_dir}' is not a directory")

    # Check if we can write to the parent directory
    if not path.parent.stat().st_mode & 0o200:  # Check write permission
        raise ValidationError(f"Cannot write to directory '{path.parent}'")

    return path


def validate_query_arguments(args: argparse.Namespace) -> None:
    """Validate all query arguments for consistency and validity.

    Args:
        args: The parsed command-line arguments.

    Raises:
        ValidationError: If any validation fails.
    """
    # Validate date ranges
    validate_date_range(args.start_date, args.end_date)

    # Validate distance ranges
    validate_distance_range(args.distance_min, args.distance_max)

    # Validate velocity ranges
    validate_velocity_range(args.velocity_min, args.velocity_max)

    # Validate diameter ranges
    validate_diameter_range(args.diameter_min, args.diameter_max)

    # Validate limit
    validate_limit(args.limit)

    # Validate output file if provided
    if hasattr(args, 'outfile') and args.outfile:
        validate_output_file_path(args.outfile)

    # Validate input files if provided
    if hasattr(args, 'neofile') and args.neofile:
        validate_file_path(args.neofile, must_exist=True)

    if hasattr(args, 'cadfile') and args.cadfile:
        validate_file_path(args.cadfile, must_exist=True)


def validate_inspect_arguments(args: argparse.Namespace) -> None:
    """Validate inspect command arguments.

    Args:
        args: The parsed command-line arguments.

    Raises:
        ValidationError: If any validation fails.
    """
    # Validate input files if provided
    if hasattr(args, 'neofile') and args.neofile:
        validate_file_path(args.neofile, must_exist=True)

    if hasattr(args, 'cadfile') and args.cadfile:
        validate_file_path(args.cadfile, must_exist=True)


def handle_validation_error(error: ValidationError) -> None:
    """Handle validation errors by printing them and exiting.

    Args:
        error: The validation error to handle.
    """
    print(f"Validation error: {error}", file=sys.stderr)
    sys.exit(1)
