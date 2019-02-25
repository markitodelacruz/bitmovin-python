# coding: utf-8

from bitmovin_python.models.abstract_condition import AbstractCondition
from bitmovin_python.models.condition_operator import ConditionOperator
from bitmovin_python.models.condition_type import ConditionType
from bitmovin_python.models.stream_condition_attribute import StreamConditionAttribute
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamCondition(AbstractCondition):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(StreamCondition, self).openapi_types
        types.update({
            'attribute': 'StreamConditionAttribute',
            'operator': 'ConditionOperator',
            'value': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(StreamCondition, self).attribute_map
        attributes.update({
            'attribute': 'attribute',
            'operator': 'operator',
            'value': 'value'
        })
        return attributes

    def __init__(self, attribute=None, operator=None, value=None, *args, **kwargs):
        super(StreamCondition, self).__init__(*args, **kwargs)

        self._attribute = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self.attribute = attribute
        self.operator = operator
        self.value = value

    @property
    def attribute(self):
        """Gets the attribute of this StreamCondition.


        :return: The attribute of this StreamCondition.
        :rtype: StreamConditionAttribute
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this StreamCondition.


        :param attribute: The attribute of this StreamCondition.
        :type: StreamConditionAttribute
        """

        if attribute is not None:
            if not isinstance(attribute, StreamConditionAttribute):
                raise TypeError("Invalid type for `attribute`, type has to be `StreamConditionAttribute`")

            self._attribute = attribute


    @property
    def operator(self):
        """Gets the operator of this StreamCondition.


        :return: The operator of this StreamCondition.
        :rtype: ConditionOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this StreamCondition.


        :param operator: The operator of this StreamCondition.
        :type: ConditionOperator
        """

        if operator is not None:
            if not isinstance(operator, ConditionOperator):
                raise TypeError("Invalid type for `operator`, type has to be `ConditionOperator`")

            self._operator = operator


    @property
    def value(self):
        """Gets the value of this StreamCondition.

        The value that should be used for comparison

        :return: The value of this StreamCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StreamCondition.

        The value that should be used for comparison

        :param value: The value of this StreamCondition.
        :type: str
        """

        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Invalid type for `value`, type has to be `str`")

            self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(StreamCondition, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(StreamCondition, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StreamCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other