
import tkinter as tk
from tkinter import messagebox
from collections import Counter


# تابع تحلیل رشته
def analyze_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("توجه", "لطفاً یک متن وارد کنید.")
        return

    # جدا کردن کلمات
    words = text.split()

    # شمارش تعداد کلمات
    word_count = len(words)

    # شمارش تعداد کاراکترها
    char_count = len(text)

    # شمارش تکرار کاراکترها
    char_frequency = Counter(text)

    # حذف فاصله برای پیدا کردن پرتکرارترین کاراکتر
    characters = Counter(
        char for char in text if not char.isspace()
    )

    if characters:
        max_frequency = max(characters.values())
        most_common = [
            char for char, count in characters.items()
            if count == max_frequency
        ]

        common_result = "، ".join(
            f"«{char}» ({max_frequency} بار)"
            for char in most_common
        )
    else:
        common_result = "کاراکتری وجود ندارد."

    # شمارش تکرار هر کلمه
    word_frequency = Counter(words)

    # نمایش نتایج
    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, "📊 نتایج تحلیل متن\n")
    result_text.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━\n\n")

    result_text.insert(
        tk.END,
        f"تعداد کلمات: {word_count}\n\n"
    )

    result_text.insert(
        tk.END,
        f"تعداد کاراکترها: {char_count}\n\n"
    )

    result_text.insert(
        tk.END,
        f"پرتکرارترین کاراکتر: {common_result}\n\n"
    )

    result_text.insert(tk.END, "تعداد تکرار هر کلمه:\n")

    for word, count in word_frequency.items():
        result_text.insert(
            tk.END,
            f"  • {word} : {count} بار\n"
        )


# تابع پاک کردن
def clear_all():
    input_text.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)


# ساخت پنجره اصلی
root = tk.Tk()
root.title("برنامه تحلیل رشته")
root.geometry("700x680")
root.configure(bg="#151526")
root.resizable(False, False)


# عنوان برنامه
title = tk.Label(
    root,
    text="تحلیلگر هوشمند متن",
    font=("Tahoma", 23, "bold"),
    bg="#151526",
    fg="#A78BFA"
)
title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="بررسی و تحلیل ویژگی های یک رشته",
    font=("Tahoma", 11),
    bg="#151526",
    fg="#B8B8CC"
)
subtitle.pack(pady=5)


# عنوان ورودی
input_label = tk.Label(
    root,
    text="متن خود را وارد کنید:",
    font=("Tahoma", 12, "bold"),
    bg="#151526",
    fg="white"
)
input_label.pack(fill="x", padx=55, pady=(25, 8))


# کادر ورود متن
input_text = tk.Text(
    root,
    width=65,
    height=6,
    font=("Tahoma", 12),
    bg="#25253B",
    fg="white",
    insertbackground="white",
    relief="flat",
    wrap="word"
)
input_text.pack(padx=50, pady=5)


# دکمه ها
button_frame = tk.Frame(root, bg="#151526")
button_frame.pack(pady=25)


def create_button(text, command, color):
    return tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Tahoma", 11, "bold"),
        bg=color,
        fg="white",
        activebackground="#9479F0",
        activeforeground="white",
        relief="flat",
        width=15,
        cursor="hand2",
        pady=10
    )


analyze_btn = create_button(
    "تحلیل متن",
    analyze_text,
    "#7657D5"
)
analyze_btn.pack(side="right", padx=10)


clear_btn = create_button(
    "پاک کردن",
    clear_all,
    "#A34F68"
)
clear_btn.pack(side="right", padx=10)


# عنوان نتایج
result_label = tk.Label(
    root,
    text="نتایج تحلیل:",
    font=("Tahoma", 12, "bold"),
    bg="#151526",
    fg="white"
)
result_label.pack(fill="x", padx=55, pady=(5, 8))


# کادر نمایش نتایج
result_text = tk.Text(
    root,
    width=65,
    height=14,
    font=("Tahoma", 11),
    bg="#25253B",
    fg="#A78BFA",
    insertbackground="white",
    relief="flat",
    wrap="word"
)
result_text.pack(padx=50, pady=5)


# متن پایین صفحه
footer = tk.Label(
    root,
    text="پروژه تحلیل رشته | Python",
    font=("Tahoma", 9),
    bg="#151526",
    fg="#77778F"
)
footer.pack(pady=15)


# اجرای برنامه
root.mainloop()
