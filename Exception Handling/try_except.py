try:

    # FOR ZeroDivisionError BLOCK
    a = 9/0
    print(a)

    # FOR TypeError BLOCK
    a = 'hello'
    b = a + 5
    print(b)
    


except ZeroDivisionError:
    # optional block
    # Handling of exception (if required)
    print("Zero Error")

except TypeError:
    print ("type error")

else:
    print("no error")
    # execute if no exception

finally:
    print(f"\n\n done ")
    # Some code .....(always executed)