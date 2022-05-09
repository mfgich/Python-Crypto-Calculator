import tkinter as tk
import tkinter.font as font
import requests
import json
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt
root = tk.Tk()
v = tk.StringVar()
c = tk.StringVar()

root.geometry("1150x1000")
root.title("Calculator")
myFont = font.Font(family="Helvetica", slant="italic",
                   size=13, underline=1, weight="bold")
currencys = ["BTC", "ETH", "XRP", "ADA", "BNB",
             "SOL", "DOGE", "DOT", "SHIB", "BCH", "UNI1", ]
namen = ["bitcoin", "ethereum", "ripple", "litecoin", "dash", "monero", "cardano", "uniswap", "chainlink",
         "stellar", "dai", "iota", "zcash"]
currencysVar = tk.StringVar(value=currencys)
namenVar = tk.StringVar(value=namen)
label1 = tk.Label(root, text="", background="white",
                  foreground="red", width=60, height=2, relief=tk.SUNKEN, font=myFont)
label2 = tk.Label(root, text="", background="lightgreen",
                  foreground="black", width=60, height=2, font=myFont)
label3 = tk.Label(root, text="", background="lightblue",
                  foreground="black", width=60, height=2, font=myFont)
label4 = tk.Label(root, text="", background="salmon",
                  foreground="black", width=60, height=2, font=myFont)
label5 = tk.Label(root, text="", background="snow",
                  foreground="black", width=60, height=2, font=myFont)
label6 = tk.Label(root, text="", background="snow",
                  foreground="black", width=60, height=2, font=myFont)
label7 = tk.Label(root, text="Krypto ID eingeben ", background="snow",
                  foreground="black", width=20, height=2, font=myFont)
entryl = tk.Entry(root, textvariable=v, background="snow",
                  foreground="black", font=myFont)
listbox1 = tk.Listbox(root, listvariable=currencysVar, height=6, font=myFont)
listbox2 = tk.Listbox(root, listvariable=namenVar, height=6, font=myFont)
label1.grid(column=2, row=5, columnspan=3)
label2.grid(column=2, row=6, columnspan=3)
label3.grid(column=2, row=7, columnspan=3)
label4.grid(column=2, row=8, columnspan=3)
label5.grid(column=2, row=9, columnspan=3)
label6.grid(column=2, row=10, columnspan=3)
label7.grid(column=2, row=12)
entryl.grid(column=3, row=12, ipadx=20, ipady=10)
listbox1.grid(column=7, row=11)
listbox2.grid(column=7, row=12)

Ergebnis = ""
Formel = ""


def Rechnung():
    Formel = label1.cget("text")
    global Ergebnis
    Ergebnis = eval(Formel)
    label2["text"] = str(Ergebnis)
    print(type(Ergebnis))


def Binaer():
    ergBin = bin(int(Ergebnis))
    label3["text"] = ergBin


def Hex():
    ergHex = hex(int(Ergebnis))
    label4["text"] = ergHex


def Zeig_Text(Wert):
    label1["text"] += Wert


def clear():
    label1["text"] = ""
    label2["text"] = ""
    label3["text"] = ""
    label4["text"] = ""
    label5["text"] = ""
    label6["text"] = ""
    entryl.delete("0", "end")


def btc():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    dict_BTC = json.loads(response.text)
    label5["text"] = dict_BTC["bitcoin"]["usd"]


def eth():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
    dict_ETH = json.loads(response.text)
    label6["text"] = dict_ETH["ethereum"]["usd"]


def Graph():
    plt.get_current_fig_manager().set_window_title("Plot BTC ETH und ADA zu USD")
    crypto = "BTC"
    currency = "USD"

    start = dt.datetime(2021, 1, 1)
    end = dt.datetime.now()

    btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)
    ada = web.DataReader(f"ADA-{currency}", "yahoo", start, end)

    plt.rcParams['axes.facecolor'] = 'black'
    plt.yscale("linear")

    plt.title("Crypto Price Chart")

    plt.plot(btc['Close'], label="BITCOIN")
    plt.plot(eth['Close'], label="ETHEREUM")
    plt.plot(ada['Close'], label="CARDANO")
    plt.legend(facecolor='k', labelcolor='w', loc="upper left")

    plt.show()


def Graph_einzeln():

    v = entryl.get()
    currency = "USD"
    crypto = str(v)
    plt.get_current_fig_manager().set_window_title("Plot " + crypto.upper())
    start = dt.datetime(2021, 1, 1)
    end = dt.datetime.now()

    btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    plt.rcParams['axes.facecolor'] = 'black'
    plt.yscale("linear")
    plt.title("Crypto Price Chart")

    plt.plot(btc['Close'], label=crypto)
    plt.legend(facecolor='k', labelcolor='w', loc="upper left")

    plt.show()


