import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    passes = []
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        passes.append(arr[:])
    return passes

def selection_sort(arr):
    n = len(arr)
    passes = []
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        passes.append(arr[:])
    return passes

def insertion_sort(arr):
    passes = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        passes.append(arr[:])
    return passes

def merge_sort(arr):
    passes = []
    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)
            passes.append(arr[:])

    def merge(arr, left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    merge_sort_recursive(arr, 0, len(arr) - 1)
    return passes

def quick_sort(arr):
    passes = []
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            passes.append(arr[:])
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return passes

def on_sort():
    try:
        arr = list(map(int, entry.get().split()))
        if sort_choice.get() == "Bubble Sort":
            passes = bubble_sort(arr)
        elif sort_choice.get() == "Selection Sort":
            passes = selection_sort(arr)
        elif sort_choice.get() == "Insertion Sort":
            passes = insertion_sort(arr)
        elif sort_choice.get() == "Merge Sort":
            passes = merge_sort(arr)
        elif sort_choice.get() == "Quick Sort":
            passes = quick_sort(arr)
        display_passes(passes)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid list of numbers.")

def display_passes(passes):
    pass_text.delete('1.0', tk.END)
    for i, p in enumerate(passes, start=1):
        pass_text.insert(tk.END, f"Pass {i}: {p}\n")

# Create the main window
root = tk.Tk()
root.title("Sorting Algorithms")

# Create and place the widgets
tk.Label(root, text="Enter numbers separated by spaces:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

sort_choice = tk.StringVar(value="Bubble Sort")
sort_options = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]

tk.Label(root, text="Select sorting algorithm:").pack(pady=10)
for option in sort_options:
    tk.Radiobutton(root, text=option, variable=sort_choice, value=option).pack(anchor='w')

tk.Button(root, text="Sort", command=on_sort).pack(pady=20)
pass_text = tk.Text(root, width=60, height=20)
pass_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
