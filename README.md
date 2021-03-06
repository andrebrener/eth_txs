# Ethereum Transactions

This application is a crawler that takes data from transactions that are listed in [Etherscan](https://etherscan.io/txs). This script is a good way to get a sample of basic Ethereum transactions information without having to connect a node and download all the GBs of data from all the Ethereum history.

The final table will look very similar to this one from Etherscan.

![img](https://i.imgur.com/Z0p2WKy.png)

## Getting Started

### 1. Clone Repo

`git clone https://github.com/andrebrener/eth_txs.git`

### 2. Install Packages Required

Go in the directory of the repo and run:
```pip install -r requirements.txt```

### 3. Insert Constants
In [constants.py](https://github.com/andrebrener/eth_txs/blob/master/python/constants.py) you can define `MAX_PAGE_NUMBER`, that is the maximum number of pages of Etherscan that you want to crawl.

### 4. Get Data - Uses recommendations

It can be used mainly in two different ways:

1. Run [get_eth_txs.py](https://github.com/andrebrener/eth_txs/blob/master/python/get_eth_txs.py) and the csv file containing Etherscan transactions will be saved in the `data` directory.
   
By doing this, **a repetition problem could exist**. As blocks in Ethereum are aproximately between 10-20 seconds away, a lot of transactions are incoming in a very short period of time. As the crawler loads each page individually, it can happen that when it loads page 10, there are tx that were already seen when a previous page was loaded. 

2. Set a cron with [get_eth_txs.py](https://github.com/andrebrener/eth_txs/blob/master/python/get_eth_txs.py) and then the files will be saved in the `data` directory. With this, you'll be always watching new transactions.

The script runtime makes about 100 pages in 1 minute. So, my recommendation is to set a `MAX_PAGE_NUMBER = 100` and run the cron every minute.

You can check how long the script runs in your device by decommenting the line `print("The script was {} long".format(end_time - start_time))` in [get_eth_txs.py](https://github.com/andrebrener/eth_txs/blob/master/python/get_eth_txs.py) and watching its print value.
