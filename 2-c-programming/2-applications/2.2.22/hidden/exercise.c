#include "../exercise.h"

MAKE_INFO a = {"BMW", "Germany"};
MAKE_INFO b = {"Ford", "USA"};
MAKE_INFO c = {"Audi", "Germany"};
MAKE_INFO d = {"Toyota", "Japan"};

char* buyMyCars() {
	unsigned int* buffer = malloc(sizeof(unsigned int) + 4*sizeof(CAR));
	buffer[0] = 4;
	CAR* cars = (CAR*)(&(buffer[1]));
	cars[0].make_info_ptr = &a;
	cars[0].type = SEDAN;
	cars[0].wheels[0].flat = 0;
	cars[0].wheels[1].flat = 0;
	cars[0].wheels[2].flat = 0;
	cars[0].wheels[3].flat = 0;
	cars[0].passengers = NULL;

	cars[1].make_info_ptr = &b;
	cars[1].type = TRUCK;
	cars[1].wheels[0].flat = 0;
	cars[1].wheels[1].flat = 1;
	cars[1].wheels[2].flat = 1;
	cars[1].wheels[3].flat = 0;
	cars[1].passengers = NULL;	
	
	cars[2].make_info_ptr = &c;
	cars[2].type = SEDAN;
	cars[2].wheels[0].flat = 0;
	cars[2].wheels[1].flat = 0;
	cars[2].wheels[2].flat = 0;
	cars[2].wheels[3].flat = 1;
	cars[2].passengers = NULL;	
	
	cars[3].make_info_ptr = &d;
	cars[3].type = SUV;
	cars[3].wheels[0].flat = 0;
	cars[3].wheels[1].flat = 0;
	cars[3].wheels[2].flat = 0;
	cars[3].wheels[3].flat = 0;
	cars[3].passengers = NULL;

	return (char*)buffer;
}

void addPeopleToCars(CAR* myCarsPtr) {
	size_t i, j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < myCarsPtr[i].type; j++) {
			myCarsPtr[i].passengers[j].age = "22";
			myCarsPtr[i].passengers[j].name = "Bob";
		}
	}
	myCarsPtr[2].passengers[1].name = "Billy";
}
