void reverseString(char *s, int sSize)
{
    int tail_ind = sSize - 1;
    int head_ind = 0;

    while (tail_ind > head_ind)
    {
        char temp = s[head_ind];
        s[head_ind] = s[tail_ind];
        s[tail_ind] = temp;

        head_ind++;
        tail_ind--;
    }
}