#include<stdio.h>
int main(){
 char str[]="Hello World";
 int i=0, count=0;
 while(str[i]){
 char c=str[i];
 if((c>='a'&&c<='z')||(c>='A'&&c<='Z')){

if(c!='a'&&c!='e'&&c!='i'&&c!='o'&&c!='u'&&

c!='A'&&c!='E'&&c!='I'&&c!='O'&&c!='U')
 count++;
 }
 i++;
 }
 printf("Consonants = %d\n", count);
 return 0;
}
