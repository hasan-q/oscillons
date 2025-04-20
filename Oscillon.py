import matplotlib.pyplot as plt
import numpy as np

# Initialize graph
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 10))
fig.text(0.5, 0.05, "Oscillon", ha = 'center', va = 'center', fontsize = 14)
ax.axis('off')

# Create the number of harmonographs to be plotted
num_layers = -1
try:
    num_layers = int(input("Enter the amount of curves to be generated: "))
except ValueError:
    print("Please enter a number.")

# Create the values for the frequency variable
step = -1
try:
    step = float(input("Enter a frequency between 0 and 1: "))
except ValueError:
    print("Please enter a number.")
else:
    if step <= 0.0 or step > 1.0:
        print("Please enter a number in between 0 and 1.")

f_choice = []
if step != -1:
    i = 0
    while i <= 3.5:
        f_choice.append(i)
        i += step

# Create the line-width of the plot
line_width = -1
try:
    line_width = float(input("Enter a line width between 0 and 1: "))
except ValueError:
    print("Please enter a number.")
else:
    if line_width <= 0.0 or line_width > 1.0:
        print("Please enter a number in between 0 and 1.")

# Create the color / color scheme of the plot
cmap = None
use_cmap = False
color = 'white'
color_name = input("Enter a color scheme or color: ")

if color_name in plt.colormaps():
    cmap = plt.get_cmap(color_name)
    use_cmap = True
else:
    use_cmap = False
    try:
        color = color_name
    except ValueError:
        print("Color/color scheme does not exist.")

t = np.logspace(1, 2.6, 50000)

# Create randomly generated variables for each oscillon
if num_layers != -1:
    for i in range(num_layers):
        A = []
        f = []
        p = []
        d = []

        for j in range(4):
            A.append(np.random.uniform(1, 4))
            f.append(np.random.choice(f_choice))
            p.append(np.random.uniform(0, 2*np.pi))
            d.append(np.random.uniform(0.001, 0.004))

        # Create equations for the harmonograph
        x = (A[0] * np.sin(t * f[0] + p[0]) * np.pow(np.e, (-d[0] * t)) +
             A[1] * np.sin(t * f[1] + p[1]) * np.pow(np.e, (-d[1] * t)))
        y = (A[2] * np.sin(t * f[2] + p[2]) * np.pow(np.e, (-d[2] * t)) +
             A[3] * np.sin(t * f[3] + p[3]) * np.pow(np.e, (-d[3] * t)))

        if use_cmap:
            color = cmap(i / num_layers)

        ax.plot(x, y, linewidth = line_width, alpha = max(0.9 - num_layers * 0.1, 0.3), color = color)

plt.show()
