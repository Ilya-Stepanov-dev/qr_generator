def get_counter():
    try:
        with open('counter.txt') as file:
            count = int(file.read())
            return count 
    except:
        with open('counter.txt', "a") as file:
            pass
        return 1
    
def save_counter(counter):
    with open('counter.txt', "w") as file:
        file.write(counter)