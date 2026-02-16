import numpy as np

def calculateStats(numbers):
    # Convert list to numpy array
    arr = np.array(numbers)
    
    # Calculate statistics
    mean = np.mean(arr)
    median = np.median(arr)
    stdDev = np.std(arr)
    
    # Print results
    print(f"Numbers: {numbers}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {stdDev}")
    
    # Return as dictionary
    stats = {
        'mean': mean,
        'median': median,
        'std_dev': stdDev
    }
    
    return stats


def multiplyArrays(arr1, arr2):
    # Convert to numpy arrays
    a = np.array(arr1)
    b = np.array(arr2)
    
    # Element-wise multiplication
    result = a * b
    
    print(f"{arr1} * {arr2} = {result.tolist()}")
    
    return result.tolist()


if __name__ == "__main__":
    # Test calculateStats
    print("Testing calculateStats:")
    calculateStats([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    print("\nTesting multiplyArrays:")
    multiplyArrays([1, 2, 3], [4, 5, 6])