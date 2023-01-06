# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ServiceManagementResult(object):

    """Implementation of the 'ServiceManagementResult' model.

    TODO: type model description here.

    Attributes:
        job_id (string): Auto Generated Id of the job.
        status (string): Can have one string value mentioned below - DRAFT,
            DESIGN, TESTING, PUBLISH, CERTIFY, READY_TO_USE, DEPRECATE,
            DELETED.
        state (string): Can have one string value mentioned below -
            DRAFT_INPROGRESS, DRAFT_COMPLETE, DESIGN_INPROGRESS,
            DESIGN_FAILED, DESIGN_COMPLETED, VALIDATION_INPROGRESS, 
            VALIDATION_FAILED, VALIDATION_COMPLETED, TESTING_INPROGRESS,
            TESTING_FAILED, TESTING_COMPLETED, READY_TO_USE_INPROGRESS,
            READY_TO_USE_FAILED, READY_TO_USE_COMPLETED,
            READY_TO_PRIVATE_USE_INPROGRESS, READY_TO_PRIVATE_USE_FAILED,
            READY_TO_PRIVATE_USE_COMPLETED,  PUBLISH_INPROGRESS, 
            PUBLISH_FAILED,  PUBLISH_COMPLETED,  CERTIFY_INPROGRESS, 
            CERTIFY_FAILED, CERTIFY_COMPLETED, DEPRECATE_INPROGRESS, 
            DEPRECATE_FAILED, DEPRECATE_COMPLETED, MARKDELETE_INPROGRESS,
            MARKDELETE_FAILED, MARKDELETE_COMPLETED.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_id": 'jobId',
        "status": 'status',
        "state": 'state'
    }

    _optionals = [
        'job_id',
        'status',
        'state',
    ]

    def __init__(self,
                 job_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 state=APIHelper.SKIP):
        """Constructor for the ServiceManagementResult class"""

        # Initialize members of the class
        if job_id is not APIHelper.SKIP:
            self.job_id = job_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if state is not APIHelper.SKIP:
            self.state = state 

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

        job_id = dictionary.get("jobId") if dictionary.get("jobId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        # Return an object of this model
        return cls(job_id,
                   status,
                   state)
