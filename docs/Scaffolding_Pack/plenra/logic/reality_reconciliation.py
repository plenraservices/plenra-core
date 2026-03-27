from __future__ import annotations


def reconcile_reality(*, expected: dict, observed: dict) -> dict:
    mismatches = []
    for key, expected_value in expected.items():
        observed_value = observed.get(key)
        if observed_value != expected_value:
            mismatches.append(
                {
                    "field": key,
                    "expected": expected_value,
                    "observed": observed_value,
                }
            )
    return {
        "status": "aligned" if not mismatches else "drift_detected",
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }
