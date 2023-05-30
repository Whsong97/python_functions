def hello():
    print("Hello, user!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch_list[0])
        for item in lunch_list[1:]:
            print("Next I eat", item)
