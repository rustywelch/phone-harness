"""Telemetry is disabled in Rusty's personal phone-harness fork.

The upstream project can collect CLI input, output, and helper arguments.
Those values can contain OCR text or content typed into the mirrored phone,
so this fork deliberately provides a no-op implementation. Keeping the
public call surface lets the rest of the upstream CLI remain easy to merge.
"""

from __future__ import annotations


def is_enabled() -> bool:
    """Return False unconditionally; config and environment cannot enable it."""
    return False


def capture_cli_event(**_event) -> None:
    """Discard an event locally without creating an identifier or network call."""
    return None
