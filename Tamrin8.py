import tkinter as tk
from tkinter import messagebox

def calculate_share():
    try:
        total_bill = float(entry_bill.get())
        people = int(entry_people.get())

        if total_bill <= 0 or people <= 0:
            raise ValueError

        share = total_bill / people
        messagebox.showinfo(
            "Natije",
            f"Sahm har nafar: {share:,.0f} toman"
        )

    except ValueError:
        messagebox.showwarning(
            "Khata",
            "Lotfan adad-e motabar vared konid!\n (Mablagh va tedad afrad bayad adad va bozorgtar az adad sefr bashad)"
        )

root = tk.Tk()
root.title("Dong Calculator")
root.geometry("500x150")

tk.Label(root, text="Mablagh kol faktor (toman):").pack(pady=5)
entry_bill = tk.Entry(root)
entry_bill.pack()

tk.Label(root, text="Tedad afrad:").pack(pady=5)
entry_people = tk.Entry(root)
entry_people.pack()

tk.Button(
    root,
    text="Mohasebe sahm har fard",
    command=calculate_share
).pack(pady=15)

root.mainloop()
