def fun_1(*args):

    if len(args) == 3:
        print("name", args[0], "age", args[1], "code", args[2])
    else:
        print("name", args[0], "age")

def print_marks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

def master(normal, *args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

list=["harry",22,"hr@31"]
list2={"harry" : 31, "aman" : 54, "jay" : 78, "shiva" : 9}
fun_1(*list)
print_marks(**list2)
master("normal",*list,**list2)