def exmaple2(required_arg, *arg, **kwarg):
    if arg:
        print("arg: ", arg)

    if kwarg:
        print("kwarg: ", kwarg)

exmaple2("Hi", 4,'j','k',4, keyword1 = "bar", keyword2 = "foo")