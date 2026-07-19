import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
df = None
# ------------------------ FUNCTIONS ------------------------

def browse_dataset():
    global df

    filepath = filedialog.askopenfilename(
        title="Select Excel Dataset",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if filepath == "":
        return

    try:
        df = pd.read_excel(filepath)

        file_label.config(text="Selected File:\n" + filepath)

        output.delete(1.0, tk.END)
        output.insert(tk.END, "DATASET LOADED SUCCESSFULLY\n\n")
        output.insert(tk.END, "First 10 Rows\n\n")
        output.insert(tk.END, df.head(10).to_string())

    except Exception as e:
        messagebox.showerror("Error", str(e))


def dataset_info():
    if df is None:
        messagebox.showwarning("Warning", "Please load a dataset first.")
        return

    output.delete(1.0, tk.END)

    output.insert(tk.END, "DATASET INFORMATION\n\n")

    output.insert(tk.END, f"Rows : {df.shape[0]}\n")
    output.insert(tk.END, f"Columns : {df.shape[1]}\n\n")

    output.insert(tk.END, "Column Names\n")
    output.insert(tk.END, "-"*50 + "\n")

    for col in df.columns:
        output.insert(tk.END, col + "\n")

    output.insert(tk.END, "\nData Types\n")
    output.insert(tk.END, "-"*50 + "\n")
    output.insert(tk.END, str(df.dtypes))

    output.insert(tk.END, "\n\nMissing Values\n")
    output.insert(tk.END, "-"*50 + "\n")
    output.insert(tk.END, str(df.isnull().sum()))


def train_model():

    global df

    if df is None:
        messagebox.showwarning("Warning", "Please load a dataset first.")
        return

    try:

        data = df.copy()

        drop_columns = [
            "OrderID",
            "CustomerID",
            "TrackingNumber",
            "ShippingAddress",
            "Date"
        ]

        for col in drop_columns:
            if col in data.columns:
                data.drop(col, axis=1, inplace=True)

        encoder = LabelEncoder()

        for col in data.columns:
            if data[col].dtype == object:
                data[col] = encoder.fit_transform(data[col].astype(str))

        target = "OrderStatus"

        if target not in data.columns:
            messagebox.showerror(
                "Error",
                "Column 'OrderStatus' not found.\nPlease update the target column name."
            )
            return

        X = data.drop(target, axis=1)
        y = data[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model = DecisionTreeClassifier(random_state=42)

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(y_test, prediction)

        report = classification_report(y_test, prediction)

        output.delete(1.0, tk.END)

        output.insert(tk.END, "MODEL TRAINED SUCCESSFULLY\n\n")

        output.insert(tk.END,
                      f"Training Samples : {len(X_train)}\n")

        output.insert(tk.END,
                      f"Testing Samples : {len(X_test)}\n\n")

        output.insert(
            tk.END,
            f"Accuracy : {accuracy*100:.2f}%\n\n"
        )

        output.insert(tk.END,
                      "Classification Report\n")

        output.insert(tk.END,
                      "-"*70 + "\n")

        output.insert(tk.END, report)

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Basic Classification Model")
root.geometry("950x700")
root.configure(bg="#EAF2F8")

title = tk.Label(
    root,
    text="Basic Classification Model",
    font=("Arial", 20, "bold"),
    bg="#1F618D",
    fg="white",
    pady=10
)

title.pack(fill="x")

button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=15)

browse_btn = tk.Button(
    button_frame,
    text="Browse Dataset",
    width=18,
    bg="#3498DB",
    fg="white",
    font=("Arial", 11),
    command=browse_dataset
)

browse_btn.grid(row=0, column=0, padx=10)

info_btn = tk.Button(
    button_frame,
    text="Dataset Info",
    width=18,
    bg="#27AE60",
    fg="white",
    font=("Arial", 11),
    command=dataset_info
)

info_btn.grid(row=0, column=1, padx=10)

train_btn = tk.Button(
    button_frame,
    text="Train Model",
    width=18,
    bg="#AF7AC5",
    fg="white",
    font=("Arial", 11),
    command=train_model
)

train_btn.grid(row=0, column=2, padx=10)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    width=18,
    bg="#E74C3C",
    fg="white",
    font=("Arial", 11),
    command=root.destroy
)

exit_btn.grid(row=0, column=3, padx=10)

file_label = tk.Label(
    root,
    text="No Dataset Selected",
    bg="#EAF2F8",
    fg="black",
    font=("Arial", 10)
)

file_label.pack()

output = scrolledtext.ScrolledText(
    root,
    width=110,
    height=28,
    font=("Consolas", 10)
)

output.pack(pady=15)

root.mainloop()
