import termtables
from rich import box
from rich.table import Table
from rich.console import Console

# 表示12，即最大轮次为12
max_round = 12


# 这个函数对应文档的第κ步骤(第五步)
# 参数说明
# * s_input 输入的4*5数组
# * round_no 当前的轮次数（0-11）
# 返回值
# * s_output 输出的4*5数组
def kappa(s_input: list, round_no: int) -> list:
    constant = [
        0x0091A2B3C4D5E6F7, 0x0048D159E26AF37B, 0x002468ACF13579BD, 0x00123456F89ABCDE,
        0x00091A2BFC4D5E6F, 0x00048D15FE26AF37, 0x0002468AFF13579B, 0x000123457F89ABCD,  # todo
        0x000091A2BFC4D5E6, 0x000048D1DFE26AF3, 0x00002468EFF13579, 0x00001234F7F89ABC]
    # 定义一个4*5的数组，并把输入的数组拷贝到这个数组中
    s_output = s_input.copy()
    # 对输出的数组的元素做异或操作（根据轮次的不同，异或不同的值）
    s_output[0][0] = s_output[0][0] ^ constant[round_no]
    return s_output


# 这个函数对应文档的第µ步骤(第一步)
# 参数说明
# * s_input 输入的4*5数组
# 返回值
# * s_output 输出的4*5数组
def mu(s_input: list) -> list:
    # 定义4*5的结果数组，初始化为0
    s_output = [[0] * 5 for _ in range(4)]

    # 异或运算的逻辑
    s_output[0][0] = s_input[0][4] ^ s_input[1][0] ^ s_input[2][0] ^ s_input[3][0]
    s_output[0][1] = s_input[0][0] ^ s_input[1][1] ^ s_input[2][1] ^ s_input[3][1]
    s_output[0][2] = s_input[0][4] ^ s_input[0][1] ^ s_input[1][2] ^ s_input[2][2] ^ s_input[3][2]
    s_output[0][3] = s_input[0][2] ^ s_input[1][3] ^ s_input[2][3] ^ s_input[3][3]
    s_output[0][4] = s_input[0][3] ^ s_input[1][4] ^ s_input[2][4] ^ s_input[3][4]

    s_output[1][0] = s_input[0][0] ^ s_input[1][0] ^ s_input[2][1] ^ s_input[3][4]
    s_output[1][1] = s_input[0][1] ^ s_input[1][1] ^ s_input[2][2] ^ s_input[2][0] ^ s_input[3][0]
    s_output[1][2] = s_input[0][2] ^ s_input[1][2] ^ s_input[2][3] ^ s_input[3][4] ^ s_input[3][1]
    s_output[1][3] = s_input[0][3] ^ s_input[1][3] ^ s_input[2][4] ^ s_input[3][2]
    s_output[1][4] = s_input[0][4] ^ s_input[1][4] ^ s_input[2][0] ^ s_input[3][3]

    s_output[2][0] = s_input[0][0] ^ s_input[1][4] ^ s_input[2][0] ^ s_input[3][1]
    s_output[2][1] = s_input[0][1] ^ s_input[1][0] ^ s_input[2][1] ^ s_input[3][2] ^ s_input[3][0]
    s_output[2][2] = s_input[0][2] ^ s_input[1][4] ^ s_input[1][1] ^ s_input[2][2] ^ s_input[3][3]
    s_output[2][3] = s_input[0][3] ^ s_input[1][2] ^ s_input[2][3] ^ s_input[3][4]
    s_output[2][4] = s_input[0][4] ^ s_input[1][3] ^ s_input[2][4] ^ s_input[3][0]

    s_output[3][0] = s_input[0][0] ^ s_input[1][1] ^ s_input[2][4] ^ s_input[3][0]
    s_output[3][1] = s_input[0][1] ^ s_input[1][2] ^ s_input[1][0] ^ s_input[2][0] ^ s_input[3][1]
    s_output[3][2] = s_input[0][2] ^ s_input[1][3] ^ s_input[2][4] ^ s_input[2][1] ^ s_input[3][2]
    s_output[3][3] = s_input[0][3] ^ s_input[1][4] ^ s_input[2][2] ^ s_input[3][3]
    s_output[3][4] = s_input[0][4] ^ s_input[1][0] ^ s_input[2][3] ^ s_input[3][4]

    return s_output


# 没有逻辑功能，只是用来打印数组的
def print_array(s: list):
    table = Table(show_header=False, header_style="bold magenta", box=box.ASCII, show_lines=True)
    for i in range(len(s)):
        table.add_row('0x{:08X}'.format(s[i][0]), '0x{:08X}'.format(s[i][1]), '0x{:08X}'.format(s[i][2]),
                      '0x{:08X}'.format(s[i][3]), '0x{:08X}'.format(s[i][4]))
    console = Console()
    console.print(table)


# 循环位移函数
# 参数说明
# * a 输入的64位无符号整数
# * k 输入的位移量（正数表示左移，负数表示右移）
# 返回值
# * a 输出的64位无符号整数（位移后的结果）
def loop_move(a: int, k: int) -> int:
    b = bin(a)
    b = b[2:]
    b = b.zfill(64)
    if k < 0:
        b = b[-k:] + b[:-k]
    else:
        b = b[k:] + b[:k]
    return int(b, 2)


