class Solution: 
    def select(self, arr, i):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        return min_idx

    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            min_idx = self.select(arr, i)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
