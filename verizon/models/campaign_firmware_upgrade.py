# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from verizon.api_helper import APIHelper
from verizon.models.v3_time_window import V3TimeWindow


class CampaignFirmwareUpgrade(object):

    """Implementation of the 'CampaignFirmwareUpgrade' model.

    Firmware upgrade for devices.

    Attributes:
        campaign_name (string): Campaign name
        firmware_name (string): Firmware name to upgrade to
        firmware_from (string): Old firmware version
        firmware_to (string): New firmware version
        protocol (string): Valid values include: LWM2M, OMA and HTTP.
        start_date (date): Campaign start date
        end_date (date): Campaign end date
        campaign_time_window_list (list of V3TimeWindow): List of allowed
            campaign time windows
        device_list (list of string): device IMEI list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "firmware_name": 'firmwareName',
        "firmware_from": 'firmwareFrom',
        "firmware_to": 'firmwareTo',
        "protocol": 'protocol',
        "start_date": 'startDate',
        "end_date": 'endDate',
        "device_list": 'deviceList',
        "campaign_name": 'campaignName',
        "campaign_time_window_list": 'campaignTimeWindowList'
    }

    _optionals = [
        'campaign_name',
        'campaign_time_window_list',
    ]

    def __init__(self,
                 firmware_name=None,
                 firmware_from=None,
                 firmware_to=None,
                 protocol='LWM2M',
                 start_date=None,
                 end_date=None,
                 device_list=None,
                 campaign_name=APIHelper.SKIP,
                 campaign_time_window_list=APIHelper.SKIP):
        """Constructor for the CampaignFirmwareUpgrade class"""

        # Initialize members of the class
        if campaign_name is not APIHelper.SKIP:
            self.campaign_name = campaign_name 
        self.firmware_name = firmware_name 
        self.firmware_from = firmware_from 
        self.firmware_to = firmware_to 
        self.protocol = protocol 
        self.start_date = start_date 
        self.end_date = end_date 
        if campaign_time_window_list is not APIHelper.SKIP:
            self.campaign_time_window_list = campaign_time_window_list 
        self.device_list = device_list 

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

        firmware_name = dictionary.get("firmwareName") if dictionary.get("firmwareName") else None
        firmware_from = dictionary.get("firmwareFrom") if dictionary.get("firmwareFrom") else None
        firmware_to = dictionary.get("firmwareTo") if dictionary.get("firmwareTo") else None
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else 'LWM2M'
        start_date = dateutil.parser.parse(dictionary.get('startDate')).date() if dictionary.get('startDate') else None
        end_date = dateutil.parser.parse(dictionary.get('endDate')).date() if dictionary.get('endDate') else None
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else None
        campaign_name = dictionary.get("campaignName") if dictionary.get("campaignName") else APIHelper.SKIP
        campaign_time_window_list = None
        if dictionary.get('campaignTimeWindowList') is not None:
            campaign_time_window_list = [V3TimeWindow.from_dictionary(x) for x in dictionary.get('campaignTimeWindowList')]
        else:
            campaign_time_window_list = APIHelper.SKIP
        # Return an object of this model
        return cls(firmware_name,
                   firmware_from,
                   firmware_to,
                   protocol,
                   start_date,
                   end_date,
                   device_list,
                   campaign_name,
                   campaign_time_window_list)
