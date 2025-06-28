import logging
import time
from contextlib import contextmanager

_timings = []

@contextmanager
def track_time(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - start
        _timings.append((label, duration))
        logging.info(f"\u23F1 {label} took {duration:.2f}s")

def reset_timings():
    _timings.clear()

def report_timings():
    if not _timings:
        logging.info("No timing data recorded")
        return
    logging.info("=== Timing Summary ===")
    totals = {}
    counts = {}
    for label, dur in _timings:
        totals[label] = totals.get(label, 0.0) + dur
        counts[label] = counts.get(label, 0) + 1
    for label, total in totals.items():
        count = counts[label]
        avg = total / count
        logging.info(f"{label}: {total:.2f}s over {count} run(s) (avg {avg:.2f}s)")
