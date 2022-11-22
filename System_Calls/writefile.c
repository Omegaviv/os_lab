// write system Call
#include<stdio.h>
#include <fcntl.h>
main()
{
int sz;
int fd = open("foo.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
if (fd < 0)
{
perror("r1");
exit(1);
}
sz = write(fd, "Today is a good Day!\n", strlen("Today is a good Day!\n"));
close(fd);
}




