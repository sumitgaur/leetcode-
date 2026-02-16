# Input file with each line having a city code and temperature of the city in Celsius, separated by a comma
#
# E.g Input
# DL, 30
# BOM, 32
# DL, 31
# CCU, 29
# HYD, 25
# DL, 32
# DL, 20
#
# Output:
# DL: 30/31/30.5
# BOM:32/32/32
#
# Return min, max and average temperature of each city in the file
# File can have millions of lines in it but the program will be running on a machine with 4 CPU cores
import os
import multiprocessing as mp
from collections import defaultdict


def process_chunk(filename, start, end):
    stats = defaultdict(lambda: {
        "min": float("inf"),
        "max": float("-inf"),
        "sum": 0,
        "count": 0
    })

    with open(filename, "r") as f:
        f.seek(start)

        # Skip partial line if not at file start
        if start != 0:
            f.readline()

        while f.tell() < end:
            line = f.readline()
            if not line:
                break

            city, temp = line.strip().split(",")
            temp = int(temp)

            s = stats[city]
            s["min"] = min(s["min"], temp)
            s["max"] = max(s["max"], temp)
            s["sum"] += temp
            s["count"] += 1

    return stats


def merge_results(results):
    final = defaultdict(lambda: {
        "min": float("inf"),
        "max": float("-inf"),
        "sum": 0,
        "count": 0
    })

    for result in results:
        for city, stats in result.items():
            f = final[city]
            f["min"] = min(f["min"], stats["min"])
            f["max"] = max(f["max"], stats["max"])
            f["sum"] += stats["sum"]
            f["count"] += stats["count"]

    return final


if __name__ == "__main__":
    filename = "temperature.csv"
    cpu_count = os.cpu_count() or 4
    file_size = os.path.getsize(filename)

    chunk_size = file_size // cpu_count
    chunks = []

    for i in range(cpu_count):
        start = i * chunk_size
        end = file_size if i == cpu_count - 1 else (i + 1) * chunk_size
        chunks.append((filename, start, end))

    with mp.Pool(cpu_count) as pool:
        results = pool.starmap(process_chunk, chunks)

    final_stats = merge_results(results)

    for city, s in final_stats.items():
        avg = s["sum"] / s["count"]
        print(f"{city}: {s['min']}/{s['max']}/{avg:.2f}")

