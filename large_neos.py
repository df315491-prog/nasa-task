from tabulate import tabulate

def show_large_neos(neos, min_size=50):
    
    # Prints all NEOs with a maximum diameter >= min_size meters
    
    large_neos = []
    for n in neos:
        # Extract max diameter from the "Diameter (m)" string
        try:
            max_d = float(n["Diameter (m)"].split(" - ")[1])
        except:
            continue  
        if max_d >= min_size:
            large_neos.append(n)

    if not large_neos:
        print(f"No NEOs found with diameter >= {min_size} meters.")
        return

    # output 10 at a time
    page_size = 10
    total = len(large_neos)
    for i in range(0, total, page_size):
        print(f"\n=== Showing NEOs {i + 1} to {min(i + page_size, total)} of {total} ===\n")
        print(tabulate(large_neos[i:i+page_size], headers="keys", tablefmt="fancy_grid"))
        if i + page_size < total:
            input("Press Enter to see the next page...")
