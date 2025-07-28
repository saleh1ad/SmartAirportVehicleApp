import tkinter as tk
from tkinter import ttk

def open_settings_screen(root):
    settings_win = tk.Toplevel(root)
    settings_win.title("System Settings")
    tk.Label(settings_win, text="Settings Screen").pack(padx=20, pady=20)