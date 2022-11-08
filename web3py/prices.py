from web3 import Web3
import requests

web3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

# Requesting data from chainlink
response = requests.get(
    "https://api.etherscan.io/api?module=contract&action=getabi&address=0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c&apikey=J8RJ5U49FP4WKY5N1I1UUXVBURCDX5Z7FM"
)

# Contract address
addr = "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"

# V3 aggregator abi
abi = response.json()["result"]

contract = web3.eth.contract(address=addr, abi=abi)
latestData = contract.functions.latestRoundData().call()
price = round(float(str(latestData[1])[:-8] + "." + str(latestData[1])[-8:]), 2)
print(price)
