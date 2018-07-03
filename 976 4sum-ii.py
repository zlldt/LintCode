class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        # Write your code here
        count=0
        A.sort()
        B.sort()
        C.sort()
        dicta={}
        dictb={}
        dictc={}
        dictd={}
        dictab={}
        dictcd={}
        for a in A:
            if a not in dicta:
                dicta[a]=1
            else:
                dicta[a]+=1
        for b in B:
            if b not in dictb:
                dictb[b]=1
            else:
                dictb[b]+=1
        for c in C:
            if c not in dictc:
                dictc[c]=1
            else:
                dictc[c]+=1
        for d in D:
            if d not in dictd:
                dictd[d]=1
            else:
                dictd[d]+=1
        # for a in A:
        #     for b in B:
        #         for c in C:
        #             if -a-b-c in D:
        #                 count+=D.count(-a-b-c)
        for keya,counta in dicta.items():
            for keyb,countb in dictb.items():
                if keya+keyb not in dictab:
                    dictab[keya+keyb]=counta*countb
                else:
                    dictab[keya+keyb]+=counta*countb
        for keyc,countc in dictc.items():
            for keyd,countd in dictd.items():
                if -keyc-keyd in dictab:
                    count +=countc*countd*dictab[-keyc-keyd]
        # print(count)
        return count
