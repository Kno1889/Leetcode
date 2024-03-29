// PSEUDOCODE: 
// allocate memory for return array, target
// insert elements. If an element already exists at required index, shift all elements after this index forward by one

// numSize = indexSize = returnSize
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize){
    
int* target = malloc(indexSize * sizeof(int));

*returnSize=indexSize;

for(int i = 0; i < indexSize; i++){
    target[i] = -1;
}

for(int i = 0; i < indexSize; i++){
    
    if(target[index[i]] == -1)
        target[index[i]] = nums[i];
    
    else{        
        for(int j = indexSize-1; j > index[i]; j--){
            target[j] = target[j-1];
        }
        target[index[i]]=nums[i];
    }
}


return target;
}
