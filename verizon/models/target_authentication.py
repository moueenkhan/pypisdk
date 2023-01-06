# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.target_authentication_body import TargetAuthenticationBody


class TargetAuthentication(object):

    """Implementation of the 'TargetAuthentication' model.

    OAUTH 2 token and refresh token for TS to stream events to Target

    Attributes:
        body (TargetAuthenticationBody): TODO: type description here.
        version (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body": 'body',
        "version": 'version'
    }

    _optionals = [
        'body',
        'version',
    ]

    def __init__(self,
                 body=APIHelper.SKIP,
                 version=APIHelper.SKIP):
        """Constructor for the TargetAuthentication class"""

        # Initialize members of the class
        if body is not APIHelper.SKIP:
            self.body = body 
        if version is not APIHelper.SKIP:
            self.version = version 

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

        body = TargetAuthenticationBody.from_dictionary(dictionary.get('body')) if 'body' in dictionary.keys() else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        # Return an object of this model
        return cls(body,
                   version)
