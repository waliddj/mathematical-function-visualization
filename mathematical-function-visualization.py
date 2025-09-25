import numpy as np
import matplotlib.pyplot as plt

def formula(x):
    return np.sin(x)   # Define the function, example: f(x) = sin(x)

# Generate data
x = np.linspace(-10, 10, 100) #From x1 = -10 to x2 = 10, and output 100 points between x1 and x2
y = formula(x)

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(x, y, 'b-', linewidth=2, label='f(x) = sin(x)')

# Enhanced axes visibility
plt.axhline(y=0, color='black', linewidth=2, alpha=0.8)  # x-axis
plt.axvline(x=0, color='black', linewidth=2, alpha=0.8)  # y-axis

# Add axis labels with larger font
plt.xlabel('x-axis', fontsize=14, fontweight='bold')
plt.ylabel('y-axis', fontsize=14, fontweight='bold')

# Title and grid
plt.title('Graph of Mathematical Formula', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')

# Customize ticks for better visibility
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add thicker spine borders
ax = plt.gca()
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(2)    # Thicker bottom spine (x-axis)
ax.spines['left'].set_linewidth(2)      # Thicker left spine (y-axis)

plt.legend(fontsize=12)
plt.tight_layout()
plt.show()