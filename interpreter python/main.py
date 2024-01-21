import interpreter 

env = {}

while True:
    try:
        text = input('OmenScript > ')
    except EOFError:
        break

    if text:
        result, error = interpreter.run(text)  
        if error:
            print(error)
        elif result:
            print(result)
