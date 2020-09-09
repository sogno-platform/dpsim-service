# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class ModelElement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator
    (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, uuid=None, name=None, type=None):  # noqa: E501
        """ModelElement - a model defined in OpenAPI

        :param id: The id of this ModelElement.  # noqa: E501
        :type id: int
        :param uuid: The uuid of this ModelElement.  # noqa: E501
        :type uuid: str
        :param name: The name of this ModelElement.  # noqa: E501
        :type name: str
        :param type: The type of this ModelElement.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'id': int,
            'uuid': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'uuid': 'uuid',
            'name': 'name',
            'type': 'type'
        }

        self._id = id
        self._uuid = uuid
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ModelElement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelElement of this ModelElement.  # noqa: E501
        :rtype: ModelElement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ModelElement.


        :return: The id of this ModelElement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelElement.


        :param id: The id of this ModelElement.
        :type id: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this ModelElement.

        CIM uuid of model element  # noqa: E501

        :return: The uuid of this ModelElement.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ModelElement.

        CIM uuid of model element  # noqa: E501

        :param uuid: The uuid of this ModelElement.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this ModelElement.

        Name of model element  # noqa: E501

        :return: The name of this ModelElement.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelElement.

        Name of model element  # noqa: E501

        :param name: The name of this ModelElement.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ModelElement.

        CIM type of model element  # noqa: E501

        :return: The type of this ModelElement.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelElement.

        CIM type of model element  # noqa: E501

        :param type: The type of this ModelElement.
        :type type: str
        """

        self._type = type
