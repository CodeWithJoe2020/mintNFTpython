# Importing stuff
from thirdweb import ThirdwebSdk, SdkOptions, MintArg
import config               #using privatekey in external file(config.py)


#choose your network
network = "https://speedy-nodes-nyc.moralis.io/88f9e10ecc7056e5ba53e173/polygon/mainnet"   #node from moralis.io

#create the object
sdk = ThirdwebSdk(SdkOptions(), network)


PRIVATE_KEY = config.PRIVATE_KEY

sdk.set_private_key(PRIVATE_KEY)


#pick your module and enter the smart contract address
nft_smart_contract_address = "0x16D6FEC720E9DfAD4Aa6fA1893Cbd20735c0D000"
nft_module = sdk.get_nft_module(nft_smart_contract_address)


#Mint an NFT on your smartcontract
name_nft = "Elon Weed"
description_nft = "Elon Musk smokes weed on Joe Rogan"
image_nft = "https://preview.redd.it/0hkeya69rx421.jpg?width=779&format=pjpg&auto=webp&s=1b562656f081d8424e09c7eca6373f8b78891428"
prop = {"level":"2"}


nft_module.mint(MintArg(name=name_nft,
description=description_nft,
image_uri=image_nft,
properties=prop))
#check your balance to check if you minted an nft!
print(nft_module.balance())
