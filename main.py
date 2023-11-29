# 表示12，即最大轮次为12
max_round = 12


# 这个函数对应文档的第κ步骤
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
