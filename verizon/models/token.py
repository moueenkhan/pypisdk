# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Token(object):

    """Implementation of the 'token' model.

    TODO: type model description here.

    Attributes:
        client_id (string): TODO: type description here.
        client_secret (string): TODO: type description here.
        grant_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_id": 'client_id',
        "client_secret": 'client_secret',
        "grant_type": 'grant_type'
    }

    def __init__(self,
                 client_id=None,
                 client_secret=None,
                 grant_type=None):
        """Constructor for the Token class"""

        # Initialize members of the class
        self.client_id = client_id 
        self.client_secret = client_secret 
        self.grant_type = grant_type 

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

        client_id = dictionary.get("client_id") if dictionary.get("client_id") else None
        client_secret = dictionary.get("client_secret") if dictionary.get("client_secret") else None
        grant_type = dictionary.get("grant_type") if dictionary.get("grant_type") else None
        # Return an object of this model
        return cls(client_id,
                   client_secret,
                   grant_type)
