def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add
    Works by determining the command and then where the command takes place.
    """
    if command == "add":
        if location == "beginning":
           lst.insert(0, value)
           return lst
        elif location == "end":
            lst.insert(len(lst), value)
            return lst
    elif command == "remove":
        if location == "beginning":
           output = lst.pop(0)
           return output
        elif location == "end":
           output = lst.pop(len(lst) -1)
           return output
    else:
        return None