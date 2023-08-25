import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class SnellsLawSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Snell's Law Simulator")

        self.create_widgets()

    def create_widgets(self):
        self.angle_label = ttk.Label(self.root, text="Incident Angle (degrees):")
        self.angle_label.pack()

        self.angle_var = tk.DoubleVar()
        self.angle_entry = ttk.Entry(self.root, textvariable=self.angle_var)
        self.angle_entry.pack()

        self.n1_label = ttk.Label(self.root, text="Refractive Index Medium 1:")
        self.n1_label.pack()

        self.n1_var = tk.DoubleVar()
        self.n1_entry = ttk.Entry(self.root, textvariable=self.n1_var)
        self.n1_entry.pack()

        self.n2_label = ttk.Label(self.root, text="Refractive Index Medium 2:")
        self.n2_label.pack()

        self.n2_var = tk.DoubleVar()
        self.n2_entry = ttk.Entry(self.root, textvariable=self.n2_var)
        self.n2_entry.pack()

        self.simulate_button = ttk.Button(self.root, text="Simulate", command=self.run_simulation)
        self.simulate_button.pack()

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def run_simulation(self):
        incident_angle_deg = self.angle_var.get()
        n1 = self.n1_var.get()
        n2 = self.n2_var.get()

        incident_angle_rad = np.radians(incident_angle_deg)
        transmitted_angle_rad = np.arcsin(n1 / n2 * np.sin(incident_angle_rad))

        reflection_coefficient = ((n1 * np.cos(incident_angle_rad) - n2 * np.cos(transmitted_angle_rad)) /
                                  (n1 * np.cos(incident_angle_rad) + n2 * np.cos(transmitted_angle_rad)))**2

        transmitted_intensity = 1 - reflection_coefficient
        reflection_intensity = reflection_coefficient

        self.ax.clear()

        self.ax.plot([-0.75, 0.75], [0, 0], 'k-', label="Media Division")
        self.ax.plot([0, 0], [-1.5, 1.5], 'k--', label="Normal Line")
        self.ax.annotate("Medium Division", xy=(-1.45, 0), fontsize=12, ha='left', va='center')
        self.ax.annotate("Medium 1", xy=(1, 1), fontsize=12, ha='left', va='center')
        self.ax.annotate("Medium 2", xy=(1, -1), fontsize=12, ha='left', va='center')
        self.ax.annotate("Normal", xy= (-.1,1),fontsize=12, ha='right',va='center' )
        # Incident ray
        self.ax.plot([0, 1], [0, np.tan(incident_angle_rad)], 'b', label="Incident Ray")
        # Reflected ray
        self.ax.plot([0, 1], [0, -np.tan(incident_angle_rad)], 'r', label="Reflected Ray")
        # Transmitted ray
        self.ax.plot([0, -1], [0, np.tan(transmitted_angle_rad)], 'g', label="Transmitted Ray")

        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-0.5, 0.5)
        self.ax.set_aspect('equal', adjustable='datalim')

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_title("Snell's Law Simulation")
        self.ax.legend()
        self.ax.grid(True)

        reflected_result_label = f"Reflection Intensity: {reflection_intensity:.2f}"
        self.ax.text(0.1, -0.75, reflected_result_label, fontsize=12, ha='left', va='bottom',color='r')
        transmitted_result_label = f"Transmitted Intensity: {transmitted_intensity:.2f}"
        self.ax.text(0.1, -0.9, transmitted_result_label, fontsize=12, ha='left', va='bottom',color='b')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SnellsLawSimulator(root)
    root.mainloop()
