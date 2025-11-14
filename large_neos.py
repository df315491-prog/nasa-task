from tabulate import tabulate
from config import MIN_DIAMETER, PAGE_SIZE


def show_large_neos(neos, min_size=MIN_DIAMETER):
    '''Display NEOs with a minimum diameter greater than or equal to 50m
    Args:
        neos (list): List of NEOs
        min_size (int): Minimum diameter in meters
    '''    

    large_neos = []
    for n in neos:
        try:
            min_d = float(n["Diameter (m)"].split(" - ")[0])
        except:
            continue
        if min_d >= min_size:
            large_neos.append(n)

    if not large_neos:
        print(f"No NEOs found with minimum diameter >= {min_size} meters.")
        return

    # output 10 at a time
    total = len(large_neos)
    for i in range(0, total, PAGE_SIZE):
        print(f"\n=== Showing NEOs {i + 1} to {min(i + PAGE_SIZE, total)} of {total} ===\n")
        print(tabulate(large_neos[i:i+PAGE_SIZE], headers="keys", tablefmt="fancy_grid"))
        if i + PAGE_SIZE < total:
            input("Press Enter to see the next page...")
