import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Crypto Trade Simulator")
root.geometry("1000x600")
root.configure(bg="#f4f6f8")

inputs = {}
outputs = {}
slippage_data = []

def update_outputs(params):
    for key, value in params.items():
        if key in outputs:
            outputs[key].config(text=f"{key}: {value}")
    update_chart(params.get("Slippage", 0))

def update_chart(new_slip):
    slippage_data.append(new_slip)
    if len(slippage_data) > 50:
        slippage_data.pop(0)
    ax.clear()
    ax.plot(slippage_data, label="Slippage")
    ax.set_title("Real-Time Slippage")
    ax.set_ylabel("Value")
    ax.set_xlabel("Tick")
    ax.legend()
    canvas.draw()

def start_simulation():
    qty = quantity_var.get()
    try:
        float(qty)
    except ValueError:
        messagebox.showerror("Input Error", "Quantity must be a number")
        return
    messagebox.showinfo("Simulation", "Simulation Started!\n(Note: This just triggers the placeholder)")
    # Trigger websocket / simulation logic here

def stop_simulation():
    messagebox.showinfo("Simulation", "Simulation Stopped!")

# ======== UI Components =========

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TFrame", background="#f4f6f8")

ttk.Label(root, text="Real-Time Trade Simulator", style="Header.TLabel", foreground="#007acc").pack(pady=(10, 5))

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

frame_left = ttk.Frame(main_frame)
frame_right = ttk.Frame(main_frame)
frame_left.pack(side="left", fill="y", padx=20)
frame_right.pack(side="right", fill="both", expand=True)

# Input Section
ttk.Label(frame_left, text="INPUT PARAMETERS", style="Header.TLabel", foreground="#005b96").pack(anchor="w", pady=(0, 10))

# Dropdowns
exchange_var = tk.StringVar(value="OKX")
asset_var = tk.StringVar(value="BTC-USDT")
fee_var = tk.StringVar(value="Tier 1")
quantity_var = tk.StringVar(value="100")

dropdowns = [
    ("Exchange", exchange_var, ["OKX"]),
    ("Asset", asset_var, ["BTC-USDT", "ETH-USDT"]),
    ("Fee Tier", fee_var, ["Tier 1", "Tier 2", "Tier 3"]),
]

for label, var, options in dropdowns:
    ttk.Label(frame_left, text=label + ":").pack(anchor="w", pady=(5, 0))
    ttk.Combobox(frame_left, textvariable=var, values=options, state="readonly").pack(anchor="w", fill="x")

# Quantity input
ttk.Label(frame_left, text="Quantity (USD):").pack(anchor="w", pady=(10, 0))
ttk.Entry(frame_left, textvariable=quantity_var).pack(anchor="w", fill="x")

ttk.Button(frame_left, text="Start Simulation", command=start_simulation).pack(pady=(20, 5), fill="x")
ttk.Button(frame_left, text="Stop Simulation", command=stop_simulation).pack(pady=5, fill="x")

# Output Section
ttk.Label(frame_right, text="OUTPUT PARAMETERS", style="Header.TLabel", foreground="#007a4d").pack(anchor="w", pady=(0, 5))
outputs_frame = ttk.Frame(frame_right)
outputs_frame.pack(anchor="nw", fill="x")

for param in ["Slippage", "Market Impact", "Fees", "Net Cost", "Role"]:
    lbl = ttk.Label(outputs_frame, text=f"{param}: --", padding=(5, 2))
    lbl.pack(anchor="w")
    outputs[param] = lbl

# Chart Section
fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_right)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

# Example usage (simulate updating outputs every 2s)
def simulate_dummy_updates():
    import random
    update_outputs({
        "Slippage": round(random.uniform(0.1, 0.9), 3),
        "Market Impact": round(random.uniform(0.5, 2.0), 3),
        "Fees": round(random.uniform(0.01, 0.05), 3),
        "Net Cost": round(random.uniform(0.2, 2.5), 3),
        "Role": "Maker" if random.random() > 0.5 else "Taker"
    })
    root.after(2000, simulate_dummy_updates)

simulate_dummy_updates()
root.mainloop()
