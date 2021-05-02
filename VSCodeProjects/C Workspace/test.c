#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void alloc_string(int size, char** out);

int main (int argc, char* argv[])
{
  
  printf ("Hello, world!\n");

  char* my_ptr = NULL;
  alloc_string(5, &my_ptr);
  const char* my_name = "Alain";
  const char* my_friend = "Alain";

  printf("the compare result is : %s\n", !strcmp(my_name,my_friend) ? "true" : "false");


  return 0;
}

void alloc_string(int size, char** out)
{
  *out = malloc(sizeof(char) * size + 1);
}