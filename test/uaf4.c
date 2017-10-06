#include <stdio.h>
#include <stdlib.h>

void printIntLine (int intNumber){
    printf("%d\n", intNumber);
}

void uaf_char_bad(){

	int *data;

    data = NULL;
    data = (int *)malloc(100*sizeof(int));
    {
        size_t i;
        for(i = 0; i < 100; i++)
        {
            data[i] = 5;
        }
    }
    free(data);    
    printIntLine(data[0]);
}


int main(int argc, char* argv[]){
	uaf_char_bad();
	return 0;
}