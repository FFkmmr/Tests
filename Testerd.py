import speedtest

def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
st = speedtest.Speedtest() 
option = int(input('''
Выбери тип проверки:   

1 - Скорость скачивания   
2 - Скорость загрузки   

Твой выбор: ''')) 
if option == 1:   
    print(humansize(st.download()/8) )  
elif option == 2:  
    print(humansize(st.upload()/8))
# elif option == 3:   
#     servernames =[]   
#     st.get_servers(servernames)
#     print(st.results.ping)     
else:  
    print("Пожалуйста, введите цифру от 1 до 2!")

#Readable
#1print(humansize(ds))