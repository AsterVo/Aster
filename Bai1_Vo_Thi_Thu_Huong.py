import random
def Bai1_CauA ():
    while True:
        try:
            n = int(input('Nhập số nguyên dương: '))
        except Exception:
            print ('Phải nhập số nguyên dương. Yêu cầu nhập lại.')
        else:
            if n < 10 or n > 1000:
                print('Chỉ nhận giá trị từ 10 đến 1000. Yêu cầu nhập lại.')
            else:
                return n
def Bai1_CauB (n):
    mylist = []
    for i in range(n):
        mylist.append(random.randint(0, 5000))
        return mylist
#Chương trình chính:
n = Bai1_CauA()
mylist = Bai1_CauB(n)
print ('List vừa tạo: ', mylist)