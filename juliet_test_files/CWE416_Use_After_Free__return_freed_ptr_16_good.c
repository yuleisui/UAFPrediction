/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE416_Use_After_Free__return_freed_ptr_16.c
Label Definition File: CWE416_Use_After_Free__return_freed_ptr.label.xml
Template File: point-flaw-16.tmpl.c
*/
/*
 * @description
 * CWE: 416 Use After Free
 * Sinks:
 *    GoodSink: Use a block of memory returned from a function
 *    BadSink : Use a block of memory returned from a function after it has been freed
 * Flow Variant: 16 Control flow: while(1)
 *
 * */

#include "std_testcase.h"

static char * helperBad(char * aString)
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
        /* FLAW: Freeing a memory block and then returning a pointer to the freed memory */
        free(reversedString);
        return reversedString;
    }
    else
    {
        return NULL;
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

#ifndef OMITGOOD

/* good1() uses the GoodSinkBody in the while loop */
static void good1()
{
    while(1)
    {
        {
            /* Call the good helper function */
            char * reversedString = helperGood("GoodSink");
            printLine(reversedString);
            /* free(reversedString);
             * This call to free() was removed because we want the tool to detect the use after free,
             * but we don't want that function to be free(). Essentially we want to avoid a double free
             */
        }
        break;
    }
}

void CWE416_Use_After_Free__return_freed_ptr_16_good()
{
    good1();
}

#endif /* OMITGOOD */

/* Below is the main(). It is only used when building this testcase on
   its own for testing or for building a binary to use in testing binary
   analysis tools. It is not used when compiling all the testcases as one
   application, which is how source code analysis tools are tested. */

#ifdef INCLUDEMAIN

int main(int argc, char * argv[])
{
    /* seed randomness */
    srand( (unsigned)time(NULL) );
#ifndef OMITGOOD
    printLine("Calling good()...");
    CWE416_Use_After_Free__return_freed_ptr_16_good();
    printLine("Finished good()");
#endif /* OMITGOOD */
    return 0;
}

#endif