servers = [
    {'hostname': 'srv-web-01', 'ip': '192.168.1.10', 'status': 'active', 'load': 45},
    {'hostname': 'srv-db-01', 'ip': '192.168.1.11', 'status': 'down', 'load': 0},
    {'hostname': 'srv-app-01', 'ip': '192.168.1.12', 'status': 'active', 'load': 88},
    {'hostname': 'srv-cache-01', 'ip': '192.168.1.13', 'status': 'down', 'load': 0},
    {'hostname': 'srv-auth-01', 'ip': '192.168.1.14', 'status': 'active', 'load': 92}
]

def monitoring_server(data_list, list_target):
    server_list = []

    for m in data_list:
        if m['status'] == list_target:
            server_list.append(m)

    return server_list

def overload_monitoring(data_list, min_load):
    overload = []

    for m in data_list:
        if m['load'] > min_load:
            overload.append(m)
    return overload

list_active = monitoring_server(servers, 'active')
list_down = monitoring_server(servers, 'down')
list_overload = overload_monitoring(servers, 80)

print(list_active)
print(list_down)
print(list_overload)