def partition(data, low, high):
  pivot = data[high]  # Choose the last element as the pivot
  i = low - 1  # Index of smaller element

  for j in range(low, high):
    # Check if current element is smaller than the pivot
    if data[j] <= pivot:
      i += 1
      data[i], data[j] = data[j], data[i]  # Swap elements

  data[i + 1], data[high] = data[high], data[i + 1]  # Put the pivot in its final place
  print("Partitioned array:", data)  # Print the partitioned array
  return i + 1

def quick_sort(data, low, high):
  if low < high:
    # pi is partitioning index, data[p] is now at right place
    pi = partition(data, low, high)

    # Recursively sort elements before and after partition
    quick_sort(data, low, pi - 1)
    quick_sort(data, pi + 1, high)



data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("Unsorted data:", data)
quick_sort(data, 0, len(data) - 1)
print("Sorted data:", data)
