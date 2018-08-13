#include <stdio.h>
#include <string.h>
    char * s1;
    char * s2;
    char * s22;
    char * x;
    int lens1;
    int lens2;
int main(){
    scanf("%s", &s1);
    scanf("%s", &s2);
    s22 = s2;
    strcat(s22,s22);
    lens1 = strlen(s1);
    lens2 = strlen(s22);
    if(lens2 == (2*lens1)){
        x = strstr(s22,s1);
        if( x == s1){
            printf("%s é rotação de %s ", s2,s1);
            return 0;
        }
        else{
            printf("%s não é rotação de %s ", s2,s1);
            return 0;
        }
    }
    else{
        printf("%s não é rotação de %s ", s2,s1);
        return 0;
    }
}
