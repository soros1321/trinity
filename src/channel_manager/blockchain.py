from .neo_api import neo_api
from configure import Configure


NeoServer = neo_api.NeoApi(Configure["BlockNet"])

def add_to_channel(address, type, public_key, signature, channel_name, deposit=0, open_block_number=10 ):
        return True


def setting_transection(sender, receiver, channel_name):
    return True


def send_raw_transection(hax):
    #return NeoServer.sendrawtransaction(hax)
    return True


def NewTransection(asset_type,from_addr, to_addr, count):
    print("Signature")
    return ""


def get_balance(address, asset_type):
    if asset_type:
        return get_asset_balance(address, asset_type.upper())
    else:
        assets_balance = []
        for asset in Configure["AssetList"]:
            for a, v in asset.items():
                asset_type.append(get_asset_balance(address, a))


def get_asset_id(asset_type):
    asset = filter(lambda x: asset_type in x , Configure["AssetList"])
    if asset:
        return asset[0].getdefault(asset_type, None)
    else:
        return None

def get_asset_balance(address, asset_type):
    if get_asset_id(asset_type):
        return {"AssetType": asset_type,
            "Balance":100000}
    else:
        return None

def query_asset_balance():
    return 1000



