/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize){
    *returnSize = encodedSize + 1; // defining the size of the original array's length
    
    int* arr = malloc((*returnSize)*sizeof(int)); // allocatng memory for the original array, arr
    
    arr[0] = first;
    
    for (int i = 0;i < encodedSize; i++){
        arr[i+1] = arr[i] ^ encoded[i];
    }
    
    return arr;
}
