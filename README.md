# 🗂️ DBExporter

**DBExporter** is a user-friendly GUI-based tool that allows anyone — even non-technical users — to export tables from **PostgreSQL** or **MySQL** databases into a well-formatted **Excel file**. With built-in filtering options and data sanitization, it ensures a smooth, clean export every time.

---

## ✨ Features

- ✅ **Graphical User Interface (GUI)** built with Tkinter
- ✅ **Supports PostgreSQL and MySQL**
- ✅ **Input fields** for host, port, user, password, and database
- ✅ **Radio buttons** to choose database type
- ✅ **Advanced export filters**:
  - Limit number of **rows per table**
  - Choose number of **tables to export**
  - Option to only **list available table names**
- ✅ **Well-formatted Excel** output:
  - Bold headers
  - Table separation with spacing
  - Sanitized sheet names and data to avoid Excel errors

---

## 📁 Project Structure

```bash
DBTableExporter/
│
├── main.py # Entry point to launch the app
├── gui.py # GUI logic (Tkinter forms)
├── db_exporter.py # Core logic to export tables
├── utils.py # Helper functions (e.g., sanitization)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DBTableExporter.git
cd DBTableExporter
```
2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate  # macOS/Linux
```
3. Install Dependencies
```bash

pip install -r requirements.txt
```
4. Run the App
```bash
python main.py
```
📤 Output Example
```bash
Once export completes, the Excel file will be saved in your current folder like:

Export_PostgreSQL_2025-07-21_14-30-55.xlsx
```
🧩 Requirements
Install all dependencies with:

```bash

pip install -r requirements.txt
```
🪪 License
This project is licensed under the MIT License — free to use and modify.

🙋‍♂️ Author
Made with ❤️ by Raj Bharad & Uttam Gohil
For suggestions or improvements, feel free to create a PR or issue.
