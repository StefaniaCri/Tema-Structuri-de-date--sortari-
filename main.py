import random
import time
import numpy as np

def cifre(n) :
    nr=0
    while n>0:
        nr+=1
        n//=10
    return nr
def BubbleSort(t):
    n = len(t)
    for i in range(n):
        ok = False
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                ok = True
        if ok == False:
            break

def CountSort(t):
    minim=min(t)
    maxim=max(t)
    frecv=[0]*(maxim-minim+1)
    for elem in t:
        frecv[elem-minim]+=1
    k=0
    for i in range(minim,maxim+1):
        for j in range(0,frecv[i-minim]):
            t[k]=i
            k+=1

def Radixsort( t ):
    base = 256      #1 0000 0000
    shift = 0       #0000 0000
    mask = ( 1 << 8 ) - 1  #1111 1111
    maxi = max(t)
    co = 0
    while maxi > 0:
        maxi >>= 8
        co += 1
    for i in range( co ):
        bucket = [] *base
        for j in range( base ):
            bucket.append( [] )
        for j in t:
            nr = ( j >> shift ) & mask
            bucket[nr].append(j)
        t = []
        for j in range(base):
            t.extend( bucket[j] )
        shift += 8

def interclasare(t, st, mij, dr):
    i = st
    j = mij+1
    aux = []
    while i <= mij and j <= dr:
        if t[i] <= t[j]:
            aux.append(t[i])
            i += 1
        else:
            aux.append(t[j])
            j += 1
    aux.extend(t[i:mij+1])
    aux.extend(t[j:dr+1])
    t[st:dr+1] = aux[:]
def mergesort(t, st, dr):
    if st < dr:
        mij = (dr+st) // 2
        mergesort(t, st, mij)
        mergesort(t, mij+1, dr)
        interclasare(t, st, mij, dr)
