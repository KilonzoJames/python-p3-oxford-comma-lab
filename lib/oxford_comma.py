def oxford_comma(item):
    string=''.join(item)
    if len(item)==2:
        string=' and '.join(item)
    elif len(item) > 2:
        last_item = ', and ' + item[-1]
        string= ', '.join(item[:-1]) + last_item
    else:
        string= ''.join(item)
    return string
items=['1','2','3']
print(oxford_comma(items))