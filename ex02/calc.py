import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
        btn = event.widget
        num = btn["text"]#クリックされたボタンの文字
        if num == "=":
            eqn = entry.get()
            res = eval(eqn)
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)
        else:
            #tkm.showinfo("", f"{num}ボタンがクリックされました")
            entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x500") #設定しないと全ウェジェットが表示されるサイズになる
    root.title("電卓")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column=0, columnspan=3)

    r, c = 1, 0 #r:行番号　c:列番号
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "="]):
        btn = tk.Button(root,
                        text=f"{num}",
                        width=4,
                        height=2,
                        font=("Times New Roman", 30)
                        )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)

        c += 1
        if (i+1)%3 == 0:
            r += 1
            c = 0

    root.mainloop()