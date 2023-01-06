# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.metadata_annotation import MetadataAnnotation
from verizon.models.metadata_label import MetadataLabel


class Metadata(object):

    """Implementation of the 'Metadata' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        display_name (string): TODO: type description here.
        created_at (string): TODO: type description here.
        modified_at (string): TODO: type description here.
        labels (MetadataLabel): TODO: type description here.
        annotations (MetadataAnnotation): TODO: type description here.
        organization_id (int): TODO: type description here.
        partner_id (int): TODO: type description here.
        project_id (int): TODO: type description here.
        id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "display_name": 'displayName',
        "created_at": 'createdAt',
        "modified_at": 'modifiedAt',
        "labels": 'labels',
        "annotations": 'annotations',
        "organization_id": 'organizationID',
        "partner_id": 'partnerID',
        "project_id": 'projectID',
        "id": 'id'
    }

    _optionals = [
        'name',
        'display_name',
        'created_at',
        'modified_at',
        'labels',
        'annotations',
        'organization_id',
        'partner_id',
        'project_id',
        'id',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 display_name=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 labels=APIHelper.SKIP,
                 annotations=APIHelper.SKIP,
                 organization_id=APIHelper.SKIP,
                 partner_id=APIHelper.SKIP,
                 project_id=APIHelper.SKIP,
                 id=APIHelper.SKIP):
        """Constructor for the Metadata class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if modified_at is not APIHelper.SKIP:
            self.modified_at = modified_at 
        if labels is not APIHelper.SKIP:
            self.labels = labels 
        if annotations is not APIHelper.SKIP:
            self.annotations = annotations 
        if organization_id is not APIHelper.SKIP:
            self.organization_id = organization_id 
        if partner_id is not APIHelper.SKIP:
            self.partner_id = partner_id 
        if project_id is not APIHelper.SKIP:
            self.project_id = project_id 
        if id is not APIHelper.SKIP:
            self.id = id 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        display_name = dictionary.get("displayName") if dictionary.get("displayName") else APIHelper.SKIP
        created_at = dictionary.get("createdAt") if dictionary.get("createdAt") else APIHelper.SKIP
        modified_at = dictionary.get("modifiedAt") if dictionary.get("modifiedAt") else APIHelper.SKIP
        labels = MetadataLabel.from_dictionary(dictionary.get('labels')) if 'labels' in dictionary.keys() else APIHelper.SKIP
        annotations = MetadataAnnotation.from_dictionary(dictionary.get('annotations')) if 'annotations' in dictionary.keys() else APIHelper.SKIP
        organization_id = dictionary.get("organizationID") if dictionary.get("organizationID") else APIHelper.SKIP
        partner_id = dictionary.get("partnerID") if dictionary.get("partnerID") else APIHelper.SKIP
        project_id = dictionary.get("projectID") if dictionary.get("projectID") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   display_name,
                   created_at,
                   modified_at,
                   labels,
                   annotations,
                   organization_id,
                   partner_id,
                   project_id,
                   id)
