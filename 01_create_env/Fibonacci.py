import numpy as np
import matplotlib.pyplot as plt

# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

# Generate first 100 Fibonacci numbers
n = 100
fib_numbers = fibonacci(n)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(range(n), fib_numbers, 'b-', linewidth=1.5)
plt.scatter(range(n), fib_numbers, c='red', s=30, alpha=0.6)
plt.title('First 100 Fibonacci Numbers', fontsize=16)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)

# Add a log scale for y-axis to better visualize the exponential growth
plt.yscale('log')
plt.tight_layout()

# Show the plot
plt.show()

# Print the first few and last few numbers for reference
print(f"First 10 Fibonacci numbers: {fib_numbers[:10]}")
print(f"Last 5 Fibonacci numbers: {fib_numbers[-5:]}")
