'''
問題文
	数列 a1,a2,...,an が以下の条件を満たすとき、 /\/\/\/ と呼ぶことにします。
	・各 i=1,2,..,n−2 について、ai=ai+2
	・数列に現れる数はちょうど 2 種類
	偶数長の数列 v1,v2,...,vn が与えられます。 
	要素をいくつか書き換えることでこの数列を /\/\/\/ にしたいです。 書き換える要素の数は最小でいくつになるか求めてください。

制約
2 ≤ n ≤ 10^5
n は偶数
1 ≤ vi ≤ 10^5
vi は整数

入力
入力は以下の形式で標準入力から与えられる。
n
v1 v2 ... vn

出力
書き換える要素数の最小値を出力してください。

入力例 1 
4
3 1 3 2
出力例 1 
1
数列 
3,1,3,2 は /\/\/\/ ではありませんが、
1 要素書き換えることで /\/\/\/ にすることができます。 例えば、4 要素目を書き換えて 3,1,3,1 とすればよいです。

入力例 2 
6
105 119 105 119 105 119
出力例 2 
0
数列 
105,119,105,119,105,119 は /\/\/\/ です。

入力例 3 
4
1 1 1 1
出力例 3 
Copy
2
数列 
1,1,1,1 は 1 種類の数からなる数列であるため、 /\/\/\/ ではありません。
'''

import collections

def calcChange(even_list, odd_list) :
	"""
	/\/\/\/にするために変更する要素数を算出

	Parameters
	----------
	even_list : list
			偶数番目の要素のリスト
	odd_list : list
			奇数番目の要素のリスト
	
	Returns
	-------
	change : int
			/\/\/\/にするために変更する要素数
			
	"""	

# 1:60   1:60
# 2:50   2:60
# 3:30   3:20
 
 
	# 変更回数を代入する変数
	change = 0

	# 各リストについて、要素名:要素数 の辞書を、Counterで作成
	even_counter = collections.Counter(even_list)
	odd_counter = collections.Counter(odd_list)
	
	# 最多要素を取得
	most_even = even_counter.most_common()
	most_odd = odd_counter.most_common()

	# 最多要素が被っていない
	if most_even[0][0] != most_odd[0][0] :
		even_change = len(even_list) - most_even[0][1]
		odd_change  = len(odd_list)  - most_odd[0][1]
		change = even_change + odd_change
	# 被ってる
	else :
		if len(most_even)==1 and len(most_odd)==1 :# 全かぶり
			change = len(even_list)
		else : # even と odd のどちらの最多要素を残すかを、それぞれの場合で比較して少ない方を採用する。
			even_1 = (len(even_list) - most_even[0][1]) + (len(odd_list)  - most_odd[1][1])
			odd_1  = (len(even_list) - most_even[1][1]) + (len(odd_list)  - most_odd[0][1])
			change = min(even_1, odd_1)


	return change



def main():
	'''
	メイン関数
	'''
	# 数列の大きさ
	n = int(input())
	# 数列
	v = list(map(int, input().split()))

	# 偶数番目を抽出した配列
	v_e = [ v[i] for i in range(0,n) if i%2==0 ]

	# 奇数番目を抽出した配列
	v_o = [ v[i] for i in range(0,n) if i%2==1 ]

	print(calcChange(v_e, v_o))


if __name__ == '__main__':
	main()


