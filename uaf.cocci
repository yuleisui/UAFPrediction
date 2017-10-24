@@
expression E;
expression E2 != NULL;
expression f;
@@
- free(E);
... when != free(E)
(
free(E);
|
E2 = E;
+ free(E);
+ E = NULL;
|
f (<+...E...+>);
+ free(E);
+ E = NULL;
)

