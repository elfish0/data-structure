
# 1.对list中的重复元素进行重命名，统计，删除

def rename_duplicate(list,print_result=False):
    renamed_duplicate = [v+str(list[:i].count(v)+1) if list.count(v)>1 else v for i,v in enumerate(list)]
    if print_result:
        print("renamed_duplicate: ", renamed_duplicate)
    return renamed_duplicate

def clean_duplicate(list,print_result=False):
    duplicate_list = []
    no_duplicate_list = []
    duplicate_dict = {}
    for ele in list:
        duplicate_list.append(ele)
        if ele not in no_duplicate_list:
            no_duplicate_list.append(ele)
        else:
            ind = len(duplicate_list)-1
            duplicate_dict[ele] = duplicate_dict.get(ele, [list.index(ele)])
            duplicate_dict[ele].append(ind)
    if print_result:
        print("origin_list: ", duplicate_list, "\nnew_list: ", no_duplicate_list, "\nduplicate_dict: ", duplicate_dict)
    return duplicate_list, no_duplicate_list, duplicate_dict

origin_list = ['blue','red','blue','grey','yellow','yellow','blue','black']
duplicate_list, no_duplicate_list, duplicate_dict = clean_duplicate(origin_list,True)
renamed_duplicate = rename_duplicate(origin_list,True)


"""
# 2.重复元素在set中自动被过滤:
no_duplicate_list2 =list(set(origin_list))
print("new_list2: ",no_duplicate_list2)

# 3.统计重复元素.
li = ['blue','red','blue','grey','yellow','yellow','blue','black']
dup = set()
for i in li:
     if li.count(i)>1:
         dup.add(i)
print("dup: ",dup)

# 4.统计重复元素.
dup2 = set([e for e in li if li.count(e)>1])
print("dup2: ",dup2)
"""
