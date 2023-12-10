try:
    a = "a"
    a = "4" / 0
    print("Top code")
except ValueError:
    print("Value Error")
except TypeError:
    print("Type Error")


except SyntaxError as e:
    print(f"Syntax Error : {e}")


except Exception as e:
    print(f"Other error happened: {e}")

print("hello")