def cur_auswahl():
    Indices = listbox1.curselection()
    for index in Indices:
        v = listbox1.get(index)
    currency = "USD"

    crypto = str(v)
    plt.get_current_fig_manager().set_window_title("Plot " + crypto.upper())
    start = dt.datetime(2021, 1, 1)
    end = dt.datetime.now()

    btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    plt.rcParams['axes.facecolor'] = 'black'
    plt.yscale("linear")
    plt.title("Crypto Price Chart")

    plt.plot(btc['Close'], label=crypto)
    plt.legend(facecolor='k', labelcolor='w', loc="upper left")

    plt.show()


def createNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("400x320")
    newWindow.title("Weiter Infos")
    myFont = font.Font(family="Helvetica", slant="italic",
                       size=13, underline=0, weight="bold")
    labelInfo1 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo1.grid(column=3, row=2, columnspan=2)
    labelInfo1_1 = tk.Label(newWindow, text="id", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo1_1.grid(column=1, row=2)
    labelInfo2 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo2.grid(column=2, row=3, columnspan=2)
    labelInfo2_1 = tk.Label(newWindow, text="Current Price in USD", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo2_1.grid(column=1, row=3,)
    labelInfo3 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo3.grid(column=2, row=4, columnspan=2)
    labelInfo3_1 = tk.Label(newWindow, text="high 24h", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo3_1.grid(column=1, row=4,)
    labelInfo4 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo4.grid(column=2, row=5, columnspan=2)
    labelInfo4_1 = tk.Label(newWindow, text="low 24h", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo4_1.grid(column=1, row=5,)
    labelInfo5 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo5.grid(column=2, row=6, columnspan=2)
    labelInfo5_1 = tk.Label(newWindow, text="Price change 24h", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo5_1.grid(column=1, row=6,)
    labelInfo6 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo6.grid(column=2, row=7, columnspan=2)
    labelInfo6_1 = tk.Label(newWindow, text="All time hight", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo6_1.grid(column=1, row=7,)
    labelInfo7 = tk.Label(newWindow, text="", background="white",
                          foreground="red", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo7.grid(column=2, row=8, columnspan=2)
    labelInfo7_1 = tk.Label(newWindow, text="All time hight change in %", background="white",
                            foreground="black", width=20, height=2, relief=tk.SUNKEN, font=myFont)
    labelInfo7_1.grid(column=1, row=8,)

    Indices = listbox2.curselection()
    for index in Indices:
        c = listbox2.get(index)

    name = str(c)
    print(name)
    response = requests.get(
        f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={name}&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    print(response)
    dict_BTC = json.loads(response.text)
    labelInfo1["text"] = dict_BTC[0]["id"]
    labelInfo2["text"] = dict_BTC[0]["current_price"]
    labelInfo3["text"] = dict_BTC[0]["high_24h"]
    labelInfo4["text"] = dict_BTC[0]["low_24h"]
    labelInfo5["text"] = dict_BTC[0]["price_change_24h"]
    labelInfo6["text"] = dict_BTC[0]["ath"]
    labelInfo7["text"] = dict_BTC[0]["ath_change_percentage"]


button1 = tk.Button(root, text="1", width=20, height=2,
                    command=lambda: Zeig_Text("1"), font=myFont)
button2 = tk.Button(root, text="2", width=20, height=2,
                    command=lambda: Zeig_Text("2"), font=myFont)
button3 = tk.Button(root, text="3", width=20, height=2,
                    command=lambda: Zeig_Text("3"), font=myFont)
button4 = tk.Button(root, text="4", width=20, height=2,
                    command=lambda: Zeig_Text("4"), font=myFont)
button5 = tk.Button(root, text="5", width=20, height=2,
                    command=lambda: Zeig_Text("5"), font=myFont)
button6 = tk.Button(root, text="6", width=20, height=2,
                    command=lambda: Zeig_Text("6"), font=myFont)
button7 = tk.Button(root, text="7", width=20, height=2,
                    command=lambda: Zeig_Text("7"), font=myFont)
button8 = tk.Button(root, text="8", width=20, height=2,
                    command=lambda: Zeig_Text("8"), font=myFont)
button9 = tk.Button(root, text="9", width=20, height=2,
                    command=lambda: Zeig_Text("9"), font=myFont)
button0 = tk.Button(root, text="0", width=20, height=2,
                    command=lambda: Zeig_Text("0"), font=myFont)
buttonPl = tk.Button(root, text="Addition", width=20, height=2,
                     command=lambda: Zeig_Text("+"), font=myFont)
buttonMin = tk.Button(root, text="Subtraktion", width=20, height=2,
                      command=lambda: Zeig_Text("-"), font=myFont)
buttonMul = tk.Button(root, text="Multiplikation", width=20, height=2,
                      command=lambda: Zeig_Text("*"), font=myFont)
buttonDiv = tk.Button(root, text="Division", width=20, height=2,
                      command=lambda: Zeig_Text("/"), font=myFont)
buttonErg = tk.Button(root, text="Ergebnis", background="lightgreen",
                      foreground="black", width=40,
                      height=2, command=Rechnung, font=myFont)
buttonDel = tk.Button(root, text="Löschen", background="red",
                      foreground="black", width=20, height=2,
                      command=lambda: clear(), font=myFont)
buttonKom = tk.Button(root, text="Komma", width=20, height=2,
                      command=lambda: Zeig_Text("."), font=myFont)
buttonExp = tk.Button(root, text="X hoch N", width=20, height=2,
                      command=lambda: Zeig_Text("**"), font=myFont)
buttonWur = tk.Button(root, text="Quadrat Wurtzel aus x", width=20, height=2,
                      command=lambda: [Zeig_Text("**(1/2)"), Rechnung()], font=myFont)
buttonBin = tk.Button(root, text="Ergebnis in BIN", background="lightblue", width=40, height=2,
                      command=Binaer, font=myFont)
buttonHex = tk.Button(root, text="Ergebnis in HEX", background="salmon", width=40, height=2,
                      command=Hex, font=myFont)
buttonBTC = tk.Button(root, text="Aktueller BTC Kurs in USD", background="snow", width=40, height=2,
                      command=btc, font=myFont)
buttonETH = tk.Button(root, text="Aktueller ETH Kurs in USD", background="snow", width=40, height=2,
                      command=eth, font=myFont)
buttonPlot = tk.Button(root, text="Aktueller Kurs von BTC ETH und ADA in USD als Plot ausgeben",
                       background="green", foreground="white", activebackground="lightgreen",
                       width=60, height=2,
                       command=Graph, font=myFont)
buttonEntry = tk.Button(root, text="Ploten", background="green", foreground="white",
                        activebackground="lightgreen", width=15, height=2,
                        command=Graph_einzeln, font=myFont)
buttonBox = tk.Button(root, text="Auswahl\naus Liste\nPloten", background="white",
                      width=20, height=3,
                      command=cur_auswahl, font=myFont)
buttonNewInfo = tk.Button(root, text="Weitere Infos\nzu dem Coins", background="snow",
                          width=20, height=3,
                          command=lambda: createNewWindow(), font=myFont)

button1.grid(column=2, row=0, padx=5, pady=5)
button2.grid(column=3, row=0, padx=5, pady=5)
button3.grid(column=4, row=0, padx=5, pady=5)
button4.grid(column=2, row=1, padx=5, pady=5)
button5.grid(column=3, row=1, padx=5, pady=5)
button6.grid(column=4, row=1, padx=5, pady=5)
button7.grid(column=2, row=2, padx=5, pady=5)
button8.grid(column=3, row=2, padx=5, pady=5)
button9.grid(column=4, row=2, padx=5, pady=5)
button0.grid(column=2, row=3, padx=5, pady=5)
buttonPl.grid(column=3, row=3, padx=5, pady=5)
buttonMin.grid(column=4, row=3, padx=5, pady=5)
buttonMul.grid(column=2, row=4, padx=5, pady=5)
buttonDiv.grid(column=3, row=4, padx=5, pady=5)
buttonErg.grid(column=7, row=6, columnspan=2, padx=5, pady=5)
buttonDel.grid(column=7, row=0, padx=5, pady=5)
buttonKom.grid(column=7, row=1, padx=5, pady=5)
buttonExp.grid(column=7, row=2, padx=5, pady=5)
buttonWur.grid(column=7, row=3, padx=5, pady=5)
buttonBin.grid(column=7, row=7, columnspan=2, padx=5, pady=5)
buttonHex.grid(column=7, row=8, columnspan=2, padx=5, pady=5)
buttonBTC.grid(column=7, row=9, columnspan=2, padx=5, pady=5)
buttonETH.grid(column=7, row=10, columnspan=2, padx=5, pady=5)
buttonPlot.grid(column=2, row=11, columnspan=3, padx=5, pady=5)
buttonEntry.grid(column=4, row=12, padx=5, pady=5)
buttonBox.grid(column=8, row=11, padx=1, pady=1)
buttonNewInfo.grid(column=8, row=12, padx=1, pady=1)

root.mainloop()
