# nested Loop = the  " inner loop " will finish all of its iteration before finishin one iteration of the "outer loop";

rows = int(input("how many rows ? "))

columns = int(input("How many columns ? "))

symbols = input("Enter a symbol to use")

for i in range(rows):
    for j in range(columns):
        print(symbols,end="")
    print()
