int main() {
    char  s[] = "Število znakov v besedi";
    int     i = 0;
    while (s[i] != '\0') i++;
    printf("Število znakov v besedi: %d\n", i);
    printf("Število znakov v besedi strlen: %d\n", strlen(s));
    printf("Število znakov v besedi sizeof: %d\n", sizeof(s));
}
