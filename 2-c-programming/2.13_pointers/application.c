int main(){
    int x = 10;
    //TODO:: create a pointer and that points to x 
    
    //TODO::call ptrFunction to change x value to 20

    if (x != 20){
        printf("Value was not changed");
        return 1;
    }
    
    return 0;
}
void ptrFunction(int* ptr){
    *ptr = 20;
}
