# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class AccountIdentifier(object):

    """Implementation of the 'AccountIdentifier' model.

    The ID of the authenticating billing account, in the format
    `{"billingaccountid":"1234567890-12345"}`.

    Attributes:
        billingaccountid (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "billingaccountid": 'billingaccountid'
    }

    _optionals = [
        'billingaccountid',
    ]

    def __init__(self,
                 billingaccountid=APIHelper.SKIP):
        """Constructor for the AccountIdentifier class"""

        # Initialize members of the class
        if billingaccountid is not APIHelper.SKIP:
            self.billingaccountid = billingaccountid 

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

        billingaccountid = dictionary.get("billingaccountid") if dictionary.get("billingaccountid") else APIHelper.SKIP
        # Return an object of this model
        return cls(billingaccountid)
