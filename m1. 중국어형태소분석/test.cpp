// win_cDemo.cpp : 定义控制台应用程序的入口点。
#include "../include/NLPIR.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifndef OS_LINUX
//#pragma comment(lib, "../../bin/NLPIR.lib")
#endif

//Linux
#ifdef OS_LINUX
#define _stricmp(X,Y) strcasecmp((X),(Y))
#define _strnicmp(X,Y,Z) strncasecmp((X),(Y),(Z))
#define strnicmp(X,Y,Z)	strncasecmp((X),(Y),(Z))
#define _fstat(X,Y)     fstat((X),(Y))
#define _fileno(X)     fileno((X))
#define _stat           stat
#define _getcwd         getcwd
#define _off_t          off_t
#define PATH_DELEMETER  "/"
#else
#pragma warning(disable:4786)
#define PATH_DELEMETER  "\\"
#endif

void SplitBIG()
{
	//初始化分词组件
	if (!ICTCLAS_Init("..", 0))//对文件进行词性标注 "E:\vsprojects\NLPIR"
	{
		printf("ICTCLAS INIT FAILED!\n");
		return;
	}
	printf("start");

	int i ;
	char s[5];
	char filein[30], fileout[30];
	for (i = 1; i <= 800; i++)
	{
		strcpy(filein, "../books_gbk/");
		strcpy(fileout, "../books_result/");

		_itoa(i, s, 10);

		strcat(filein, s);
		strcat(fileout, s);

		strcat(filein, ".txt");
		strcat(fileout, ".txt");

		ICTCLAS_FileProcess(filein, fileout);
		printf("%s %s\n", filein,fileout);
	}

	ICTCLAS_Exit();
}
int main()
{
	SplitBIG();
	return 1;
}