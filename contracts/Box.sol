// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Box {
    uint256 private _favouritenumber;
    event ValueChanged(uint256 _favouritenumber);

    function store(uint256 favouritenumber) public {
        _favouritenumber = favouritenumber;
        emit ValueChanged(_favouritenumber);
    }

    function retrieve() public view returns (uint256) {
        return _favouritenumber;
    }
}
