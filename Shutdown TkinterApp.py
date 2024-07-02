import os
import platform
import tkinter as tk
from tkinter import messagebox


def shutdown_system():
    """Shutdown the computer."""
    if platform.system() == 'Windows':
        os.system("shutdown /s /t 3")
    else:
        os.system("shutdown -h +3")


def restart_system():
    """Restart the computer."""
    if platform.system() == 'Windows':
        os.system("shutdown /r /t 3")
    else:
        os.system("shutdown -r +3")


def on_shutdown():
    """Handle shutdown action."""
    if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown your computer?"):
        shutdown_system()


def on_restart():
    """Handle restart action."""
    if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart your computer?"):
        restart_system()


# def on_cancel():
#     """Handle cancel action."""
#     messagebox.showinfo("Action Cancelled", "No action will be performed.")


def create_app():
    """Create the main application window."""
    app = tk.Tk()
    app.title("System Control")

    # Set the window size
    app.geometry("400x300")

    # Set the background color
    app.configure(bg="#282c34")

    # Create a frame for the buttons
    frame = tk.Frame(app, bg="#282c34")
    frame.pack(expand=True)

    # Custom styles
    button_style = {
        "font": ("Helvetica", 14),
        "bg": "#61afef",
        "fg": "white",
        "activebackground": "#3a3f4b",
        "activeforeground": "white",
        "width": 10,
        "height": 1,
        "bd": 0,
        "highlightthickness": 0
    }

    # Create buttons
    shutdown_button = tk.Button(frame, text="Shutdown", command=on_shutdown, **button_style)
    shutdown_button.pack(pady=10)

    restart_button = tk.Button(frame, text="Restart", command=on_restart, **button_style)
    restart_button.pack(pady=10)

    # cancel_button = tk.Button(frame, text="Cancel", command=on_cancel, **button_style)
    # cancel_button.pack(pady=10)

    exit_button = tk.Button(frame, text="Exit", command=app.quit, **button_style)
    exit_button.pack(pady=10)

    # Run the main loop
    app.mainloop()


if __name__ == "__main__":
    create_app()
