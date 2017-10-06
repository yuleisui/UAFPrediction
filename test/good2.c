#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printLine (const char * line)
{
    if(line != NULL) 
    {
        printf("%s\n", line);
    }
}

static char * helperGood(char * aString)
{
    size_t i = 0;
    size_t j;
    char * reversedString = NULL;
    if (aString != NULL)
    {
        i = strlen(aString);
        reversedString = (char *) malloc(i+1);
        for (j = 0; j < i; j++)
        {
            reversedString[j] = aString[i-j-1];
        }
        reversedString[i] = '\0';
        /* FIX: Do not free the memory before returning */
        return reversedString;
    }
    else
    {
        return NULL;
    }
}

static void good()
{
    {
        /* Call the good helper function */
        char * reversedString = helperGood("GoodSink");
        printLine(reversedString);
        free(reversedString);
         // * This call to free() was removed because we want the tool to detect the use after free,
         // * but we don't want that function to be free(). Essentially we want to avoid a double free
         
    }
}

int main(int argc, char const *argv[])
{
	good();
	return 0;
}