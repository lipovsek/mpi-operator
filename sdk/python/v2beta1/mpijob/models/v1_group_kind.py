# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mpijob.configuration import Configuration


class V1GroupKind(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'group': 'str',
        'kind': 'str'
    }

    attribute_map = {
        'group': 'group',
        'kind': 'kind'
    }

    def __init__(self, group='', kind='', local_vars_configuration=None):  # noqa: E501
        """V1GroupKind - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._kind = None
        self.discriminator = None

        self.group = group
        self.kind = kind

    @property
    def group(self):
        """Gets the group of this V1GroupKind.  # noqa: E501


        :return: The group of this V1GroupKind.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1GroupKind.


        :param group: The group of this V1GroupKind.  # noqa: E501
        :type group: str
        """
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def kind(self):
        """Gets the kind of this V1GroupKind.  # noqa: E501


        :return: The kind of this V1GroupKind.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1GroupKind.


        :param kind: The kind of this V1GroupKind.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1GroupKind):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1GroupKind):
            return True

        return self.to_dict() != other.to_dict()