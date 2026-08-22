from loop_basic import users

def filter_by_role(data_list, list_target):
    hasil_filter =[]

    for u in data_list:
        if u['role'] == list_target:
            hasil_filter.append(u)

    return hasil_filter

para_admin = filter_by_role(users, 'admin')
para_user = filter_by_role(users, 'user')

print(para_admin)
print(para_user)