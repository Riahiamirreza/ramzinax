#include <stdio.h>

void str2bit(char *msg, char *file_name){
	
   	FILE *fp;
	fp = fopen(file_name,"w");	
	char *ptr = msg;
	for(; *ptr != 0; ++ptr){
		//printf("%c => ", *ptr);

		for(int i =7;i >= 0; --i){
			//(*ptr & 1 << i) ? putchar('1') : putchar('0');
			(*ptr & 1 << i) ? fprintf(fp,"1",1) : fprintf(fp,"0",1);
		}
		//putchar('\n');
	}

}

void chr2bit(char ch){

	//char *ptr = ch;
	for(int i=7; i>=0; --i){	
		(ch & 1 << i) ? putchar('1') : putchar('0');
	}
		
}


int main(int argc, char *argv[]){
	
	str2bit(argv[1],"msg.txt");
	//chr2bit();
	return 0;
}
