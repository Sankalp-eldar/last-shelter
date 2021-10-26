from tkinter import Tk, Frame, Text
from tkinter.ttk import Entry, Button, Label, Style
import last_shelter as ls
import json

root = Tk()
root.title('Last Shelter')

fr = Frame(root)
fr_left = Frame(fr)
fr_mis = Frame(fr_left)
fr_display = Frame(fr_left)

fr.pack(expand=True, fill="both")
res = Text(fr)

res.pack(side="right")
fr_left.pack(expand=True, fill="both",side="left")
fr_mis.pack()
fr_display.pack()


missions = dict()

def add_mission(where = missions):
    name = mission_add[0].get()
    exp = int(mission_add[1].get())
    try:
        nper = int(mission_add[2].get())
    except ValueError:
        nper = 0
    try:
        unknown = [int(i) for i in mission_add[3].get().split(',')]
    except ValueError:
        unknown = []
    cards = mission_add[4].get()
    if cards:
        try:
            cards = json.loads(cards)
            if not isinstance(cards, dict):
                raise ValueError
        except:
            insert("Card error. defaulting to empty dict.")
            cards = {}
    else:
        cards = None

    mission = ls.create_mission(exp, nper, *unknown, cards=cards)
    where[name] = mission


mission_add = list()
mission_details = ["Name", "Exp", "National exp %", "Unknown cards %", "Cards*"]

for i, val in enumerate(mission_details):
    Label(fr_mis, text = val).grid(row=i, column=0, pady=2)
    a = Entry(fr_mis)
    a.grid(row=i, column=1, pady=2)
    mission_add.append(a)
def clean():
    for i in mission_add:
        i.delete("0", "end")
Button(fr_mis, text = "Add mission", command = add_mission).grid(row=i+1, column=0)
Button(fr_mis, text = "Clear", command= clean).grid(row=i+1, column=1)


def clear():
    res.delete("0.0", "end")
def insert(data):
    res.insert("end", data+"\n")
def clear_insert(data):
    clear()
    insert(data)


def Calculate():
    results = dict()
    for i,val in missions.items():
        exp = ls.mission(val)
        results[i] = exp
    totals = ls.total(results)
    insert("\n".join(totals))
    return results

def Display():
    if not missions:
        return
    data = "\n".join([f"{k}:{v}" for k,v in missions.items()])
    insert(data)

def Diff():
    if not missions:
        return
    diff = ls.all_diff(**Calculate())
    data = "\n".join(ls.total(diff))
    insert(data)
    return diff

Button(fr_display, text="Calculate Exp", command=Calculate).grid(row=0, column=0, pady=2, padx=1)
Button(fr_display, text="Display missions", command=Display).grid(row=0, column=1, pady=2, padx=1)
Button(fr_display, text="Clear", command=clear).grid(row=1, column=0, pady=2, padx=1)
Button(fr_display, text="Differences", command=Diff).grid(row=1, column=1, pady=2, padx=1)



root.mainloop()

