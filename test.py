#!/usr/bin/python2
# -*- coding:UTF-8 -*-
# code related at: http://blog.mckelv.in/articles/1453.html
 
import sys
 
distance = lambda a,b : 0 if a==b else 1
 
def dtw(sa,sb):
    '''
    >>>dtw(u"�������������������������úúúð�����", u"���������úð�")
    2
    '''
    MAX_COST = 1<<32
    #��ʼ��һ��len(sb) ��(i)��len(sa)��(j)�Ķ�ά����
    len_sa = len(sa)
    len_sb = len(sb)
    # BUG:�����Ǵ����(ǳ����): dtw_array = [[MAX_COST]*len(sa)]*len(sb)
    dtw_array = [[MAX_COST for i in range(len_sa)] for j in range(len_sb)]
    dtw_array[0][0] = distance(sa[0],sb[0])
    for i in xrange(0, len_sb):
        for j in xrange(0, len_sa):
            if i+j==0:
                continue
            nb = []
            if i > 0: nb.append(dtw_array[i-1][j])
            if j > 0: nb.append(dtw_array[i][j-1])
            if i > 0 and j > 0: nb.append(dtw_array[i-1][j-1])
            min_route = min(nb)
            cost = distance(sa[j],sb[i])
            dtw_array[i][j] = cost + min_route
    return dtw_array[len_sb-1][len_sa-1]
 
 
def main(argv):
#    s1 = u'�������������������������úúúð�����'
#	s1 = u'\u5e72\u5566\u4eca\u4eca\u4eca\u4eca\u4eca\u5929\u5929\u6c14\u6c14\u6c14\u6c14\u6c14\u597d\u597d\u597d\u597d\u554a\u554a\u554a'
#    s2 = u'���������úð�'
#	s2 =  u'\u4eca\u5929\u5929\u6c14\u597d\u597d\u554a'
	s1 = u'\u4f60\u597d'
	s2 =  u'\u4f60~~~~~~\u597d'

	d = dtw(s1, s2)
	print d
	return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
	print("done")

