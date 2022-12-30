import ast
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
data_BT = []
data_BJ = []
data_SH = []
data_GZ = []
data_SZ = []
with open("test1/RentHouseBT.json", "r", encoding="utf-8") as json_file:
    content = json_file.read()
for line in content.split("\n"):
    if len(line) != 0:
        data_BT.append(ast.literal_eval(line))
with open("test1/RentHouseBJ.json", "r", encoding="utf-8") as json_file:
    content = json_file.read()
for line in content.split("\n"):
    if len(line) != 0:
        data_BJ.append(ast.literal_eval(line))
with open("test1/RentHouseSH.json", "r", encoding="utf-8") as json_file:
    content = json_file.read()
for line in content.split("\n"):
    if len(line) != 0:
        data_SH.append(ast.literal_eval(line))
with open("test1/RentHouseGZ.json", "r", encoding="utf-8") as json_file:
    content = json_file.read()
for line in content.split("\n"):
    if len(line) != 0:
        data_GZ.append(ast.literal_eval(line))
with open("test1/RentHouseSZ.json", "r", encoding="utf-8") as json_file:
    content = json_file.read()
for line in content.split("\n"):
    if len(line) != 0:
        data_SZ.append(ast.literal_eval(line))


def price(data):
    result = []
    for item in data:
        if 'price' in item:
            result.append(int(item['price']))
    return sorted(result)


def unit_price(data):
    result = []
    for item in data:
        if len(item['area']) <= 0:
            continue
        area = float(item['area'][:len(item['area']) - 1])
        totalPrice = int(item['price'])
        result.append(round(totalPrice / area, 2))
    return sorted(result)


def type_price(data, flag):
    result = []
    for item in data:
        if len(item['type']) <= 0:
            continue
        if item['type'][0].isdigit() and int(item['type'][0]) == flag:
            result.append(int(item['price']))
    return sorted(result)


def location_price(data):
    result = {}
    for item in data:
        if len(item['location_2']) <= 0:
            continue
        if item['location_2'] not in result:
            result[item['location_2']] = []
        result[item['location_2']].append(int(item['price']))
        result[item['location_2']] = sorted(result[item['location_2']])
    return result


def forward_price(data):
    result = {}
    for item in data:
        if len(item['forward']) <= 0 or item['forward'][0] not in ['东', '南', '西', '北'] or len(item['area']) <= 0:
            continue
        for forward in item['forward'].split("/"):
            if forward not in ['东', '南', '西', '北', '东北', '东南', '西北', '西南']:
                continue
            if forward not in result:
                result[forward] = []
            area = float(item['area'][:len(item['area']) - 1])
            totalPrice = int(item['price'])
            result[forward].append(round(totalPrice / area, 2))
            result[forward] = sorted(result[forward])
    return result


