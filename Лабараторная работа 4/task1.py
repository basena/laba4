import json
# TODO решите задачу

INPUT="input.json"
def task() -> float:
    with open(INPUT) as f:
        slovar = json.load(f)
    sum=0
    for s in slovar:
        pr=s["score"]*s["weight"]
        sum=sum+pr
    return round(sum, 3)


print(task())
