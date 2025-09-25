from threading import Thread

def work(id,start,end,result):
  total=0
  for i in range(start,end):
    total += 1
  result.append(total)
  return

if __name__ =="__main__":
  START,END=0,100000000
  result=list()
  th1=Thread(target=work,atgs=(1,START,END//2,result))
  th2=Thread(target=work,args=(2,END,END,result))

  th1.start
  th2.start


