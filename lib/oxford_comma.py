# Loop through add item with a comma if its the second to last add and

def oxford_comma(items):
    new_list = []

    if len(items) == 1:
        return items[0]
    
    elif len(items) == 2:
        new_str = ' and '.join(items)
        return new_str
    
    else:
        
        for item in items:
            str = item + ','
            new_list.append(str)

            if items.index(item) == len(items) - 2:
                last = items.index(item) + 1
                new_list.append('and ' + items[last])
                return ' '.join(new_list)

    return None            
            
   
       

print(oxford_comma(['kiwi', 'durian']))