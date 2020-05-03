import multiprocessing  
  
def func(mydict,mylist,i):  
    # mydict["index1"]=str(i)   
    # mylist.append(11)  
    # mylist.append(22)  
    # mylist.append(33)

    print('mydict' + str(i), mydict)
    print('mylist' + str(i), mylist)
  
if __name__=="__main__":  
    with multiprocessing.Manager() as MG:   #重命名  
        mydict=multiprocessing.Manager().dict()   #主进程与子进程共享这个字典  
        mylist=multiprocessing.Manager().list()   #主进程与子进程共享这个List  
  
        process_list = []
        pool = multiprocessing.Pool(10)
        for i in range(10):
            # p=multiprocessing.Process(target=func,args=(mydict,mylist,i))
            process_list.append(i)

        for one in process_list:
            pool.apply_async(func, args=(mydict, mylist, one))