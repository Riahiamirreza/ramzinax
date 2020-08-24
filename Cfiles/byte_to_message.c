#include <stdio.h>
#include <stdlib.h>

void bit2str(char *file_name){

	FILE *fp;
	fp = fopen(file_name, "r");
	char byte[8],bit;
	int counter = 0;

	while((bit = fgetc(fp)) != EOF){
		byte[counter] = bit;
	        counter ++;	
		if(counter == 8){
			char c = strtol(byte,0,2);
			printf("%c",c);
			counter = 0;
		}

	}
	printf("\n");
}

int main(){

	bit2str("msg.txt");
	return 0;
}
