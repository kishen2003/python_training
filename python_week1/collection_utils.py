#list
def list_create(elements):
    return list(elements)

def list_read(lst, index):
    if -len(lst) <= index < len(lst):
        return lst[index]
    else:
        return None

def list_update(lst, index, value):
    if -len(lst) <= index < len(lst):
        lst[index]=value
        return lst
    else:
        return "List index out of range"

def list_delete(lst, index):
    if -len(lst) <= index < len(lst):
        lst.pop(index)
        return lst
    else:
        return "List index out of range"

def list_insert(lst, index, value):
    if -len(lst) <= index <= len(lst):
        lst.insert(index, value)
    else:
        return "List index out of range"
    

#tuple
def tuple_create(elements):
    return tuple(elements)

def tuple_read(tpl, index):
    if -len(tpl)<= index <len(tpl):
        return tpl[index]
    else:
        return None

def tuple_update(tpl, index, value):
    if -len(tpl)<= index <len(tpl):
        lst = list(tpl)
        lst[index]=value
        return tuple(lst)
    else:
        return "Tuple index out of range"

def tuple_delete(tpl, index):
    if -len(tpl)<= index <len(tpl):
        lst = list(tpl)
        lst.pop(index)
        return tuple(lst)
    else:
        return "Tuple index out of range"
    
def tuple_insert(tpl, index, value):
    if -len(tpl) <= index <= len(tpl):
        lst = list(tpl)
        lst.insert(index, value)
        return tuple(lst)
    else:
        return "Tuple index out of range"


#set
def set_create(elements):
    return set(elements)

def set_read(st, value):
    return value in st

def set_update(st, old_value, new_value):
    if old_value in st:
        st.discard(old_value)
        st.add(new_value)
        return st
    else:
        return "Value not present in set"

def set_delete(st, value):
    st.discard(value)
    return st

def set_insert(st, value):
    st.add(value)
    return st


#dict
def dict_create(pairs):
    return dict(pairs)

def dict_read(dct, key):
    if key in dct:
        return dct[key]
    else:
        return None

def dict_update(dct, key, value):
    if key in dct:
        dct[key]=value
        return dct
    else:
        return "Key doesn't exist"

def dict_delete(dct, key):
    if key in dct:
        dct.pop(key)
        return dct
    else:
        return "Key doesn't exist"
    
def dict_insert(dct, key, value):
    dct[key]=value
    return dct


if __name__ == "__main__":
    print("=== LIST CRUD ===")
    lst = list_create([1, 2, 3])
    print(list_insert(lst, 2, 30))
    print(list_read(lst, 1))
    print(list_update(lst, 1, 20))
    print(list_delete(lst, 0))

    print("\n=== TUPLE CRUD ===")
    tpl = tuple_create([1, 2, 3])
    print(tuple_insert(tpl, 2, 30))
    print(tuple_read(tpl, 2))
    print(tuple_update(tpl, 1, 50))
    print(tuple_delete(tpl, 0))

    print("\n=== SET CRUD ===")
    st = set_create([1, 2, 3])
    print(set_insert(st, 30))
    print(set_read(st, 2))
    print(set_update(st, 2, 20))
    print(set_delete(st, 1))

    print("\n=== DICT CRUD ===")
    dct = dict_create([("a", 1), ("b", 2)])
    print(dict_insert(dct, "d", "4"))
    print(dict_read(dct, "a"))
    print(dict_update(dct, "c", 3))
    print(dict_delete(dct, "b"))

