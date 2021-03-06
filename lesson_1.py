# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().

from ipaddress import ip_address
import subprocess
import random
import re
from tabulate import tabulate


def random_ipv4(foo: int) -> list:
    """Создает список случайных ip адресов.
    :param foo: цисло узлов
    :return: список ip
    """
    ip_list = []
    for i in range(foo):
        str = ip_address(
            f'77.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}')
        ip_list.append(str)
    return ip_list


def host_ping(bar: list):
    """Проверяет доступность ip адресов.
    -w 2 -- останавливаеn пинг через 2 сек, на тот случай если ip мертв
    -с 2 -- отправляем 2 пакета больше не нужно для наших целей
    :param bar: список узлов
    :return: Узел доступен/Узел недоступен
    """
    for i in bar:
        p = subprocess.Popen(f'ping {i} -w 2 -c 2',
                             shell=True, stdout=subprocess.PIPE)

        if re.search('100% packet loss', p.stdout.read().decode()):
            print(f'Узел {i} не доступен')
        else:
            print(f'Узел {i} доступен')

# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
# октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.


def host_range_ping(number: int, ip: str) -> list:
    """Функция перебора ip адресов из заданного диапазона. тк меняется только
    последний октет то идет прибавка 1 к последнему октету в ip адресе.
    :param number: целое цисло - количество ip адресов
    :param ip:  начальный ip адресс
    :return: список айпи адресов
    """
    try:
        bar = []
        foo = ip_address(ip)
        for i in range(number):
            bar.append(foo+i)
        return bar
    except TypeError:
        print('Введите целое число')

# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
# результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).


def host_range_ping_tab(bar: list) -> str:
    """Функция распределяет переданные аругментом список ip адресов на те
    которые пингуются и нет.
    :param bar: Список ip адресов
    :return: Две колонки с работающими и не работающими ip адресами
    """
    reach, unreach = [], []
    try:
        for i in bar:
            p = subprocess.Popen(f'ping {i} -w 2 -c 2',
                                 shell=True, stdout=subprocess.PIPE)
            if re.search('100% packet loss', p.stdout.read().decode()):
                unreach.append(i)
                print(f'Узел {i} не доступен')
            else:
                reach.append(i)
                print(f'Узел {i} доступен')
        ip = {'Reachable': reach, 'Unreachable': unreach}
        print(tabulate(ip, headers='keys'))
    except TypeError:
        print('Передайте аргументом список ip адресов')

# 4. Продолжаем работать над проектом «Мессенджер»:
# a) Реализовать скрипт, запускающий два клиентских приложения: на чтение чата и на запись в него. Уместно использовать модуль subprocess).

for i in range(2):
    p = subprocess.call('xfce4-terminal -H -e "python3 client_6.py"', executable='/bin/bash', shell=True)

# b) Реализовать скрипт, запускающий указанное количество клиентских приложений.
if __name__ == '__main__':
    bar = random_ipv4(5)
    foo = (host_range_ping(8, '87.250.250.250'))
    print(host_ping(bar))
    print(host_range_ping_tab(foo))
