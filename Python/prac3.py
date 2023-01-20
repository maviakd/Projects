def auth(x):
    x = x[2:len(x)-1]

    if x.lower() == 'success':
        print(f"success x is {x}")
    else:
        print(f"Failure x is {x}")

b = b'success'
auth(str(b))