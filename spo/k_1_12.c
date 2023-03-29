int main() {
    struct {
        char e;    // 1 bajt
        int a;     // 4 bajti
        char b;    // 1 bajt
        double c;  // 8 bajtov
    } x;
    printf("Velikost strukture: %d\n", sizeof(x));
}
