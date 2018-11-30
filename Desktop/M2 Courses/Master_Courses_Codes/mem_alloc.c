#include "mem_alloc.h"
#include <stdio.h>
#include <assert.h>
#include <string.h>

/* memory */
//#define MEMORY_SIZE 512
char memory[MEMORY_SIZE]; 

/* Structure declaration for a free block */
typedef struct free_block{
  int size; 
  struct free_block *next; 
} free_block_s, *free_block_t; 

/* Structure declaration for an occupied block */
typedef struct{
  int size; 
} busy_block_s, *busy_block_t; 


/* Pointer to the first free block in the memory */
free_block_t first_free; 


#define ULONG(x)((long unsigned int)(x))
#define max(x,y) (x>y?x:y)


void memory_init(void){
  
  first_free = (free_block_t)memory;
  first_free->size=MEMORY_SIZE;
  first_free->next= NULL;
  
}

char *memory_alloc(int size){
  
  ///* ... */
	free_block_t pointer = first_free;
	
	//First Fit Policy
	while (pointer == NULL || pointer->size < size + sizeof(busy_block_s)) {		
		pointer=pointer->next;
	}
	if(pointer == NULL){
		return NULL;
	}

	char *allocated_address = AllocateMemoryBlock((char*)pointer,size);
	

	//Worst Fit Policy
	//pointer = FindWorstFit(size);
	//AllocateMemoryBlock(pointer,size);

	//Best Fit Policy
	//pointer = FindBestFit(size);
	//AllocateMemoryBlock(pointer,size);
	
	
	print_alloc_info(allocated_address, size); 
  
	return allocated_address;

}

char *AllocateMemoryBlock(char * pointer,int size) {
	free_block_t fb = (free_block_t)(pointer + size + sizeof(busy_block_s));
	fb->size = ((free_block_t)pointer)->size - (size + sizeof(busy_block_s));//The size of new free block (after allocation) is equal to size of block which referred by "pointer" - reuquested size + size of descriptor
	fb->next = ((free_block_t)pointer)->next;//next block of new free block is the same as next of "pointer" block
	busy_block_t bb = (busy_block_t)pointer;
	bb->size = size + sizeof(busy_block_s);

	//Resetting next pointer of previous block 
	 ((free_block_t)pointer)->next = fb;
	
	return (char*)(bb + sizeof(busy_block_s));//Returns the address of allocated block

}

char *FindWorstFit(int size) {

 	free_block_t smallest_block;
 	free_block_t tmpblock = first_free;
 	int smallest_size = (smallest_block->size) - size;
	tmpblock=tmpblock->next;
	while (tmpblock!=NULL) {
		//if () {
			
		//}
	
	}

	return (char *)smallest_block;
}


char *FindBestFit(int size) {

 	free_block_t smallet_block=first_free;
 	free_block_t tmpblock = first_free;
	while (tmpblock!=NULL) {
		//if () {
			
		//}
	
	}
	
	return (char *)smallet_block;
}


void memory_free(char *busyblock){
  
	free_block_t current_pointer = first_free;
		
	while (current_pointer != NULL) {
		
		//if(current_pointer->next<=busyblock){// Checks left side blocks of busyblock for a freeblock
		
			//if ((current_pointer + current_pointer->size) == busyblock) {//There is no any busyblock between
			////if (current_pointer->next = busyblock + busybloc.size) {//This condition also can be used
			
				//current_pointer->size = current_pointer-> size + busyblock->size;
				
				////current_pointer->next=busyblock+busyblock->size;
			//}
			
			//else {//There is a block between in the left side of busyblock

				//free_block_s new_freeblock = busyblock + sizeof(busyblock->size);
				//new_freeblock->size=busyblock->size;
				//new_freeblock->next=current_pointer->next;
				//current_pointer->next=busyblock;
			//}
		//}
		//else { // Next freeblock is after the busy block 
			//if(current_pointer->next=(free_block_t)((char*)busyblock + busyblock.size) { //Next block of busyblock is a freeblock
				//busyblock->next=(free_block_t)((char*)busyblock + busyblock->size);
			//}
			//else { //There is a busyblock between
				//current_pointer->next=busyblock;
				//free_block_s new_freeblock = busyblock + sizeof(busyblock->size);
				//new_freeblock->size=busyblock->size;
				//new_freeblock->next=current_point->next;
			//}
		//}
		current_pointer = current_pointer->next;
	}
    
  print_free_info((char*)first_free); 
 
}


void print_info(void) {
  fprintf(stderr, "Memory : [%lu %lu] (%lu bytes)\n", (long unsigned int) 0, (long unsigned int) (memory+MEMORY_SIZE), (long unsigned int) (MEMORY_SIZE));
  fprintf(stderr, "Free block : %lu bytes; busy block : %lu bytes.\n", ULONG(sizeof(free_block_s)), ULONG(sizeof(busy_block_s))); 
}

void print_free_info(char *addr){
  if(addr)
    fprintf(stderr, "FREE  at : %lu \n", ULONG(addr - memory)); 
  else
    fprintf(stderr, "FREE  at : %lu \n", ULONG(0)); 
}

void print_alloc_info(char *addr, int size){
  if(addr){
    fprintf(stderr, "ALLOC at : %lu (%d byte(s))\n", 
	    ULONG(addr - memory), size);
  }
  else{
    fprintf(stderr, "Warning, system is out of memory\n"); 
  }
}

void print_free_blocks(void) {
  free_block_t current; 
  fprintf(stderr, "Begin of free block list :\n"); 
  for(current = first_free; current != NULL; current = current->next)
    fprintf(stderr, "Free block at address %lu, size %u\n", ULONG((char*)current - memory), current->size);
}

char *heap_base(void) {
  return memory;
}


void *malloc(size_t size){
  static int init_flag = 0; 
  if(!init_flag){
    init_flag = 1; 
    memory_init(); 
    print_info(); 
  }      
  return (void*)memory_alloc((size_t)size); 
}

void free(void *p){
  if (p == NULL) return;
  memory_free((char*)p); 
  print_free_blocks();
}

void *realloc(void *ptr, size_t size){
  if(ptr == NULL)
    return memory_alloc(size); 
  busy_block_t bb = ((busy_block_t)ptr) - 1; 
  printf("Reallocating %d bytes to %d\n", bb->size - (int)sizeof(busy_block_s), (int)size); 
  if(size <= bb->size - sizeof(busy_block_s))
    return ptr; 

  char *new = memory_alloc(size); 
  memcpy(new, (void*)(bb+1), bb->size - sizeof(busy_block_s) ); 
  memory_free((char*)(bb+1)); 
  return (void*)(new); 
}


#ifdef MAIN
int main(int argc, char **argv){

  /* The main can be changed, it is *not* involved in tests */
  memory_init();
  print_info(); 
  print_free_blocks();
  
  //int i;
  //for(i = 0; i < 10; i++) {
    //char *b = memory_alloc(rand()%8);
    //memory_free(b); 

    //print_free_blocks();
  //}




  char * a = memory_alloc(15);
  a=realloc(a, 20); 
  memory_free(a);


  a = memory_alloc(10);
  //memory_free(a);

  printf("%lu\n",(long unsigned int) (memory_alloc(9)));
  
  print_info();

  return EXIT_SUCCESS;
}
#endif 
