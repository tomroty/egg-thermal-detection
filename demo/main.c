#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ROW 24
#define COL 32

char** getArrayFromFile(char *file)
{
    FILE *f = fopen(file, "r");
    if (f == NULL)
    {
        printf("Incorrect path:\n'%s'\n", file);
        return NULL;
    }
    char** array = calloc(ROW, sizeof(char*));
    for (int i=0; i<ROW; i++)
    {
        array[i] = calloc(ROW, sizeof(char));
    }

    for (int i=0; i<ROW; i++)
    {
        for (int j=0; j<COL; j++) {
            char chartmp;
            fscanf(f, "%c", &chartmp);
            array[i][j] = chartmp;
        }
        fscanf(f, "\n");
    }
    return array;
}
void printArray(char **array)
{
    for (int i=0; i<ROW; i++)
    {
        for (int j=0; j<COL; j++)
        {
            if (array[i][j] == '*') printf(". ", array[i][j]);
            else
            printf("%c ", array[i][j]);
        }
        printf("\n");
    }
}

void printBlacklist(bool **blacklist)
{
    for (int i=0; i<ROW; i++)
    {
        for (int j=0; j<COL; j++)
        {
            if (blacklist[i][j] == true) printf("X ");
            else printf(". ");
        }
        printf("\n");
    }
}


bool isToBlacklist(char **array, bool **blacklist, int i, int j)
{
    if (array[i][j] == 'X' && blacklist[i][j] == false)
    {
        return true;
    }
    return false;
}

void blacklistRec(char **array, bool **blacklist, int i, int j)
{
    blacklist[i][j] = true;

    bool top=true, bottom=true, left=true, right=true;

    if (i==0) top = false;
    if (i==ROW-1) bottom = false;
    if (j==0) left = false;
    if (j==COL-1) right = false;

    if (top)
    {
        if (isToBlacklist(array, blacklist, i-1, j)) blacklistRec(array, blacklist, i-1, j);
        if (left && isToBlacklist(array, blacklist, i-1, j-1)) blacklistRec(array, blacklist, i-1, j-1);
        if (right && isToBlacklist(array, blacklist, i-1, j+1)) blacklistRec(array, blacklist, i-1, j+1);
    }
    if (bottom)
    {
        if (isToBlacklist(array, blacklist, i+1, j)) blacklistRec(array, blacklist, i+1, j);
        if (left && isToBlacklist(array, blacklist, i+1, j-1)) blacklistRec(array, blacklist, i+1, j-1);
        if (right && isToBlacklist(array, blacklist, i+1, j+1)) blacklistRec(array, blacklist, i+1, j+1);
    }
    if (left)
    {
        if (isToBlacklist(array, blacklist, i, j-1)) blacklistRec(array, blacklist, i, j-1);
    }
    if (right)
    {
        if (isToBlacklist(array, blacklist, i, j+1)) blacklistRec(array, blacklist, i, j+1);
    }
}

int eggCount(char** array)
{

    int eggcount = 0;
    bool** blacklist = calloc(ROW, sizeof(bool*));
    for (int i=0; i<ROW; i++)
    {
        blacklist[i] = calloc(COL, sizeof(bool));
    }

    for (int i=0; i<ROW; i++)
    {
        for (int j=0; j<COL; j++)
        {
            if (array[i][j] == 'X' && blacklist[i][j] == false)
            {
                eggcount++;
                blacklistRec(array, blacklist, i, j);
            }
        }
    }


    for(int i=0; i<ROW; i++)
    {
        free(blacklist[i]);
    }
    free(blacklist);
    return eggcount;
}

int main(int argc, char *argv[])
{
    char *path = argv[1];
    if (path == NULL)
    {
        printf("No path provided\n");
        return 1;
    }

    char **array = getArrayFromFile(path);
    int eggcount = eggCount(array);
    printf("%d\n", eggcount);
    free(array);
    return eggcount;
}
