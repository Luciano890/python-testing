import re

def solve_runes(runes: str):
    from string import digits
    for num in digits:
        if num not in runes:
            f = runes.replace("?", num)
            n1, op, n2, res = re.findall(r"(-?\d+)([+*-])(-?\d+)=(-?\d+)", f)[0]
            if (result := eval(f"{int(n1)} {op} {int(n2)}")) == int(res) and len(str(result)) == len(res):
                return int(num)
    return -1
        
# print(solve_runes("-5?*-1=5?"))
# print(solve_runes("?38???+-595???=833444"))
# print("++")
print(solve_runes("?*11=??"))
