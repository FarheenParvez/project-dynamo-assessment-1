import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_output_written():
    """Success Criterion 1: Write the output to /app/report.json."""
    assert REPORT.exists(), "Expected output file /app/report.json was not created."


def test_output_is_json_object():
    """Success Criterion 2: The output must be a single JSON object."""
    report = _load()
    assert isinstance(report, dict), "report.json must contain a single JSON object."


def test_required_keys():
    """Success Criterion 3: The JSON object must contain exactly total_requests, unique_ips, and top_path."""
    report = _load()
    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }, "report.json does not contain exactly the required keys."


def test_total_requests():
    """Success Criterion 4: total_requests equals the number of non-empty log entries."""
    report = _load()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 5: unique_ips equals the number of distinct client IP addresses."""
    report = _load()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success Criterion 6: top_path equals the most frequently requested path."""
    report = _load()
    assert report["top_path"] == "/index.html"