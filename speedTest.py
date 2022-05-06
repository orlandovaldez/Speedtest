import speedtest

st = speedtest.Speedtest()

option = int(input('''What speed would you like to test?
1) Download Speed
2) Upload Speed
3) Ping
\nYour Choice: '''))

if option == 1:
    print(st.download(), "Mb/s")    
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.Ping)
else:
    print("Please enter a corrct choice!")