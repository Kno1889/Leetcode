/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *shuffle(int *nums, int numsSize, int n, int *returnSize)
{

    int *shuffled = (int *)malloc(sizeof(int) * 2 * n);

    // for n = 4, need 0, 4, 1, 5, 2, 6, 3, 7
    //      in indices 0, 1, 2, 3, 4, 5, 6, 7

    for (int i = 0; i < n; i++)
    {
        shuffled[2 * i] = nums[i];
        shuffled[2 * i + 1] = nums[i + n];
    }

    return shuffled;
}

void main()
{
    int num = {1, 2, 3, 4, 4, 3, 2, 1};
    int *nums = num;
    int *shuffled = shuffle(nums, 8, 4, 8);

    for (int i = 0; i < 8; i++)
    {
        printf("%d ", shuffled[i]);
    }
}