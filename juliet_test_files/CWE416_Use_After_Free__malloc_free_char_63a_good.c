/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE416_Use_After_Free__malloc_free_char_63a.c
Label Definition File: CWE416_Use_After_Free__malloc_free.label.xml
Template File: sources-sinks-63a.tmpl.c
*/
/*
 * @description
 * CWE: 416 Use After Free
 * BadSource:  Allocate data using malloc(), initialize memory block, and Deallocate data using free()
 * GoodSource: Allocate data using malloc() and initialize memory block
 * Sinks:
 *    GoodSink: Do nothing
 *    BadSink : Use data
 * Flow Variant: 63 Data flow: pointer to data passed from one function to another in different source files
 *
 * */

#include "std_testcase.h"

#include <wchar.h>

#ifndef OMITGOOD

/* goodG2B uses the GoodSource with the BadSink */
void CWE416_Use_After_Free__malloc_free_char_63b_goodG2BSink(char * * data);

static void goodG2B()
{
    char * data;
    /* Initialize data */
    data = NULL;
    data = (char *)malloc(100*sizeof(char));
    memset(data, 'A', 100-1);
    data[100-1] = '\0';
    /* FIX: Do not free data in the source */
    CWE416_Use_After_Free__malloc_free_char_63b_goodG2BSink(&data);
}

/* goodB2G uses the BadSource with the GoodSink */
void CWE416_Use_After_Free__malloc_free_char_63b_goodB2GSink(char * * data);

static void goodB2G()
{
    char * data;
    /* Initialize data */
    data = NULL;
    data = (char *)malloc(100*sizeof(char));
    memset(data, 'A', 100-1);
    data[100-1] = '\0';
    /* POTENTIAL FLAW: Free data in the source - the bad sink attempts to use data */
    free(data);
    CWE416_Use_After_Free__malloc_free_char_63b_goodB2GSink(&data);
}

void CWE416_Use_After_Free__malloc_free_char_63_good()
{
    goodG2B();
    goodB2G();
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
    CWE416_Use_After_Free__malloc_free_char_63_good();
    printLine("Finished good()");
#endif /* OMITGOOD */
    return 0;
}

#endif