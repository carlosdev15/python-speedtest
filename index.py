import speedtest

st = speedtest.Speedtest()
print("Velocidade Download: ",st.download()//10**6, "Mbps")
print("Velocidade Upload ",st.upload()//10**6, "Mbps")
print("Ping: ", int(st.results.ping), "MS")