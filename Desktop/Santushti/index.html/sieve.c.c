#include<stdio.h>
#include<cmaths>
using namespace std;
int main();
{
    int n;

    scanf("%d",&n);

    bool a[n+1];

    a[0]=false;
    a[1]=false;

    for(int i=2;i<=n;i++)
    {
        if(i%2==0 && i!=2)
        a[i]=false

        else
        a[i]=true;
    }

    for(int i=0;i*i<=n;i++)
    {
        if(a[i]==true)
        {
            for(int j=i*2;j<=n;j+=i)
            a[i]=false;
        }
    }
    
    for(int i=0;i<=n;i++)
    {
        if(a[i]==true)
        printf("%d\n",i);
    }
    return 0;
}
