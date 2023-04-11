"""
Hi There,

This is a timer application built using the Tkinter library in Python.
The application allows the user to set a timer for a specific amount of time, start, pause, stop, and reset the timer.

The user can input the desired time in minutes and seconds using the entry fields provided.
The timer display label shows the remaining time in minutes and seconds.
The progress bar shows the progress of the timer countdown.

The user can start the timer by clicking the "Start" button,
The timer will start counting down from the specified time,
The user can pause the timer by clicking the "Pause" button,
The user can stop the timer by clicking the "Stop" button,
The user can reset the timer by clicking the "Reset" button.

The application also includes a listbox that displays the timer values that have been set and completed
The completed timer values are displayed in green, and the stopped timer values are displayed in red.

Overall, this application provides a simple and user-friendly interface for setting and managing timers.

All The Best

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TimerTk:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.master.configure(bg="#F5F5F5")

        
        # Create widgets
        timer_frame = tk.Frame(self.master, bg="#F5F5F5")
        timer_frame.pack(pady=20)

        timer_input_frame = tk.Frame(timer_frame, bg="#F5F5F5")
        timer_input_frame.pack()

        # Create minutes label and entry
        self.minutes_label = tk.Label(timer_input_frame, text="Minutes:", font=("Arial", 14), bg="#F5F5F5")
        self.minutes_label.pack(side=tk.LEFT, padx=5)

        self.minutes_entry = tk.Entry(timer_input_frame, width=5, font=("Arial", 14))
        self.minutes_entry.pack(side=tk.LEFT, padx=5)

        # Create seconds label and entry
        self.seconds_label = tk.Label(timer_input_frame, text="Seconds:", font=("Arial", 14), bg="#F5F5F5")
        self.seconds_label.pack(side=tk.LEFT, padx=5)

        self.seconds_entry = tk.Entry(timer_input_frame, width=5, font=("Arial", 14))
        self.seconds_entry.pack(side=tk.LEFT, padx=5)

        timer_control_frame = tk.Frame(timer_frame, bg="#F5F5F5")
        timer_control_frame.pack(pady=10)

        # Create start button
        self.start_button = tk.Button(timer_control_frame, text="Start", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.startTimer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Create stop button
        self.stop_button = tk.Button(timer_control_frame, text="Stop", font=("Arial", 14), bg="#F44336", fg="white", command=self.stopTimer)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Create reset button
        self.reset_button = tk.Button(timer_control_frame, text="Reset", font=("Arial", 14), bg="#2196F3", fg="white", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Create pause button
        self.pause_button = tk.Button(timer_control_frame, text="Pause", font=("Arial", 14), bg="#FFC107", fg="white", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        # Create timer display label
        self.timer_label = tk.Label(self.master, text="00:00", font=("Arial", 48), bg="#F5F5F5")
        self.timer_label.pack(pady=10)

        # Create timer listbox
        self.timer_listbox = tk.Listbox(self.master, font=("Arial", 14), bg="#F5F5F5")
        self.timer_listbox.pack(pady=10)

        # Create progress bar
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        # Initialize timer variables
        self.is_running = False
        self.remaining_time = 0

        

    def startTimer(self):
       # Check if timer is already running
        if not self.is_running:

            # Get minutes and seconds from entries
            minutes = int(self.minutes_entry.get() or 0)
            seconds = int(self.seconds_entry.get() or 0)
            
            self.remaining_time = minutes * 60 + seconds # Calculate total remaining time in seconds
            self.is_running = True # Set timer to running state
            self.timer_listbox.insert(tk.END, f"{minutes:02d}:{seconds:02d}") # Add timer value to listbox
            
            self.runTimer() # Start timer countdown



    def runTimer(self):
        # Check if timer is running and there is remaining time
        if self.is_running and self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60) # Convert remaining time to minutes and seconds

            # Format timer display label
            timer = f"{mins:02d}:{secs:02d}"
            self.timer_label.configure(text=timer)

            self.remaining_time -= 1 # Decrement remaining time by 1 second

            # Update progress bar
            self.progress_bar["maximum"] = self.remaining_time
            self.progress_bar["value"] = self.remaining_time

            self.master.after(1000, self.runTimer) # Schedule next timer update after 1 second
    
        elif self.is_running and self.remaining_time == 0:
            self.timer_label.configure(text="End") # Set timer display label to "End"
            self.is_running = False # Set timer to not running state
            self.timer_listbox.itemconfig(tk.END, fg="green")  # change color of completed timer
            self.progress_bar["value"] = 0 # Reset progress bar



    def stopTimer(self):
        self.is_running = False # Set timer to not running state
        self.remaining_time = 0 # Reset remaining time to 0
        self.timer_label.configure(text="00:00") # Set timer display label to "00:00"
        self.timer_listbox.itemconfig(tk.ACTIVE, fg="red")  # Change color of stopped timer in listbox
        self.progress_bar["value"] = 0 # Reset progress bar
    
    def pause(self):
        # Toggle timer running state
        if self.is_running:
            self.is_running = False
        else:
            self.is_running = True
            self.runTimer()

    def reset(self):
        # Ask user for confirmation before resetting timer
        if tk.messagebox.askyesno("Reset Timer", "Are you sure you want to reset the timer?"):
            self.is_running = False # Set timer to not running state
            self.remaining_time = 0 # Reset remaining time to 0
            self.timer_label.configure(text="00:00") # Set timer display label to "00:00"
            self.timer_listbox.delete(0, tk.END) # Clear timer listbox
            self.progress_bar["value"] = 0 # Reset progress bar

# Run Program
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerTk(root)
    root.mainloop()