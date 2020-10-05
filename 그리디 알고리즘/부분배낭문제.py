data_list = [[10,10],[20,10],[30,5],[15,12],[25,8]]

def get_max_value(data_list, capacity):
    data_list.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity-data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0],data[1],1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value,details

print (get_max_value(data_list,30))