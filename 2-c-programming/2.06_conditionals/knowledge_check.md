# C Programming Conditionals - Knowledge Check

[Back to README](README.md)

1. Given this source code for a color picker:
    ```c
    #include <stdio.h>
    
    int main() {
        int colorCode;
    
        printf("Enter a number from 1 to 8: ");
        scanf("%d", &colorCode);
    
        switch (colorCode) {
            case 1:
                printf("Purple\n");
                break;
            case 3:
                printf("Brown\n");
                break;
            case 5:
                printf("Pink\n");
                break;
            case 2:
                printf("Green\n");
                break;
            case 8:
                printf("Orange\n");
                break;
            case 6:
                printf("Red\n");
                break;
            case 4:
                printf("Blue\n");
                break;
            case 7:
                printf("Yellow\n");
                break;
            default:
                printf("Unknown color\n");
        }
    
        return 0;
    }
    ```

a. What color is chosen when `5` is entered?

b. What color is chosen when `7` is entered?

c. What color is chosen when `9` is entered?

d. What color is chosen when `1` is entered?

```
ANSWER: 
a.
b.
c.
d.
```

2. Given this source code for a movie ticket price calculator: 
    ```c
    #include <stdio.h>

    int main() {
        int age;
        double ticketPrice = 0.0;
        char timeOfDay;

        printf("Enter your age: ");
        scanf("%d", &age);

        printf("Enter the time of the movie (M for matinee, E for evening): ");
        scanf(" %c", &timeOfDay);

        if (age >= 8 && age <= 12) {
            if (timeOfDay == 'M') {
                ticketPrice = 6.50;
            } else {
                ticketPrice = 9.50;
            }
        } else if (age >= 13 && age <= 17) {
            if (timeOfDay == 'M') {
                ticketPrice = 8.50;
            } else {
                ticketPrice = 11.50;
            }
        } else if (age >= 18 && age <= 64) {
            if (timeOfDay == 'M') {
                ticketPrice = 10.50;
            } else {
                ticketPrice = 13.50;
            }
        } else if (age >= 65) {
            if (timeOfDay == 'M') {
                ticketPrice = 7.50;
            } else {
                ticketPrice = 10.50;
            }
        } else {
            printf("Invalid age.\n");
            return 1; // Exit with an error code
        }

        printf("Your ticket price is: $%.2lf\n", ticketPrice);

        return 0;
    }
    ```

a. What is the output when `age` is `15` and `time` is `matinee`?

b. What is the output when `age` is `35` and `time` is `evening`?

c. What is the output when `age` is `7` and `time` is `evening`?

```
ANSWER:
a.
b.
c.
```

[Back to README](README.md)