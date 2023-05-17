/*
 * Dewey Decimal Classification (DDC)
 * https://www.library.illinois.edu/infosci/research/guides/dewey/
 */
typedef enum _CATEGORY {
    DRAMA,
    FICTION,
    NON_FICTION,
    MILITARY_SCIENCE
} CATEGORY;

typedef struct _DDC {
    char call_number[3];
    char *category_name;
} DDC;

typedef struct _BOOK {
    char *title;
    char *author;
    DDC dewey_decimal;
} BOOK;
