#NFT Marketplace python

# Importing stuff
from thirdweb import ThirdwebSdk, SdkOptions, MintArg, ListArg
import config
#choose your network
network = "https://speedy-nodes-nyc.moralis.io/88f9e10ecc7056e5ba53e173/polygon/mainnet"   #moralis node - moralis.io

#create the object
sdk = ThirdwebSdk(SdkOptions(), network)


PRIVATE_KEY = config.PRIVATE_KEY

sdk.set_private_key(PRIVATE_KEY)
#pick your module and enter the smart contract address
market_smart_contract_address = "0x4E674fBEE5143E3b4472a5Eaf2966C7FA1673e6a"
market_module = sdk.get_market_module(market_smart_contract_address)

#pick your module and enter the smart contract address
nft_smart_contract_address = "0x16D6FEC720E9DfAD4Aa6fA1893Cbd20735c0D000"
nft_module = sdk.get_nft_module(nft_smart_contract_address)

#currency
#list an asset in the marketplace
#what arguments should be passed for the listarg
market_module.list(ListArg(asset_contract=nft_smart_contract_address,
                            token_id=1,
                            currency_contract="0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",
                            price_per_token=10,
                            quantity=1,
                            tokens_per_buyer=1,
                            seconds_until_start=30,
                            seconds_until_end=3600))
#check out out all your listings!!
print(market_module.get_all_listings())
