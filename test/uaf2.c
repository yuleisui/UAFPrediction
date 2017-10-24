#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printLine (const char *line){
    if(line != NULL) 
        printf("%s\n", line);
}

void uaf_char_bad(){
	char *data;
	data = NULL;
	data = (char*)malloc(100*sizeof(char));
	memset(data, 'A', 99);
	data[99] = '\0';
	free(data);
    printline(data);
}

int main(int argc, char* argv[]){
	uaf_char_bad();
	return 0;
} 
