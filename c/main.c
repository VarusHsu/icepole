#include "icepole.h"
#include <stdio.h>
int main() {
    ICESTATE input = {
            {0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005},
            {0x00000006, 0x00000007, 0x00000008, 0x00000009, 0x0000000A},
            {0x0000000B, 0x0000000C, 0x0000000D, 0x0000000E, 0x0000000F},
            {0x00000010, 0x00000011, 0x00000012, 0x00000013, 0x00000014}};
    ICESTATE output;
    P12(output, input);
    return 0;
}
