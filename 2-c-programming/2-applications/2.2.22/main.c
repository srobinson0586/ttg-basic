#include "exercise.h"


int main() {
    // TODO: Read exercise.h

    // TODO: Receive an allocated buffer of CARs by calling "buyMyCars()"
    char* buffer;

    // TODO: Determine the number of CARs you have and get a pointer to the first CAR structure in the buffer
    unsigned int numCars;
    CAR* myCarsPtr;
    
    // TODO: Print out the make of each of our new cars
        // Hint: Pay close attention to the types of the fields in CAR and MAKE_INFO 
        // Think of getting this value in the following way:
        // myCarsPtr                        CAR*        Points to buffer of cars                    ->| Car 1 | Car 2 | Car 3 | Car 4 |
        // myCarsPtr[i]                     CAR         Points to, then dereferences car i          Car i: || MAKE_INFO* | CAR_TYPE | WHEEL | WHEEL | WHEEL | WHEEL | PERSON* ||
        // myCarsPtr[i].make_info_ptr       MAKE_INFO*  Gets the ptr to the MAKE_INFO of car i      make_info_ptr: | MAKE_INFO* |
        // myCarsPtr[i].make_info_ptr->make char*       Dereferences MAKE_INFO*, then gets make     ->|F|o|r|d|  or  "Ford"

        // Note: if we want to iterate through all the cars, our for loop index (i) should be on the CAR* variable
        // Note: array notation arr[i] both points to element i and dereferences it
        // Note: the difference between useing "." and "->" to get a struct element is that you use "->" on a pointer to the struct to dereference it first:
        //          *(structPtr).element  :=  structPtr->element


    // TODO: for each car, print out whether it needs to put air in its wheels (i.e. if any of its 4 wheels are flat (non-zero))
    //      Hint: 2 cars need air in their wheels
    //      Hint: You should use 2 for loops, nested


    // TODO: We want to put people in each car. For each car, allocate a buffer to hold the correct numebr of passengers:
    //      if CAR_TYPE == SEDAN, 4 people
    //      if CAR_TYPE == SUV, 6 people
    //      if CAR_TYPE == TRUCK, 2 people
    //
    //      Hint: the allocated space should be pointed to by PERSON* passengers


    // This will add the people to the cars in the space you just allocated
    addPeopleToCars(myCarsPtr);

    // TODO: Print the name of the second passenger in your third car (assume you have a third car)?
    //      Hint: Correct answer is Billy


    // TODO: We are done with the cars. For each car,
    //    free the space we allocated for each set of passengers


    // TODO: Free the space allocated for the cars


    return 0;
}
