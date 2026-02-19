import time
import random
import matplotlib.pyplot as plt

# ---------------- Bubble Sort ----------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ---------------- Quick Sort ----------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# ---------------- Main Program ----------------
if __name__ == "__main__":

    # Input sizes to test
    input_sizes = [100, 300, 500, 700, 900]

    # Lists to store time results
    bubble_times = []
    quick_times = []

    # Run the sorting algorithms
    for size in input_sizes:
        data = random.sample(range(10000), size)

        # Bubble Sort timing
        arr1 = data.copy()
        start = time.time()
        bubble_sort(arr1)
        bubble_times.append(time.time() - start)

        # Quick Sort timing
        arr2 = data.copy()
        start = time.time()
        quick_sort(arr2)
        quick_times.append(time.time() - start)

        print(f"Completed test for size: {size}")

    # ---------------- Plot the Graph ----------------
    plt.plot(input_sizes, bubble_times, marker='o', label="Bubble Sort")
    plt.plot(input_sizes, quick_times, marker='o', label="Quick Sort")

    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Bubble Sort vs Quick Sort Performance")
    plt.legend()
    plt.grid(True)

    # ---------------- Save the Graph ----------------
    plt.savefig("sorting_comparison_graph.png")  # Saves PNG file
    plt.savefig("sorting_comparison_graph.pdf")  # Optional PDF version

    print("\nGraph saved as 'sorting_comparison_graph.png' and 'sorting_comparison_graph.pdf'.")

    # Show the graph window
    plt.show()