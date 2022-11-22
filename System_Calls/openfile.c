// open system call
#include<stdio.h>
#include<fcntl.h> //Library for File Control
int errno; //Error Number
int main()
{
// if file does not have in directory
// then file foo.txt is created.
int fd = open("foo.txt", O_RDONLY | O_CREAT); //Opening file in either Read Mode or Create
printf("fd = %d/n", fd);
if (fd ==-1)
{
// print which type of error
printf("Error Number % d\n", errno);
// print program detail "Success or failure"
perror("Program"); //Prints the error in the program
}
return 0;
}