def cal_total(totalprice, data, index):
    totalprice[index].append(round(sum(price(data)) / len(price(data)), 2))
    totalprice[index].append(max(price(data)))
    totalprice[index].append(min(price(data)))
    if len(price(data)) % 2 == 0:
        totalprice[index].append(
            (price(data)[len(price(data)) // 2 - 1] + price(data)[len(price(data)) // 2]) / 2)
    else:
        totalprice[index].append(price(data)[len(price(data)) // 2])


def cal_unit(unitprice, data, index):
    unitprice[index].append(round(sum(unit_price(data)) / len(unit_price(data)), 2))
    unitprice[index].append(max(unit_price(data)))
    unitprice[index].append(min(unit_price(data)))
    if len(unit_price(data)) % 2 == 0:
        unitprice[index].append(
            (unit_price(data)[len(unit_price(data)) // 2 - 1] + unit_price(data)[len(unit_price(data)) // 2]) / 2)
    else:
        unitprice[index].append(unit_price(data)[len(unit_price(data)) // 2])


def cal_type(typeprice, data, index, flag):
    typeprice[index].append(round(sum(type_price(data, flag)) / len(type_price(data, flag)), 2))
    typeprice[index].append(max(type_price(data, flag)))
    typeprice[index].append(min(type_price(data, flag)))
    if len(type_price(data, flag)) % 2 == 0:
        typeprice[index].append((type_price(data, flag)[len(type_price(data, flag)) // 2 - 1] + type_price(data, flag)[len(type_price(data, flag)) // 2]) / 2)
    else:
        typeprice[index].append(type_price(data, flag)[len(type_price(data, flag)) // 2])


def cal_location(locationprice, data, index):
    for key, value in location_price(data).items():
        locationprice[index][key] = round(sum(value) / len(value), 2)


def cal_forward(forwardprice, data, index):
    for key, value in forward_price(data).items():
        forwardprice[index][key] = round(sum(value) / len(value), 2)


def draw_3(totalprice, title):
    plt.figure()
    city_names = list(totalprice.keys())
    rent_mean = [n[0] for n in totalprice.values()]
    rent_max = [n[1] for n in totalprice.values()]
    rent_min = [n[2] for n in totalprice.values()]
    rent_median = [n[3] for n in totalprice.values()]
    fig, ax = plt.subplots(2, 2)
    bar_width = 0.7
    bar_x = city_names
    ax[0, 0].bar(bar_x, rent_mean, width=bar_width)
    ax[0, 0].set_title('均价')
    ax[0, 1].bar(bar_x, rent_max, width=bar_width)
    ax[0, 1].set_title('最高价')
    ax[1, 0].bar(bar_x, rent_min, width=bar_width)
    ax[1, 0].set_title('最低价')
    ax[1, 1].bar(bar_x, rent_median, width=bar_width)
    ax[1, 1].set_title('中位数')
    plt.suptitle(title)
    plt.savefig(f"./{title}.png", dpi=3000)


def draw_4(typeprice):
    plt.figure()
    fig, ax = plt.subplots(1, 4)
    cities = list(typeprice[0].keys())
    one = []
    two = []
    three = []
    for i in range(0, 4):
        one.append([n[i] for n in typeprice[0].values()])
        two.append([n[i] for n in typeprice[1].values()])
        three.append([n[i] for n in typeprice[2].values()])
    typetemp = ['均值', '最大值', '最小值', '中位数']
    for i in range(0, 4):
        ax[i].set_xticks(range(len(cities)))
        ax[i].set_xticklabels(cities)
        bar_width = 0.2
        ax[i].bar(range(len(cities)), one[i], bar_width, label='一居室')
        ax[i].bar([x + bar_width for x in range(len(cities))],
                  two[i], bar_width, label='二居室')
        ax[i].bar([x + 2 * bar_width for x in range(len(cities))],
                  three[i], bar_width, label='三居室')
        ax[i].legend()
        ax[i].set_title(typetemp[i])
    plt.suptitle('不同城市间一、二、三居室租金对比')
    plt.savefig("不同城市间一、二、三居室租金对比.png", dpi=3000)


totalprice = {'BT': [], 'BJ': [], 'SH': [], 'GZ': [], 'SZ': []}
cal_total(totalprice, data_BT, 'BT')
cal_total(totalprice, data_BJ, 'BJ')
cal_total(totalprice, data_SH, 'SH')
cal_total(totalprice, data_GZ, 'GZ')
cal_total(totalprice, data_SZ, 'SZ')
draw_3(totalprice, '总体房租情况')

unitprice = {'BT': [], 'BJ': [], 'SH': [], 'GZ': [], 'SZ': []}
cal_unit(unitprice, data_BT, 'BT')
cal_unit(unitprice, data_BJ, 'BJ')
cal_unit(unitprice, data_SH, 'SH')
cal_unit(unitprice, data_GZ, 'GZ')
cal_unit(unitprice, data_SZ, 'SZ')
draw_3(unitprice, '单位面积租金')

typeprice = [
    {'BT': [], 'BJ': [], 'SH': [], 'GZ': [], 'SZ': []},
    {'BT': [], 'BJ': [], 'SH': [], 'GZ': [], 'SZ': []},
    {'BT': [], 'BJ': [], 'SH': [], 'GZ': [], 'SZ': []}
]
for i in range(0, 3):
    cal_type(typeprice[i], data_BT, 'BT', i + 1)
for i in range(0, 3):
    cal_type(typeprice[i], data_BJ, 'BJ', i + 1)
for i in range(0, 3):
    cal_type(typeprice[i], data_SH, 'SH', i + 1)
for i in range(0, 3):
    cal_type(typeprice[i], data_GZ, 'GZ', i + 1)
for i in range(0, 3):
    cal_type(typeprice[i], data_SZ, 'SZ', i + 1)
draw_4(typeprice)

locationprice = {'BT': {}, 'BJ': {}, 'SH': {}, 'GZ': {}, 'SZ': {}}
cal_location(locationprice, data_BT, 'BT')
cal_location(locationprice, data_BJ, 'BJ')
cal_location(locationprice, data_SH, 'SH')
cal_location(locationprice, data_GZ, 'GZ')
cal_location(locationprice, data_SZ, 'SZ')
for name, item in locationprice.items():
    plt.figure()
    lengths = list(item.values())
    labels = list(item.keys())
    my_range = range(1, len(item) + 1)
    ymin = min(lengths) - 100
    ymax = max(lengths) + 200
    plt.vlines(x=my_range, ymin=0, ymax=lengths, colors='skyblue')
    plt.plot(lengths, my_range, "o")
    plt.ylim(ymin, ymax)
    plt.xticks(my_range, labels, rotation=90)
    plt.xlim(0, len(item) + 10)
    plt.ylabel('租金均价')
    plt.savefig(f"./{name}不同板块均价.png", dpi=3000)

forwardprice = {'BT': {}, 'BJ': {}, 'SH': {}, 'GZ': {}, 'SZ': {}}
cal_forward(forwardprice, data_BT, 'BT')
cal_forward(forwardprice, data_BJ, 'BJ')
cal_forward(forwardprice, data_SH, 'SH')
cal_forward(forwardprice, data_GZ, 'GZ')
cal_forward(forwardprice, data_SZ, 'SZ')
plt.figure()
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(10, 5))
for i, (city, data) in enumerate(forwardprice.items()):
    ax = axes[i]
    for direction, rents in data.items():
        ax.scatter(direction, rents)
    ax.set_xlabel("方向")
    ax.set_ylabel("租金均价")
    ax.set_title(city)
plt.tight_layout()
plt.savefig("./各城市不同朝向单位面积均价.png", dpi=3000)



