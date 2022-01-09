def function_triangle(a,inp):
    total=1
    for i in a:
        if(inp<= i):
            break
        else:
            inp = inp-i
        total=total+1
    print(total)

if __name__ == "__main__":
    balls = int(input("Enter number of balls"))
    a = range(1,(balls*10))
    function_triangle(a,balls)
