def isfizz(n):
    return n % 3 == 0

def isbuzz(n):
    return n % 5 == 0

def outfizz():
    print("fizz", end="")

def outbuzz():
    print("buzz", end="")

def endnum(n):
    if isfizz(n) or isbuzz(n):
        n = ""
    print(n)

def fizzbuzz(numbers):
    for n in numbers:
        if isfizz(n):
            outfizz()
        if isbuzz(n):
            outbuzz()
        endnum(n)

def main():
    fizzbuzz(range(100))
    