# 这个函数对应文档的第ρ步骤（第二步）
# 参数说明
# * s_input 输入的4*5数组
# 返回值
# * s_output 输出的4*5数组
def rho(s_input: list) -> list:
    # 定义4*5的结果数组，初始化为0
    s_output = [[0] * 5 for _ in range(4)]

    # 位移运算的逻辑
    s_output[0][0] = s_input[0][0]  # 改元素不需要位移
    s_output[0][1] = loop_move(s_input[0][1], 36)
    s_output[0][2] = loop_move(s_input[0][2], 3)
    s_output[0][3] = loop_move(s_input[0][3], 41)
    s_output[0][4] = loop_move(s_input[0][4], 18)

    s_output[1][0] = loop_move(s_input[1][0], 1)
    s_output[1][1] = loop_move(s_input[1][1], 44)
    s_output[1][2] = loop_move(s_input[1][2], 10)
    s_output[1][3] = loop_move(s_input[1][3], 45)
    s_output[1][4] = loop_move(s_input[1][4], 2)

    s_output[2][0] = loop_move(s_input[2][0], 62)
    s_output[2][1] = loop_move(s_input[2][1], 6)
    s_output[2][2] = loop_move(s_input[2][2], 43)
    s_output[2][3] = loop_move(s_input[2][3], 15)
    s_output[2][4] = loop_move(s_input[2][4], 61)

    s_output[3][0] = loop_move(s_input[3][0], 28)
    s_output[3][1] = loop_move(s_input[3][1], 55)
    s_output[3][2] = loop_move(s_input[3][2], 25)
    s_output[3][3] = loop_move(s_input[3][3], 21)
    s_output[3][4] = loop_move(s_input[3][4], 56)
    return s_output


# 这个函数对应文档的第π步骤（第三步）
# 参数说明
# * s_input 输入的4*5数组
# 返回值

def pi(s_input: list) -> list:
    # 定义4*5的结果数组，初始化为0
    s_output = [[0] * 5 for _ in range(4)]
    # 循环计算每个位置输出的值
    for x in range(4):
        for y in range(5):
            xx = (x + y) % 4
            yy = (xx + y + 1) % 5
            s_output[xx][yy] = s_input[x][y]
    return s_output


# 这个函数对应文档的第ψ步骤（第四步）
# 参数说明
# * s_input 输入的4*5数组
# 返回值
# * s_output 输出的4*5数组
def psi(s_input: list) -> list:
    for x in range(4):
        tmp1 = s_input[x][0] & s_input[x][1] & s_input[x][2] & s_input[x][3] & s_input[x][4]
        tmp2 = (no_bit(s_input[x][0])) & (no_bit(s_input[x][1])) & (no_bit(s_input[x][2])) & (no_bit(s_input[x][3]))& (no_bit(s_input[x][4]))
        s_input[x][0] = s_input[x][0] ^ ((no_bit(s_input[x][1])) & s_input[x][2]) ^ tmp1 ^ tmp2
        s_input[x][1] = s_input[x][1] ^ ((no_bit(s_input[x][2])) & s_input[x][3]) ^ tmp1 ^ tmp2
        s_input[x][2] = s_input[x][2] ^ ((no_bit(s_input[x][3])) & s_input[x][4]) ^ tmp1 ^ tmp2
        s_input[x][3] = s_input[x][3] ^ ((no_bit(s_input[x][4])) & s_input[x][0]) ^ tmp1 ^ tmp2
        s_input[x][4] = s_input[x][4] ^ ((no_bit(s_input[x][0])) & s_input[x][1]) ^ tmp1 ^ tmp2
    return s_input


def round_loop(s_input: list, round_no: int) -> list:
    print(f"round{round_no + 1} step µ:")
    s_input = mu(s_input)
    print_array(s_input)
    print(f"round{round_no + 1} step ρ:")
    s_input = rho(s_input)
    print_array(s_input)
    print(f"round{round_no + 1} step π:")
    s_input = pi(s_input)
    print_array(s_input)
    print(f"round{round_no + 1} step ψ:")
    s_input = psi(s_input)
    print_array(s_input)
    print(f"round{round_no + 1} step κ:")
    s_input = kappa(s_input, round_no)
    print_array(s_input)
    return s_input


# 封装后的取反函数，主要是为了解决python中的数字是有符号数
def no_bit(n: int) -> int:
    n = ~n
    if n < 0:
        n &= 0xFFFFFFFFFFFFFFFF
    return i


if __name__ == "__main__":
    # 数据输入
    source = [
        [0x0000000000000001, 0x0000000000000002, 0x0000000000000003, 0x0000000000000004, 0x0000000000000005],
        [0x0000000000000006, 0x0000000000000007, 0x0000000000000008, 0x0000000000000009, 0x000000000000000A],
        [0x000000000000000B, 0x000000000000000C, 0x000000000000000D, 0x000000000000000E, 0x000000000000000F],
        [0x0000000000000010, 0x0000000000000011, 0x0000000000000012, 0x0000000000000013, 0x0000000000000014]
    ]
    print(f"source data:")
    print_array(source)
    for i in range(max_round):
        source = round_loop(source, i)
