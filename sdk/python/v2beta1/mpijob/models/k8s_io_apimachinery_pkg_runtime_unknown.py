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


class K8sIoApimachineryPkgRuntimeUnknown(object):
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
        'content_encoding': 'str',
        'content_type': 'str',
        'api_version': 'str',
        'kind': 'str'
    }

    attribute_map = {
        'content_encoding': 'ContentEncoding',
        'content_type': 'ContentType',
        'api_version': 'apiVersion',
        'kind': 'kind'
    }

    def __init__(self, content_encoding='', content_type='', api_version=None, kind=None, local_vars_configuration=None):  # noqa: E501
        """K8sIoApimachineryPkgRuntimeUnknown - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._content_encoding = None
        self._content_type = None
        self._api_version = None
        self._kind = None
        self.discriminator = None

        self.content_encoding = content_encoding
        self.content_type = content_type
        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind

    @property
    def content_encoding(self):
        """Gets the content_encoding of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501

        ContentEncoding is encoding used to encode 'Raw' data. Unspecified means no encoding.  # noqa: E501

        :return: The content_encoding of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """Sets the content_encoding of this K8sIoApimachineryPkgRuntimeUnknown.

        ContentEncoding is encoding used to encode 'Raw' data. Unspecified means no encoding.  # noqa: E501

        :param content_encoding: The content_encoding of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type content_encoding: str
        """
        if self.local_vars_configuration.client_side_validation and content_encoding is None:  # noqa: E501
            raise ValueError("Invalid value for `content_encoding`, must not be `None`")  # noqa: E501

        self._content_encoding = content_encoding

    @property
    def content_type(self):
        """Gets the content_type of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501

        ContentType  is serialization method used to serialize 'Raw'. Unspecified means ContentTypeJSON.  # noqa: E501

        :return: The content_type of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this K8sIoApimachineryPkgRuntimeUnknown.

        ContentType  is serialization method used to serialize 'Raw'. Unspecified means ContentTypeJSON.  # noqa: E501

        :param content_type: The content_type of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type content_type: str
        """
        if self.local_vars_configuration.client_side_validation and content_type is None:  # noqa: E501
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def api_version(self):
        """Gets the api_version of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501


        :return: The api_version of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this K8sIoApimachineryPkgRuntimeUnknown.


        :param api_version: The api_version of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501


        :return: The kind of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this K8sIoApimachineryPkgRuntimeUnknown.


        :param kind: The kind of this K8sIoApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type kind: str
        """

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
        if not isinstance(other, K8sIoApimachineryPkgRuntimeUnknown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, K8sIoApimachineryPkgRuntimeUnknown):
            return True

        return self.to_dict() != other.to_dict()
