import tkinter as t, random as r

c = ["Rock","Paper","Scissors"]
u, pc, res = t.StringVar(), t.StringVar(), t.StringVar()

def play(x):
    u.set(x); y=r.choice(c); pc.set(y)
    res.set("Tie" if x==y else "You Win" if (x,y) in
            [("Rock","Scissors"),("Paper","Rock"),("Scissors","Paper")] else "Computer Wins")

def reset(): u.set(""); pc.set(""); res.set("")

w=t.Tk(); w.title("RPS")

for i,x in enumerate(c):
    t.Button(w,text=x,command=lambda x=x:play(x)).grid(row=0,column=i)

t.Label(w,text="You").grid(row=1,column=0)
t.Label(w,textvariable=u).grid(row=1,column=1)
t.Label(w,text="Computer").grid(row=2,column=0)
t.Label(w,textvariable=pc).grid(row=2,column=1)
t.Label(w,textvariable=res).grid(row=3,column=1)
t.Button(w,text="Reset",command=reset).grid(row=4,column=1)

w.mainloop()
