# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from verizon.api_helper import APIHelper
from verizon.models.v2_time_window import V2TimeWindow


class CampaignSoftware(object):

    """Implementation of the 'CampaignSoftware' model.

    Software upgrade information

    Attributes:
        id (string): Upgrade identifier
        account_name (string): Account identifier
        campaign_name (string): Campaign name
        software_name (string): Software name
        distribution_type (string): LWM2M, OMD-DM or HTTP
        make (string): Applicable make
        model (string): Applicable model
        software_from (string): Old software name
        software_to (string): New software name
        start_date (date): Campaign start date
        end_date (date): Campaign end date
        download_after_date (date): Specifies starting date client should
            download package. If null, client will download as soon as
            possible.
        download_time_window_list (list of V2TimeWindow): List of allowed
            download time windows
        install_after_date (date): Client will install package after date. If
            null, client will install as soon as possible.
        install_time_window_list (list of V2TimeWindow): List of allowed
            install time windows
        status (string): Software upgrade status

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "account_name": 'accountName',
        "software_name": 'softwareName',
        "distribution_type": 'distributionType',
        "make": 'make',
        "model": 'model',
        "software_from": 'softwareFrom',
        "software_to": 'softwareTo',
        "start_date": 'startDate',
        "end_date": 'endDate',
        "status": 'status',
        "campaign_name": 'campaignName',
        "download_after_date": 'downloadAfterDate',
        "download_time_window_list": 'downloadTimeWindowList',
        "install_after_date": 'installAfterDate',
        "install_time_window_list": 'installTimeWindowList'
    }

    _optionals = [
        'campaign_name',
        'download_after_date',
        'download_time_window_list',
        'install_after_date',
        'install_time_window_list',
    ]

    def __init__(self,
                 id=None,
                 account_name=None,
                 software_name=None,
                 distribution_type=None,
                 make=None,
                 model=None,
                 software_from=None,
                 software_to=None,
                 start_date=None,
                 end_date=None,
                 status=None,
                 campaign_name=APIHelper.SKIP,
                 download_after_date=APIHelper.SKIP,
                 download_time_window_list=APIHelper.SKIP,
                 install_after_date=APIHelper.SKIP,
                 install_time_window_list=APIHelper.SKIP):
        """Constructor for the CampaignSoftware class"""

        # Initialize members of the class
        self.id = id 
        self.account_name = account_name 
        if campaign_name is not APIHelper.SKIP:
            self.campaign_name = campaign_name 
        self.software_name = software_name 
        self.distribution_type = distribution_type 
        self.make = make 
        self.model = model 
        self.software_from = software_from 
        self.software_to = software_to 
        self.start_date = start_date 
        self.end_date = end_date 
        if download_after_date is not APIHelper.SKIP:
            self.download_after_date = download_after_date 
        if download_time_window_list is not APIHelper.SKIP:
            self.download_time_window_list = download_time_window_list 
        if install_after_date is not APIHelper.SKIP:
            self.install_after_date = install_after_date 
        if install_time_window_list is not APIHelper.SKIP:
            self.install_time_window_list = install_time_window_list 
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

        id = dictionary.get("id") if dictionary.get("id") else None
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        software_name = dictionary.get("softwareName") if dictionary.get("softwareName") else None
        distribution_type = dictionary.get("distributionType") if dictionary.get("distributionType") else None
        make = dictionary.get("make") if dictionary.get("make") else None
        model = dictionary.get("model") if dictionary.get("model") else None
        software_from = dictionary.get("softwareFrom") if dictionary.get("softwareFrom") else None
        software_to = dictionary.get("softwareTo") if dictionary.get("softwareTo") else None
        start_date = dateutil.parser.parse(dictionary.get('startDate')).date() if dictionary.get('startDate') else None
        end_date = dateutil.parser.parse(dictionary.get('endDate')).date() if dictionary.get('endDate') else None
        status = dictionary.get("status") if dictionary.get("status") else None
        campaign_name = dictionary.get("campaignName") if dictionary.get("campaignName") else APIHelper.SKIP
        download_after_date = dateutil.parser.parse(dictionary.get('downloadAfterDate')).date() if dictionary.get('downloadAfterDate') else APIHelper.SKIP
        download_time_window_list = None
        if dictionary.get('downloadTimeWindowList') is not None:
            download_time_window_list = [V2TimeWindow.from_dictionary(x) for x in dictionary.get('downloadTimeWindowList')]
        else:
            download_time_window_list = APIHelper.SKIP
        install_after_date = dateutil.parser.parse(dictionary.get('installAfterDate')).date() if dictionary.get('installAfterDate') else APIHelper.SKIP
        install_time_window_list = None
        if dictionary.get('installTimeWindowList') is not None:
            install_time_window_list = [V2TimeWindow.from_dictionary(x) for x in dictionary.get('installTimeWindowList')]
        else:
            install_time_window_list = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   account_name,
                   software_name,
                   distribution_type,
                   make,
                   model,
                   software_from,
                   software_to,
                   start_date,
                   end_date,
                   status,
                   campaign_name,
                   download_after_date,
                   download_time_window_list,
                   install_after_date,
                   install_time_window_list)
