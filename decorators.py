def cough_dec(func):
    def func_wrapper():
        # code before function
        print("*Cough*")
        func()
        # code after function
        print("*Cough*")

    return func_wrapper


@cough_dec
def question():
    print("Can you give me a discount on that?")


@cough_dec
def answer():
    print("it's only 50p you cheapskate")


question()

answer()
