// #include <stdio.h>
// #include <stdlib.h>

#define SIZE 11

void convert_numerical_system(unsigned base_10, char *s, unsigned base);


int main()
{
    unsigned num, base;
    char s[SIZE];
    printf("Enter number is decimal numerical system: ");
    scanf("%u", &num);
    printf("Enter base in which the number is going to be converted: ");
    scanf("%u", &base);

    convert_numerical_system(num, s, base);

    printf("%s", s);

    return 0;
}

void convert_numerical_system(unsigned base_10, char *s, unsigned base)
{
    char remainder;
    int d = SIZE - 1;

    if(base_10 == 0)
    {
        printf("Your number in %d base is: %d", base, base_10);
    }

    while(base_10 > 0)
    {
        remainder = base_10 % base;
        switch(remainder)
        {
            case 10:
                remainder = 'A';
                break;
            case 11:
                remainder = 'B';
                break;
            case 12:
                remainder = 'C';
                break;
            case 13:
                remainder = 'D';
                break;
            case 14:
                remainder = 'E';
                break;
            case 15:
                remainder = 'F';
                break;
            default:
                break;
        }
        s[d--] = remainder;
        base_10 /= base;
    }
    s[SIZE] = '\0';
}
