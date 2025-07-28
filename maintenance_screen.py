import tkinter as tk
from tkinter import ttk

def open_maintenance_screen(root):
    maintenance_win = tk.Toplevel(root)
    maintenance_win.title("Maintenance Management")
    tk.Label(maintenance_win, text="Maintenance Screen").pack(padx=20, pady=20)