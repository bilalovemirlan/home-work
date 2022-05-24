John = [["fizika", 32],["russki", 43],["istoriya", 54],["biologiya", 78],["himiya", 44],["algebra", 20],["astronomia", 78]]
Jack = [["fizika", 56],["russki", 87],["istoriya", 23],["biologiya", 45],["himiya", 76],["algebra", 10],["astronomia", 16]]
Tomas = [["fizika", 45],["russki", 33],["istoriya", 50],["biologiya", 78],["himiya", 87],["algebra", 20],["astronomia", 76]]
total_st={}
def dict_st(a):
    st1 = {}
    for i in a:
        st1.update({i[0]:i[1]})
    return st1
def aver_sc(a):
    s=0
    for i in a:
        x=int(a.get(i))
        s+=x
    return int(s/7)
print('John: ', dict_st(John))
print('средний балл : ')
print('John: ', aver_sc(dict_st(John)),'балл')
total_st.update({"John": aver_sc(dict_st(John))})
print()
print('Jack:' , dict_st(Jack))
print('средний балл : ')
print('Jack: ', aver_sc(dict_st(Jack)),'балл')
total_st.update({"Jack": aver_sc(dict_st(Jack))})
print()
print('Tomas :',  dict_st(Tomas))
print('средний балл : ')
print('Tomas: ', aver_sc(dict_st(Tomas)),'балл')
total_st.update({"Tomas": aver_sc(dict_st(Tomas))})
print()

print (total_st)
max_Score = max( zip(total_st.values(),total_st.keys()) )
print('Лучшим студентом является: ', max_Score)