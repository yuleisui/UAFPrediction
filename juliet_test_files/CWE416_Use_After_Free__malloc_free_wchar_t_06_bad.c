/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE416_Use_After_Free__malloc_free_wchar_t_06.c
Label Definition File: CWE416_Use_After_Free__malloc_free.label.xml
Template File: sources-sinks-06.tmpl.c
*/
/*
 * @description
 * CWE: 416 Use After Free
 * BadSource:  Allocate data using malloc(), initialize memory block, and Deallocate data using free()
 * GoodSource: Allocate data using malloc() and initialize memory block
 * Sinks:
 *    GoodSink: Do nothing
 *    BadSink : Use data
 * Flow Variant: 06 Control flow: if(STATIC_CONST_FIVE==5) and if(STATIC_CONST_FIVE!=5)
 *
 * */

#include "std_testcase.h"

#include <wchar.h>

/* The variable below is declared "const", so a tool should be able
   to identify that reads of this will always give its initialized
   value. */
static const int STATIC_CONST_FIVE = 5;

#ifndef OMITBAD

void CWE416_Use_After_Free__malloc_free_wchar_t_06_bad()
{
    wchar_t * data;
    /* Initialize data */
    data = NULL;
    if(STATIC_CONST_FIVE==5)
    {
        data = (wchar_t *)malloc(100*sizeof(wchar_t));
        wmemset(data, L'A', 100-1);
        data[100-1] = L'\0';
        /* POTENTIAL FLAW: Free data in the source - the bad sink attempts to use data */
        free(data);
    }
    if(STATIC_CONST_FIVE==5)
    {
        /* POTENTIAL FLAW: Use of data that may have been freed */
        printWLine(data);
        /* POTENTIAL INCIDENTAL - Possible memory leak here if data was not freed */
    }
}

#endif /* OMITBAD */

/* Below is the main(). It is only used when building this testcase on
   its own for testing or for building a binary to use in testing binary
   analysis tools. It is not used when compiling all the testcases as one
   application, which is how source code analysis tools are tested. */

#ifdef INCLUDEMAIN

int main(int argc, char * argv[])
{
    /* seed randomness */
    srand( (unsigned)time(NULL) );
#ifndef OMITBAD
    printLine("Calling bad()...");
    CWE416_Use_After_Free__malloc_free_wchar_t_06_bad();
    printLine("Finished bad()");
#endif /* OMITBAD */
    return 0;
}

#endif