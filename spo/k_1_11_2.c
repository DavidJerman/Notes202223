struct A1 {
    char a;
    long b;
    short c;
};

struct A2 {
    char a;
    short c;
    long b;
};

int main() {
    printf("sizeof(struct A1) = %d\n", sizeof(struct A1));
    printf("sizeof(struct A2) = %d\n", sizeof(struct A2));
}
