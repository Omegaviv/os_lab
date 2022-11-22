#include<stdio.h>
#include <fcntl.h>
int main()
{
int fd1 = open("foo.txt", O_RDONLY);
if (fd1 < 0) //Printing the error in the file
{
perror("Program");
exit(1);
}
printf("opened the fd = % d\n", fd1);
// Using close system Call
if (close(fd1) < 0)  //closed(fd1) - Closes the file
{
perror("Error"); //If not closed- print the error.
exit(1);
}
printf("closed the fd.\n");
}