#include <stdio.h>

//int main(){
  //  printf("%20s  %13.2f\n", "Double", 1234567.8912);
//}
//
/*int main() {
   int integer = 10;
   float floating = 12.345;
   char character = 'A';
   char string[] = "Hello, World!";
   unsigned int unsignedInteger = 150;
   long longInteger = 1234567890L;
   double doubleNumber = 1234567.8912;
   void *pointer = (void *)string;
   int Fahr = 100;

   printf("%20s %15d\n","Integer:",  integer);
   printf("%20s %15u\n","Unsigned Integer:",  unsignedInteger);
   printf("%20s %15ld\n","Long Integer:" , longInteger);
   printf("%20s %15c\n","Character:", character);
   printf("%20s %15s\n","String:", string);
   printf("%20s %15.2f\n","Floating Point:", floating);
   printf("%20s %15.2lf\n","Double:", doubleNumber);
   printf("%20s %15p\n","Pointer:", pointer);
   printf("%20s %15e\n","Scientific Notation:", doubleNumber);
   printf("%20s %15x\n","Hexadecimal:", unsignedInteger);
   printf("%20s %15o\n","Octal:", unsignedInteger);

   printf("%20s %3d %11.3f\n","Temperature:", Fahr, (5.0/9.0)*(Fahr-32));

   return 0;
}*/
int main(){
    double doubleNumber = 1234567.8912;
    int Fahr = 78;
    
    printf("%20s %15e\n","Scientific:", doubleNumber);
    printf("%20s %2d %12.3f\n","Temperature:", Fahr, (5.0/9.0)*(Fahr-32));
}
