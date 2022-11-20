from scripts.helpful_scripts import encode_function_data, get_account, upgrade
from brownie import (
    network,
    Box,
    BoxV2,
    ProxyAdmin,
    TransparentUpgradeableProxy,
    Contract,
    config,
)


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    box.store(5, {"from": account})
    tx = box.retrieve()
    print(box)

    proxy_admin = ProxyAdmin.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    # initializer = box.store, 1
    initializer_encoded_data = encode_function_data()

    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        initializer_encoded_data,
        {"from": account, "gas_limit": 1000000},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    print(f"Proxy deployed to {proxy}")
    box.store(1)

    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    print(proxy_box.retrieve())
