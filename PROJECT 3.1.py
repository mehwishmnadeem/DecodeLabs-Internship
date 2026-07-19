import tkinter as tk
from tkinter import ttk, messagebox
# Movie Database
movies = [
    {"title": "John Wick", "genre": "Action", "language": "English", "rating": 8.2},
    {"title": "The Dark Knight", "genre": "Action", "language": "English", "rating": 9.0},
    {"title": "Mad Max: Fury Road", "genre": "Action", "language": "English", "rating": 8.1},

    {"title": "Interstellar", "genre": "Science Fiction", "language": "English", "rating": 8.7},
    {"title": "The Matrix", "genre": "Science Fiction", "language": "English", "rating": 8.6},
    {"title": "Avatar", "genre": "Science Fiction", "language": "English", "rating": 7.9},

    {"title": "Titanic", "genre": "Romance", "language": "English", "rating": 7.9},
    {"title": "La La Land", "genre": "Romance", "language": "English", "rating": 8.0},
    {"title": "The Notebook", "genre": "Romance", "language": "English", "rating": 7.8},

    {"title": "The Conjuring", "genre": "Horror", "language": "English", "rating": 7.5},
    {"title": "IT", "genre": "Horror", "language": "English", "rating": 7.3},
    {"title": "Insidious", "genre": "Horror", "language": "English", "rating": 6.8},
]
# Recommendation Function
def recommend():

    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    genre = genre_box.get()
    language = language_box.get()
    min_rating = float(rating_box.get())

    result_box.delete(1.0, tk.END)

    recommendations = []

    for movie in movies:

        score = 0

        if movie["genre"] == genre:
            score += 5

        if movie["language"] == language:
            score += 3

        if movie["rating"] >= min_rating:
            score += 2

        if score > 0:
            recommendations.append((score, movie))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    result_box.insert(
        tk.END,
        f"Hello {name}!\n\nHere are your recommended movies:\n\n"
    )

    if len(recommendations) == 0:
        result_box.insert(tk.END, "No recommendations found.")
        return

    count = 1

    for score, movie in recommendations[:5]:
        result_box.insert(
            tk.END,
            f"{count}. {movie['title']}\n"
            f"   Genre : {movie['genre']}\n"
            f"   Language : {movie['language']}\n"
            f"   IMDb Rating : {movie['rating']}\n"
            f"   Match Score : {score}/10\n\n"
        )
        count += 1
# Reset Function
def reset():

    name_entry.delete(0, tk.END)
    genre_box.current(0)
    language_box.current(0)
    rating_box.current(0)
    result_box.delete(1.0, tk.END)
# GUI
root = tk.Tk()

root.title("Smart Movie Recommendation System")
root.geometry("700x650")
root.configure(bg="#DDEEFF")

title = tk.Label(
    root,
    text="SMART MOVIE RECOMMENDATION SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#DDEEFF",
    fg="darkblue"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#DDEEFF")
frame.pack()

tk.Label(frame, text="Your Name", bg="#DDEEFF",
         font=("Arial", 11, "bold")).grid(row=0, column=0, pady=10, sticky="w")

name_entry = tk.Entry(frame, width=30, font=("Arial", 11))
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Favorite Genre", bg="#DDEEFF",
         font=("Arial", 11, "bold")).grid(row=1, column=0, pady=10, sticky="w")

genre_box = ttk.Combobox(
    frame,
    values=["Action", "Science Fiction", "Romance", "Horror"],
    state="readonly",
    width=27
)
genre_box.current(0)
genre_box.grid(row=1, column=1)

tk.Label(frame, text="Language", bg="#DDEEFF",
         font=("Arial", 11, "bold")).grid(row=2, column=0, pady=10, sticky="w")

language_box = ttk.Combobox(
    frame,
    values=["English"],
    state="readonly",
    width=27
)
language_box.current(0)
language_box.grid(row=2, column=1)

tk.Label(frame, text="Minimum IMDb Rating", bg="#DDEEFF",
         font=("Arial", 11, "bold")).grid(row=3, column=0, pady=10, sticky="w")

rating_box = ttk.Combobox(
    frame,
    values=["6.5", "7.0", "7.5", "8.0", "8.5"],
    state="readonly",
    width=27
)
rating_box.current(0)
rating_box.grid(row=3, column=1)

button_frame = tk.Frame(root, bg="#DDEEFF")
button_frame.pack(pady=20)

recommend_btn = tk.Button(
    button_frame,
    text="Get Recommendations",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=recommend
)
recommend_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(
    button_frame,
    text="Reset",
    font=("Arial", 11, "bold"),
    bg="orange",
    width=12,
    command=reset
)
reset_btn.grid(row=0, column=1)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=12,
    command=root.destroy
)
exit_btn.grid(row=0, column=2)

tk.Label(
    root,
    text="Recommended Movies",
    font=("Arial", 13, "bold"),
    bg="#DDEEFF"
).pack()

scroll = tk.Scrollbar(root)

result_box = tk.Text(
    root,
    height=18,
    width=75,
    yscrollcommand=scroll.set,
    font=("Arial", 10)
)

scroll.config(command=result_box.yview)

scroll.pack(side=tk.RIGHT, fill=tk.Y)

result_box.pack(pady=10)

root.mainloop()