def test(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return 0
    return 1

def partition(t, start, stop):
    pivot = start
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if t[i] >= t[pivot]:
                break
        while True:
            j = j - 1
            if t[j] <= t[pivot]:
                break
        if i >= j:
            return j
        t[i], t[j] = t[j], t[i]
def partitionrand(t, start, stop):
    randpivot = random.randrange(start, stop)
    t[start], t[randpivot] = t[randpivot], t[start]
    return partition(t, start, stop)
def quicksortrrand(t, start, stop):
    if (start < stop):
        pivotindex = partitionrand(t, start, stop)
        quicksortrrand(t, start, pivotindex)
        quicksortrrand(t, pivotindex + 1, stop)
def quicksortmed(t, start, stop):
    if (start < stop):
        pivotindex = median(t, start, stop)
        quicksortmed(t, start, pivotindex)
        quicksortmed(t, pivotindex + 1, stop)
def quicksortstart(t,start,stop):
    if (start < stop):
        pivotindex = partition(t, start, stop)
        quicksortstart(t, start, pivotindex)
        quicksortstart(t, pivotindex + 1, stop)
def median(t,start,stop):
    mij=(start+stop)//2
    if t[mij]<t[start]:
        t[start],t[mij]=t[mij],t[start]
    if t[stop]<t[start]:
        t[start],t[stop]=t[stop],t[start]
    if t[mij]<t[stop]:
        t[mij],t[stop]=t[stop],t[mij]
    t[start], t[stop] = t[stop], t[start]
    return partition(t,start,stop)

g=open("Timpi",'w')
f=open("teste")
numar_teste=int(f.readline())
for i in range(numar_teste):
    n, maxim=f.readline().split()
    n=int(n)
    maxim=int(maxim)
    g.write("N={}    Maxim={}\n".format(n,maxim))
    print(i,". Generam o lista random. Doriti sa generam o lista speciala?")
    ras=int(input("1/0="))
    if ras:
        print("Ce fel de lista: 1-cu un singur element;2-sortata crescator;3-sortata descrescator; 4-sortata patial crescator; 5-sotata partial descrescator")
        ras1=int(input("1/2/3/4/5:"))
        if ras1==1:
            x=random.randint(0,maxim)
            a=[x for i in range(n)]
            g.write("Un singur element\n")
        elif ras1==2:
            a = [random.randrange(0, maxim, 1) for i in range(n)]
            a.sort(reverse=False)
            g.write("Gata sorta\n")
        elif ras1==3:
            a = [random.randrange(0, maxim, 1) for i in range(n)]
            a.sort(reverse=True)
            g.write("Gata sortata descrescator\n")
        elif ras1==4:
            a = [random.randrange(0, maxim, 1) for i in range(n)]
            lis = [random.randrange(0,n) for i in range(4)]
            a=np.partition(a,lis)
            g.write("Partial sortata\n")
        elif ras1==5:
            a = [random.randrange(0, maxim, 1) for i in range(n)]
            lis = [random.randrange(0, n) for i in range(4)]
            a = np.partition(a, lis)
            a=a[::-1]
            g.write("Patial sortata descrescator\n")
        else:
            print("Nu avem aceasta comanda, generam o lista random")
            a = [random.randrange(0, maxim, 1) for i in range(n)]
    else:
        a=[random.randrange(0,maxim,1) for i in range(n)]
    asort_radix=a
    asort_quick=a
    asort_merge=a
    asort_bubble=a
    asort_count=a
    asort_corect=a
    asort_start=a
    raspuns=0

    if n>=10**5:
        print("Sarim peste Bubble. Sunteti de acord? 1/0")
        g.write("Am sarit peste Bubble\n")
        raspuns=int(input("1/0:"))
    if raspuns==0:
        start=time.time()
        BubbleSort(asort_bubble)
        end=time.time()
        timp=end-start
        g.write("A sortat {} (10^{}) elemente in {} secunde cu BubbleSort() \n".format(n,cifre(n)-1,timp))
        if (test(asort_bubble)):
            g.write("CORECT\n")
        else:
            g.write("Incorect\n")


    start=time.time()
    asort_corect.sort()
    end=time.time()
    timp=end-start
    g.write("A sortat {} (10^{}) elemente in {} secunde cu Sort()\n ".format(n,cifre(n)-1,timp))
    start=time.time()
    Radixsort(asort_radix)
    end=time.time()
    timp=end-start
    g.write("A sortat {} (10^{}) elemente in {} secunde cu RadixSort()\n".format(n,cifre(n)-1,timp))
    if (test(asort_radix)):
        g.write("CORECT\n")
    else:
        g.write("Incorect\n")


    start=time.time()
    CountSort(asort_count)
    end=time.time()
    timp=end-start
    g.write("A sortat {} (10^{}) elemente in {} secunde cu CountSort()\n ".format(n,cifre(n)-1,timp))
    if (test(asort_count)):
        g.write("CORECT\n")
    else:
        g.write("Incorect\n")


    start=time.time()
    mergesort(asort_merge,0,len(asort_merge)-1)
    end=time.time()
    timp=end-start
    g.write("A sortat {} (10^{}) elemente in {} secunde cu MergeSort() ".format(n,cifre(n)-1,timp))
    g.write('\n')
    if test(asort_merge):
        g.write("CORECT\n")
    else:
        g.write("Incorect\n")

    print("Cum sa alegem pivotul: mediana de 3=1/primul elem=2/la intamplare=3")
    ans=int(input("1/2/3:"))

    if ans==1:
        start=time.time()
        quicksortmed(asort_quick,0,len(asort_quick)-1)
        end=time.time()
        timp=end-start
        g.write("A sortat {} (10^{}) elemente in {} secunde cu QuickSort() pivotul ales ca mediana de 3\n".format(n,cifre(n)-1,timp))
        if (test(asort_quick)):
            g.write("CORECT\n")
        else:
            g.write("Incorect\n")

    if ans==2:
        start=time.time()
        quicksortstart(asort_start,0,len(asort_start)-1)
        end=time.time()
        timp=end-start
        g.write("A sortat {} (10^{}) elemente in {} secunde cu QuickSort() pivotul ales ca primul element \n".format(n,cifre(n)-1,timp))
        if (test(asort_start)):
            g.write("CORECT\n")
        else:
            g.write("Incorect\n")

    if ans==3:
        start = time.time()
        quicksortrrand(asort_start, 0, len(asort_start) - 1)
        end = time.time()
        timp = end - start
        g.write("A sortat {} (10^{}) elemente in {} secunde cu QuickSort() pivotul ales la intamplare \n".format(n, cifre(n) - 1, timp))
        if (test(asort_start)):
            g.write("CORECT\n")
        else:
            g.write("Incorect\n")
    g.write("---------\n\n\n")
f.close()
