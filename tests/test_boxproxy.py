from scripts.helpful_scripts import encode_function_data, get_account
from brownie import Box, TransparentUpgradeableProxy, Contract, ProxyAdmin


def test_proxy_delegates_calls():
    account = get_account()
    box = Box.deploy({"from": account})
    proxy_admin = ProxyAdmin.deploy({"from": account})
    box_encode_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encode_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi())

    assert proxy_box.retrieve() == 0
    proxy_box.store(5, {"from": account})
    assert proxy_box.retrieve() == 5
