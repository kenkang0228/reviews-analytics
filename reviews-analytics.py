data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)	
		
print('讀取完成，總共有', len(data), '筆資料')

sum_len = 0
for x in data:
	sum_len = sum_len + len(x)

print('1.', data[0].strip()) #印出檔案中第1筆資料
print('2.', data[1].strip()) #印出檔案中第2筆資料
print('3.', data[2].strip()) #印出檔案中第3筆資料
print('4.', data[3].strip()) #印出檔案中第4筆資料
print('5.', data[4].strip()) #印出檔案中第5筆資料
print('6.', data[5].strip()) #印出檔案中第6筆資料
print('留言的平均長度為', sum_len/len(data), '個字元')

# 練習篩選留言長度
new = []
for d in data:
	if len(d) < 30:
		new.append(d)
print('一共有', len(new), '筆留言長度小於30')

#練習篩選某關鍵字在留言
word = []
for d in data:
	if 'if' in d:
		word.append(d)
print('共有', len(word), '筆留言提到if')
print(word[1])