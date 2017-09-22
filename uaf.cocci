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
@@
expression E;
expression E2 != NULL;
expression f;
@@
- OPENSSL_free(E);
... when != OPENSSL_free(E)
(
OPENSSL_free(E);
|
E2 = E;
+ OPENSSL_free(E);
+ E = NULL;
|
f (<+...E...+>);
+ OPENSSL_free(E);
+ E = NULL;
)