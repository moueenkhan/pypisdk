# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList


class DeviceRequest(object):

    """Implementation of the 'DeviceRequest' model.

    Request for Device Information.

    Attributes:
        account_name (string): The name of a billing account.
        devices (list of AccountDeviceList): Up to 10,000 devices that you
            want to move to a different account, specified by device
            identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "devices": 'devices'
    }

    _optionals = [
        'account_name',
        'devices',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 devices=APIHelper.SKIP):
        """Constructor for the DeviceRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if devices is not APIHelper.SKIP:
            self.devices = devices 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   devices)
