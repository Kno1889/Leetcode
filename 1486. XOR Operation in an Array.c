int xorOperation(int n, int start){
    int* nums = malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++){
        nums[i] = start + 2 * i;
    }
    
    int result = nums[0]; 
    
    for(int j = 1; j < n; j++){
        result = result ^ nums[j];
    }
    
    return result;
}
