# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class RequestResultWithStatus(object):

    """Implementation of the 'RequestResultWithStatus' model.

    A successful request returns the request ID and the current status.

    Attributes:
        request_id (string): The unique ID of the asynchronous request.
        status (RequestStatusEnum): The current status of the callback
            response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'requestId',
        "status": 'status'
    }

    _optionals = [
        'request_id',
        'status',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the RequestResultWithStatus class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if status is not APIHelper.SKIP:
            self.status = status 

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

        request_id = dictionary.get("requestId") if dictionary.get("requestId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status)
