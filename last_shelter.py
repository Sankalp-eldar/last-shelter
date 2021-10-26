from datetime import datetime, timedelta
from itertools import combinations

CARDS = {
    "per": [30, 40],
    "exp": [60_000]
}

def per(x, y) -> float:
    return (x*y)/100

def card_exp(x, cards = CARDS) -> float:
    total = 0
    for exp_percent in cards.get("per", []):
        total += per(x, exp_percent)
    for exp in cards.get("exp", []):
        total += exp
    return total

def mission(m1):
    a = m1.get("exp")
    per_a = m1.get("National_percentage")
    unknown_card = m1.get("unknown")
    card = CARDS if m1.get("cards") is None else m1.get("cards")

    ta = a + per(a, per_a) + card_exp(a, card) + card_exp(a, unknown_card)

    return round(ta)/1000

def create_mission(exp, Nper, *per,**kw):
    m = {"exp":exp, "National_percentage": Nper, "unknown": {"per": per }}
    m.update(kw)
    return m

def all_diff(**values):
    diff = dict()
    for i in combinations(values, 2):
        val = round(values[i[0]]-values[i[1]], 2)
        diff[f"{i[0]}-{i[1]}"] = val
    return diff

def total(d:dict, text:str = "k") -> list:
    return [f"Total {i}: {val}{text}" for i,val in d.items()]

def main():
    h5 = create_mission(193_000, 35, 4)
    r4 = create_mission(203_000, 0)
    r5 = create_mission(169_000, 15)
    # x = create_mission(2000, 100, 100, 100, 60, cards={})

    h5 = mission(h5)
    r4 = mission(r4)
    r5 = mission(r5)
    # x = mission(x)

    coll = {
    #"5h": h5,
    "4r": r4,
    "5r": r5
    }
    # coll = {"x": x}
    diff = all_diff(**coll)


    print(*total(coll), sep="\n")
    print()
    print(*total(diff), sep="\n")


if __name__ == "__main__":
    main()

