driving = input('請問你有開過車嗎?')
if driving!= '有' and driving!='沒有' :
	print('只能輸入有/沒有')
	raise SystemExit  #這個是讓系統終止

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18 :
		print('你通過測試了')
	else :
		print('奇怪囉，你怎麼可以開車')
elif driving == '沒有':
	if age >= 18 :
		print('可以去考駕照囉')
	else :
		print('再過幾年就可以考囉')