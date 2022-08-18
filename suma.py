from threading import Thread

def hi(hi="hi"):
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    
def he(hi="he"):
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)
    print(hi)

Thread(target=he).start()
Thread(target=hi).start()