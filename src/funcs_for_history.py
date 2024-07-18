import os
from datetime import datetime

def get_qr_files():
    directory = os.getcwd() + f"\qr_png\\"
    list_files = os.listdir(directory)
    list_time = []
    files = []
    for i in range(len(list_files)):
        mtime = os.path.getmtime(directory + list_files[i])
        files.append({"file": list_files[i], "date": datetime.fromtimestamp(mtime).strftime('%d.%m.%y %H:%M:%S')})
    return files

def get_dict_add_and_del(list_old, list_new):
    set_a = set()
    set_b = set()
    for _d in list_old:
        set_a.add(_d["file"])
    for _d in list_new:
        set_b.add(_d["file"])

    add = set_b - set_a
    delete = set_a - set_b
    # print(set_a)
    # print(set_b)
    # print(add)
    # print(delete)


    list_add = []
    list_delete = []

    for name in add:
        for i in range(len(list_new)):
            if name == list_new[i]["file"]:
                list_add.append(list_new[i])

    for name in delete:
        for i in range(len(list_old)):
            if name == list_old[i]["file"]:
                list_delete.append(list_old[i])
    
    return {"add" : list_add, "delete" : list_delete}

def delete_file(name_file):
    path = os.getcwd() + f"\qr_png\\{name_file}"
    os.remove(path)


    # diff = set_a.symmetric_difference(set_b)
    # add_set = diff.intersection(set_b)
    # delete_set = diff.intersection(set_a)

    # for add in add_set



# sett = get_qr_files()
# print(sett)

# for i in sett:
#     print(dict(i))
