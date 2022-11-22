#include <fcntl.h>
int main()
{
int fd, sz;
char *c = (char *) calloc(100, sizeof(char)); //Character Array of size 100 * Size of character
fd = open("foo.txt", O_RDONLY); 
if (fd < 0) 
{ 
    perror("r1"); 
    exit(1); 
} //error in file opening
sz = read(fd, c, 10); //reads the file- attributes are fd, c, number of characters to be read
printf("called read(% d, c, 10). returned that"
" %d bytes were read.\n", fd, sz);
c[sz] = '\0';
printf("Those bytes are as follows: % s\n", c); //Displaying the read information
}