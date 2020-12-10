// 输入一行字符，分别统计出其中英文字母、空白符（包括空格、制表、换行）、数字和其它字符的个数。
#include <stdio.h>

int main(){
    int c, nletter, ndigit, nwhite, nother;
    nletter = ndigit = nwhite = nother = 0;

    printf("input some word：");
    while((c = getchar()) != EOF) {  // 每次读取一个字符，回车时结束
        if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z')
            nletter++;
        else if (c == ' ' || c == '\n' || c == '\t')
            nwhite++;
        else if (c >= '0' && c <= '9')
            ndigit++;
        else
            nother++;
    }
    
    printf("\nletter = %d, digit = %d, white = %d, other = %d\n", nletter, ndigit, nwhite, nother);
    return 0;
}