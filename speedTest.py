from sre_parse import State
import speedtest

st = speedtest.Speedtest()

def pythonSpeed():
    stillAlive = True

    while stillAlive == True:
        print("*" * 35)
        option = int(input('''What speed would you like to test?
        1) Download Speed
        2) Upload Speed
        3) Ping
        4) Quit
        \nYour Choice: '''))
        print("*" * 35)

        if option == 1:
            print("Download SpeedTest started, Please Wait...")
            speed = (st.download())   
            downloadSpeed = (speed / 1000000.00) 
            print("\nDownload Speed:")
            print(downloadSpeed," Mb/s")
        elif option == 2:
            print(st.upload())
        elif option == 3:
            servernames = []
            st.get_servers(servernames)
            print(st.results.ping)
        elif option == 4:
            print("Quitting SpeedTest")
            stillAlive = False
            return stillAlive
        else:
            print("Please enter a corrct choice!")

def main():
   pythonSpeed()
   print("\nProgram Has Exited. Self-Destruct Starting in 3...2..1\n")
main()