import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import time
import threading

def run_macro():
    # 1. Grab inputs from GUI
    ids_raw = text_ids.get("1.0", tk.END).strip()
    amount = entry_amount.get().strip()

    if not ids_raw:
        messagebox.showerror("Error", "Please paste at least one Discord ID.")
        return

    if not amount:
        messagebox.showerror("Error", "Please enter an amount.")
        return

    discord_ids = [i.strip() for i in ids_raw.splitlines() if i.strip()]

    # 2. Countdown alert
    messagebox.showinfo("Ready!", "After clicking OK, you have 5 SECONDS to click inside your Discord text box!")
    time.sleep(5)

    btn_start.config(state=tk.DISABLED)

    # 3. Macro Loop
    for discord_id in discord_ids:
        # Type /add
        pyautogui.write('/add', interval=0.05)
        time.sleep(0.8) 

        # Press TAB to select the /add command
        pyautogui.press('tab')
        time.sleep(0.4)

        # Type the point amount
        pyautogui.write(amount, interval=0.05)
        time.sleep(0.3)

        # Press TAB 3 times to get to the 'mention' input
        pyautogui.press('tab')
        time.sleep(0.15)
        pyautogui.press('tab')
        time.sleep(0.15)
        pyautogui.press('tab')
        
        # Wait for the 'mention' box to spawn
        time.sleep(0.6) 

        # Type <@Discord_ID>
        pyautogui.write(f'<@{discord_id}>', interval=0.03)
        time.sleep(0.4)

        # Press Right Arrow to step out of the tag box
        pyautogui.press('right')
        time.sleep(0.3)

        # Press Enter to send the command
        pyautogui.press('enter')

        # Pause between commands
        time.sleep(1.5)

    btn_start.config(state=tk.NORMAL)
    messagebox.showinfo("Done", f"Successfully processed {len(discord_ids)} IDs!")

def start_macro_thread():
    threading.Thread(target=run_macro, daemon=True).start()

# --- GUI Setup ---
root = tk.Tk()
root.title("Discord Points Macro")
root.geometry("400x480")
root.resizable(False, False)

lbl_info = ttk.Label(root, text="Discord Points Auto-Typer", font=("Arial", 14, "bold"))
lbl_info.pack(pady=10)

lbl_amount = ttk.Label(root, text="Point Amount:")
lbl_amount.pack(anchor="w", padx=20)
entry_amount = ttk.Entry(root, width=15)
entry_amount.insert(0, "100")
entry_amount.pack(anchor="w", padx=20, pady=(0, 10))

lbl_ids = ttk.Label(root, text="Paste Discord IDs (One per line):")
lbl_ids.pack(anchor="w", padx=20)
text_ids = tk.Text(root, height=12, width=42)
text_ids.pack(padx=20, pady=(0, 15))

lbl_emergency = ttk.Label(
    root, 
    text="Emergency Stop: Move mouse to top-left corner of screen", 
    font=("Arial", 8), 
    foreground="red"
)
lbl_emergency.pack(pady=(0, 5))

btn_start = ttk.Button(root, text="Start Macro", command=start_macro_thread)
btn_start.pack(ipady=5, ipadx=10)

root.mainloop()