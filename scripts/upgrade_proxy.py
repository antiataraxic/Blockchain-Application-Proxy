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

    boxV2 = BoxV2.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    proxy = TransparentUpgradeableProxy[-1]
    proxy_admin = ProxyAdmin[-1]
    upgrade_tx = upgrade(
        account, proxy, boxV2.address, proxy_admin_contract=proxy_admin
    )

    print("Proxy has been upgraded")

    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)

    proxy_box.multiply({"from": account})
    print(proxy_box.retrieve())
