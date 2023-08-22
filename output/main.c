#include <stdio.h>
#include <string.h>

int main()
{
  char *str = "Hello World";
  char *word = "World";


  char first = word[0];
  char *result = NULL;

  while(result = strrchr(str, first)) != NULL) {
    if (strncmp(result, word, strlen(word)) == 0) {
      printf("Found %s\n", word);
      break;
    }
    str = result;
  }

  return 0;
}