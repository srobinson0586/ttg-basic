# C Programming: Strings

Strings are actually one-dimensional array of characters terminated by a **null** character '\0'. Thus a null-terminated string contains the characters that comprise the string followed by a **null**.

The following declaration and initialization create a string consisting of the word "Hello". To hold the null character at the end of the array, the size of the character array containing the string is one more than the number of characters in the word "Hello."

```c
char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
```

If you follow the rule of array initialization then you can write the above statement as follows:

```c
char greeting[] = "Hello";
```

Following is the memory presentation of the above defined string in C/C++:

![String Presentation in C/C++](../images/string_representation.jpg)

Actually, you do not place the _null_ character at the end of a string constant. The C compiler automatically places the '\0' at the end of the string when it initializes the array. Let us try to print the above mentioned string:

```c
#include <stdio.h>

int main () {

   char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
   printf("Greeting message: %s\n", greeting );
   return 0;
}
```

When the above code is compiled and executed, it produces the following result:

```
Greeting message: Hello
```

C supports a wide range of functions that manipulate null-terminated strings:

Function | Purpose
-------- | --------
**strcpy(s1, s2);** | Copies string s2 into string s1.
**strcat(s1, s2);** | Concatenates string s2 onto the end of string s1.
**strlen(s1);** | Returns the length of string s1.
**strcmp(s1, s2);** | Returns 0 if s1 and s2 are the same; less than 0 if s1<s2; greater than 0 if s1>s2.
**strchr(s1, ch);** | Returns a pointer to the first occurrence of character ch in string s1.
**strstr(s1, s2);** | Returns a pointer to the first occurrence of string s2 in string s1.

The following example uses some of the above-mentioned functions:

```c
#include <stdio.h>
#include <string.h>

int main () {

   char str1[12] = "Hello";
   char str2[12] = "World";
   char str3[12];
   int  len ;

   /* copy str1 into str3 */
   strcpy(str3, str1);
   printf("strcpy( str3, str1) :  %s\n", str3 );

   /* concatenates str1 and str2 */
   strcat( str1, str2);
   printf("strcat( str1, str2):   %s\n", str1 );

   /* total lenghth of str1 after concatenation */
   len = strlen(str1);
   printf("strlen(str1) :  %d\n", len );

   return 0;
}
```

When the above code is compiled and executed, it produces the following result:

```bash
strcpy( str3, str1) :  Hello
strcat( str1, str2):   HelloWorld
strlen(str1) :  10
```

Stack strings **cannot** be resized after they are created. Because of this, you might see some developers create character arrays that are larger than the strings that they intend to store in them. Take the following code for example:

```c
#include <stdio.h>
#include <string.h>

int main(){

   char greeting[64];

   strcpy(greeting, "howdy");
   printf("First greeting: %s\n", greeting);

   strcpy(greeting, "look who the cat dragged in");
   printf("Second greeting: %s\n", greeting);

   return 0;
}
```

The `greeting` array is large enough to hold 63 characters plus a null byte. This allows it to be reused to if we ever need to change the string it holds (so long as the string we are swapping is not greater than 64 bytes). When compiled and executed, the program produces the following output:

```
First greeting: howdy
Second greeting: look who the cat dragged in
```

## Resources

- [C Strings - GeeksforGeeks](https://www.geeksforgeeks.org/strings-in-c)

## Sources

- [TutorialsPoint - C Strings](https://www.tutorialspoint.com/cprogramming/c_strings.htm)

[Back to README](README.md)