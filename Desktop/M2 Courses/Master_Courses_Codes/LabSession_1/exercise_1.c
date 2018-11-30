#include <stdio.h>
#include <limits.h>
#include <malloc.h>

void fonc(unsigned int nb, int *tab) {
     int *dst;
     int i;
     printf("nb : %u \n", nb);
     printf("size : %u \n", sizeof(unsigned int)*nb);
     dst = (int *) malloc(sizeof(unsigned int)*nb);
     if (!dst) { printf("Stop  \n") ; return ;}
     for (i=0; i <nb; i++)
          { dst[i]=tab[i] ;} }

void main ()

{	int *tab;
        unsigned int nb ;
        unsigned  int TwoExp30 = 1073741824;
        printf(" size of an  unsigned int %u \n", sizeof(unsigned int));
        printf(" Call OK \n");
        tab = (int *)malloc(sizeof(unsigned int)*2E8);
        fonc(4, tab);
        printf(" Call KO \n");
        fonc((unsigned int)TwoExp30, tab);
}

