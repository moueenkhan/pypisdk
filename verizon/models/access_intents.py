# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class AccessIntents(object):

    """Implementation of the 'AccessIntents' model.

    TODO: type model description here.

    Attributes:
        enable_carrier_network_access (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_carrier_network_access": 'enableCarrierNetworkAccess'
    }

    _optionals = [
        'enable_carrier_network_access',
    ]

    def __init__(self,
                 enable_carrier_network_access=False):
        """Constructor for the AccessIntents class"""

        # Initialize members of the class
        self.enable_carrier_network_access = enable_carrier_network_access 

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

        enable_carrier_network_access = dictionary.get("enableCarrierNetworkAccess") if dictionary.get("enableCarrierNetworkAccess") else False
        # Return an object of this model
        return cls(enable_carrier_network_access)
