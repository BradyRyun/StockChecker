# StockChecker

This is a simple stock checking application that will output to the command line information regarding your Robinhood account.
To get started, you will need python install on your machine. <br />

Run the following commands: <br /> 
```
pip install robin_stocks
pip install numpy
```
Once you've done this, simply run the *main.py* file. <br />
You'll be prompted to enter your username/password for Robinhood. <br />
I was originally prompted with an SMS message for 2FA. If you experience any issues with logging in, please let me know and I can add 2FA options to the script. <br />
<br />
The following will be outputted to your terminal: <br />
**Total Equity:** <br />
**Highest performing stocks** (performs above the average): <br />
**Lowest performers** (less than average return): <br />
**Distribution Average** (Diversification target): <br />
**Stocks to Purchase:** (If lower than distribution average and is a high performer) <br />
