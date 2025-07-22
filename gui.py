import tkinter as tk
from tkinter import ttk, messagebox
from data_exporter import export_to_excel
from db_connector import test_connection
import threading

def run_app():
    app = tk.Tk()
    app.title("Database to Excel Exporter")
    app.geometry("600x500")

    db_type = tk.StringVar(value="PostgreSQL")

    # === Title ===
    ttk.Label(app, text="Database to Excel Exporter", font=("Arial", 16, "bold")).pack(pady=10)

    # === DB Type Radio Buttons ===
    # frame_db = ttk.LabelFrame(app, text="")
    # frame_db.pack(pady=10, fill="x", padx=10)
    # ttk.Radiobutton(frame_db, text="PostgreSQL", variable=db_type, value="PostgreSQL").pack(side="left", padx=10)
    # ttk.Radiobutton(frame_db, text="MySQL", variable=db_type, value="MySQL").pack(side="left", padx=10)

    # === Connection Fields ===
    conn_entries = {}
    frame_conn = ttk.LabelFrame(app, text="Connection Details")
    frame_conn.pack(pady=10, fill="x", padx=10)

    for label in ["Host", "Port", "Database", "Username", "Password"]:
        row = ttk.Frame(frame_conn)
        row.pack(fill="x", pady=2)
        ttk.Label(row, text=label, width=12).pack(side="left")
        ent = ttk.Entry(row, show="*" if label == "Password" else "")
        ent.pack(side="left", fill="x", expand=True)
        conn_entries[label.lower()] = ent

    # === Filters ===
    frame_filter = ttk.LabelFrame(app, text="Advanced Filters")
    frame_filter.pack(pady=10, fill="x", padx=10)

    row_limit = tk.IntVar(value=1000)
    # table_limit = tk.IntVar(value=0)
    # show_tables = tk.BooleanVar(value=False)

    ttk.Label(frame_filter, text="Rows per Table:").pack(anchor="w", padx=10)
    ttk.Entry(frame_filter, textvariable=row_limit).pack(fill="x", padx=10)

    # ttk.Label(frame_filter, text="Number of Tables (0 for all):").pack(anchor="w", padx=10, pady=(10, 0))
    # ttk.Entry(frame_filter, textvariable=table_limit).pack(fill="x", padx=10)

    # ttk.Checkbutton(frame_filter, text="Show Table List", variable=show_tables).pack(anchor="w", padx=10, pady=5)

    # === Loading Popup ===
    def show_loading_popup():
        loading = tk.Toplevel(app)
        loading.title("Processing...")
        loading.geometry("300x140")
        loading.resizable(False, False)
        loading.configure(bg="#f4f4f4")
        loading.grab_set()  # Modal behavior

        tk.Label(loading, text="Please wait while exporting...", font=("Segoe UI", 12, "bold"), bg="#f4f4f4").pack(pady=(20, 10))

        progress = ttk.Progressbar(loading, mode="indeterminate", length=200)
        progress.pack(pady=5)
        progress.start(10)  # 10ms interval (adjust for speed)

        tk.Label(loading, text="🧠 Crunching data for you...", font=("Segoe UI", 10), fg="#666", bg="#f4f4f4").pack(pady=(10, 5))

        return loading


    # === Export Function (with threading) ===
    def on_export():
        config = {
            "db_type": db_type.get(),
            "host": conn_entries["host"].get(),
            "port": conn_entries["port"].get(),
            "database": conn_entries["database"].get(),
            "user": conn_entries["username"].get(),
            "password": conn_entries["password"].get(),
            "row_limit": row_limit.get(),
            # "table_limit": table_limit.get(),
            # "show_tables": show_tables.get()
        }

        loading_win = show_loading_popup()

        def export_task():
            success, message = export_to_excel(config)
            loading_win.destroy()  # Close the loading popup

            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)

        threading.Thread(target=export_task).start()

    # === Test Connection ===
    def on_test():
        config = {
            "db_type": db_type.get(),
            "host": conn_entries["host"].get(),
            "port": conn_entries["port"].get(),
            "database": conn_entries["database"].get(),
            "user": conn_entries["username"].get(),
            "password": conn_entries["password"].get(),
        }
        success, msg = test_connection(config)
        if success:
            messagebox.showinfo("Connection Success", msg)
        else:
            messagebox.showerror("Connection Failed", msg)

    # === Buttons ===
    btn_frame = ttk.Frame(app)
    btn_frame.pack(pady=20)
    ttk.Button(btn_frame, text="Test Connection", command=on_test).pack(side="left", padx=10)
    ttk.Button(btn_frame, text="Export to Excel", command=on_export).pack(side="left", padx=10)

    app.mainloop()

# Run the app
if __name__ == "__main__":
    run_app()
