#include <iostream>
#define MAXROUND 12



int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

// 这个函数对应文档的第κ步骤
// 参数说明
// * s_output 输出的4*5数组
// * s_input 输入的4*5数组
// * round_no 当前的轮次数（0-11）
void Kappa(uint64_t s_output[4][5], uint64_t s_input[4][5], int round_no)
{
    // MAXROUND 表示12，即最大轮次为12
    // 下面的数组定义了每个轮次数组[0][0]元素在这一轮计算中异或的常数 （附录A）Appendix A
    // 其中0x前缀表示该数字为16进制，ULL后缀表示数据类型为无符号长整形（如果看不懂这句话就在脑海里把前缀和后缀删掉就行）
    const uint64_t constant[MAXROUND] = {
    0x0091A2B3C4D5E6F7ULL, 0x0048D159E26AF37BULL, 0x002468ACF13579BDULL, 0x00123456F89ABCDEULL,
    0x00091A2BFC4D5E6FULL, 0x00048D15FE26AF37ULL, 0x0002468AFF13579BULL, 0x000123457F89ABCDULL,
    0x000091A2BFC4D5E6ULL, 0x000048D1DFE26AF3ULL, 0x00002468EFF13579ULL, 0x00001234F7F89ABCULL };

    // 下面的操作主要是用两层for循环把输入数组的数据拷贝到输出的数组中
    unsigned int x,y;
    for(x = 0; x < 4; ++x) {
        for(y = 0; y < 5; ++y) {
            s_output[x][y] = s_input[x][y];
        }
    }

    // 对输出的数组的元素做异或操作（根据轮次的不同，异或不同的值）
    s_output[0][0] = s_output[0][0] ^ constant[round_no];
}
