
print("嘿女孩們～")
print("請默想妳心裡的任意多個幸運數字")

number= list(map(int, input('輸入妳心裏的數字, 然後記得用分號區隔開喔：').split(',')))

print ("這是你今天的總體能量：",end=str(sum(number)))

print ("後面這是你的幸運大數：",end=str(max(number)))