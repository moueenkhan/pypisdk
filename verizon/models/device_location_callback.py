# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DeviceLocationCallback(object):

    """Implementation of the 'DeviceLocationCallback' model.

    TODO: type model description here.

    Attributes:
        name (CallbackServiceNameEnum): The name of the callback service.
        url (string): The location of your callback listener.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "url": 'url'
    }

    def __init__(self,
                 name=None,
                 url=None):
        """Constructor for the DeviceLocationCallback class"""

        # Initialize members of the class
        self.name = name 
        self.url = url 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        url = dictionary.get("url") if dictionary.get("url") else None
        # Return an object of this model
        return cls(name,
                   url)
