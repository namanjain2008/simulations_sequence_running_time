import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to create the plot
def create_plot():
    # Create a figure and an axis
    fig, ax = plt.subplots()
    
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    
    # Plot data
    ax.plot(x, y, marker='o')
    
    # Set title and labels
    ax.set_title('Simple Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    
    return fig

# Create the main window
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Create a frame for the plot
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Create the plot
fig = create_plot()

# Create a canvas and add the plot to the canvas
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()

# Pack the canvas into the frame
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

# Start the Tkinter main loop
root.mainloop()