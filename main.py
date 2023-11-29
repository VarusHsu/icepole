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
        0x00091A2BFC4D5E6F, 0x00048D15FE26AF37, 0x0002468AFF13579, 0x000123457F89ABCD,  # todo
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
    s_output = [[0] * 5] * 4

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
    if k < 0:
        k = -k
        a = (a >> k | a << (64 - k))
    else:
        a = (a << k | a >> (64 - k))
    return a


if __name__ == "__main__":
    # 数据输入
    source = [
        [0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005],
        [0x00000006, 0x00000007, 0x00000008, 0x00000009, 0x0000000A],
        [0x0000000B, 0x0000000C, 0x0000000D, 0x0000000E, 0x0000000F],
        [0x00000010, 0x00000011, 0x00000012, 0x00000013, 0x00000014]
    ]
    print("source:")
    print_array(source)
    print("step µ:")
    source = mu(source)
    print_array(source)
