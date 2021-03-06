#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import os
# 輸入檔案名稱
filename = "a1.txt"
filename01 = "a2.txt"

# 建立 MD5 物件
m = hashlib.md5()
n = hashlib.md5()

# 讀取檔案內容，計算 MD5 雜湊值
with open(filename, "rb") as f:
  buf = f.read()
with open(filename01, "rb") as g:
  buf1 = g.read()
# 更新 MD5 雜湊值
m.update(buf)
n.update(buf1)
# 取得 MD5 雜湊值
h = m.hexdigest()
i = n.hexdigest()
#比較雜湊結果是否相同
if h == i:
  print('第一個檔案的雜湊值為：'+h)
  print('第二個檔案的雜湊值為：'+i)
  print(h+'  等於  '+i)
  print('計算出的雜湊值經比較後是相同的，故檔案未被植入任何程式碼')
if h != i:
  class cmpFile:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def fileExists(self):
        if os.path.exists(self.file1) and os.path.exists(self.file2):
            return True
        else:
            return False

    # 對比文件不同之處, 並返回結果
    def compare(self):
        if cmpFile(self.file1, self.file2).fileExists():
            fp1 = open(self.file1)
            fp2 = open(self.file2)
            flist1 = [i for i in fp1]
            flist2 = [x for x in fp2]

        flines1 = len(flist1)
        flines2 = len(flist2)
        if flines1 < flines2:
            flist1[flines1:flines2+1] = ' ' * (flines2 - flines1)
        if flines2 < flines1:
            flist2[flines2:flines1+1] = ' ' * (flines1 - flines2)

        counter = 1
        cmpreses = []
        for x in zip(flist1, flist2):
            if x[0] == x[1]:
                counter +=1
                continue

            if x[0] != x[1]:
                cmpres = '%s和%s第%s行不同, 內容為: %s --> %s' % (self.file1, self.file2, counter, x[0].strip(), x[1].strip())
                cmpreses.append(cmpres)
                counter +=1
        return cmpreses

if __name__ == '__main__':
    cmpfile = cmpFile('a1.txt','a2.txt')
    difflines = cmpfile.compare()
    for i in difflines:
        print(i, end='\n')



