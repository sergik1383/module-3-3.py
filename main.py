def prints_params (a,b,c) :
    print(a,b,c)
list_= [1,'строка',True]
prints_params(*list_)

values_list = [1,'a',True]
prints_params(*values_list)
values_dict = {'a':1,'b':'a','c':True}
prints_params(**values_dict)
values_list2 = [54.32,'Строка']
prints_params(*values_list2,42)
