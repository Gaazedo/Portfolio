#include <stdio.h>

main() {
    int i,v[99];
    for (i = 0; i<99; ++i) v[i] = 98 - i;
    for (i = 0; i<99; ++i) {
        v[i] = v[v[i]];
        printf("%d",v[i]);
    };
}