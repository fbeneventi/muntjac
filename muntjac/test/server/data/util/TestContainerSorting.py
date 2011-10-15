# Copyright (C) 2010 IT Mill Ltd.
# Copyright (C) 2011 Richard Lincoln
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __pyjamas__ import (ARGERROR, POSTINC,)
# from java.util.HashMap import (HashMap,)
# from junit.framework.TestCase import (TestCase,)


class TestContainerSorting(TestCase):
    _ITEM_DATA_MINUS2_NULL = 'Data -2 null'
    _ITEM_DATA_MINUS2 = 'Data -2'
    _ITEM_DATA_MINUS1 = 'Data -1'
    _ITEM_DATA_MINUS1_NULL = 'Data -1 null'
    _ITEM_ANOTHER_NULL = 'Another null'
    _ITEM_STRING_2 = 'String 2'
    _ITEM_STRING_NULL2 = 'String null'
    _ITEM_STRING_1 = 'String 1'
    _PROPERTY_INTEGER_NULL2 = 'integer-null'
    _PROPERTY_INTEGER_NOT_NULL = 'integer-not-null'
    _PROPERTY_STRING_NULL = 'string-null'
    _PROPERTY_STRING_ID = 'string-not-null'

    def setUp(self):
        super(TestContainerSorting, self).setUp()

    def testEmptyFilteredIndexedContainer(self):
        ic = IndexedContainer()
        self.addProperties(ic)
        self.populate(ic)
        ic.addContainerFilter(self._PROPERTY_STRING_ID, 'aasdfasdfasdf', True, False)
        ic.sort([self._PROPERTY_STRING_ID], [True])

    def testFilteredIndexedContainer(self):
        ic = IndexedContainer()
        self.addProperties(ic)
        self.populate(ic)
        ic.addContainerFilter(self._PROPERTY_STRING_ID, 'a', True, False)
        ic.sort([self._PROPERTY_STRING_ID], [True])
        self.verifyOrder(ic, [self._ITEM_ANOTHER_NULL, self._ITEM_DATA_MINUS1, self._ITEM_DATA_MINUS1_NULL, self._ITEM_DATA_MINUS2, self._ITEM_DATA_MINUS2_NULL])

    def testIndexedContainer(self):
        ic = IndexedContainer()
        self.addProperties(ic)
        self.populate(ic)
        ic.sort([self._PROPERTY_STRING_ID], [True])
        self.verifyOrder(ic, [self._ITEM_ANOTHER_NULL, self._ITEM_DATA_MINUS1, self._ITEM_DATA_MINUS1_NULL, self._ITEM_DATA_MINUS2, self._ITEM_DATA_MINUS2_NULL, self._ITEM_STRING_1, self._ITEM_STRING_2, self._ITEM_STRING_NULL2])
        ic.sort([self._PROPERTY_INTEGER_NOT_NULL, self._PROPERTY_INTEGER_NULL2, self._PROPERTY_STRING_ID], [True, False, True])
        self.verifyOrder(ic, [self._ITEM_DATA_MINUS2, self._ITEM_DATA_MINUS2_NULL, self._ITEM_DATA_MINUS1, self._ITEM_DATA_MINUS1_NULL, self._ITEM_ANOTHER_NULL, self._ITEM_STRING_NULL2, self._ITEM_STRING_1, self._ITEM_STRING_2])
        ic.sort([self._PROPERTY_INTEGER_NOT_NULL, self._PROPERTY_INTEGER_NULL2, self._PROPERTY_STRING_ID], [True, True, True])
        self.verifyOrder(ic, [self._ITEM_DATA_MINUS2_NULL, self._ITEM_DATA_MINUS2, self._ITEM_DATA_MINUS1_NULL, self._ITEM_DATA_MINUS1, self._ITEM_ANOTHER_NULL, self._ITEM_STRING_NULL2, self._ITEM_STRING_1, self._ITEM_STRING_2])

    def testHierarchicalContainer(self):
        hc = HierarchicalContainer()
        self.populateContainer(hc)
        hc.sort(['name'], [True])
        self.verifyOrder(hc, ['Audi', 'C++', 'Call of Duty', 'Cars', 'English', 'Fallout', 'Finnish', 'Ford', 'Games', 'Java', 'Might and Magic', 'Natural languages', 'PHP', 'Programming languages', 'Python', 'Red Alert', 'Swedish', 'Toyota', 'Volvo'])
        self.assertArrays(list(hc.rootItemIds()), [self._nameToId['Cars'], self._nameToId['Games'], self._nameToId['Natural languages'], self._nameToId['Programming languages']])
        self.assertArrays(list(hc.getChildren(self._nameToId['Games'])), [self._nameToId['Call of Duty'], self._nameToId['Fallout'], self._nameToId['Might and Magic'], self._nameToId['Red Alert']])

    @classmethod
    def populateContainer(cls, container):
        container.addContainerProperty('name', str, None)
        cls.addItem(container, 'Games', None)
        cls.addItem(container, 'Call of Duty', 'Games')
        cls.addItem(container, 'Might and Magic', 'Games')
        cls.addItem(container, 'Fallout', 'Games')
        cls.addItem(container, 'Red Alert', 'Games')
        cls.addItem(container, 'Cars', None)
        cls.addItem(container, 'Toyota', 'Cars')
        cls.addItem(container, 'Volvo', 'Cars')
        cls.addItem(container, 'Audi', 'Cars')
        cls.addItem(container, 'Ford', 'Cars')
        cls.addItem(container, 'Natural languages', None)
        cls.addItem(container, 'Swedish', 'Natural languages')
        cls.addItem(container, 'English', 'Natural languages')
        cls.addItem(container, 'Finnish', 'Natural languages')
        cls.addItem(container, 'Programming languages', None)
        cls.addItem(container, 'C++', 'Programming languages')
        cls.addItem(container, 'PHP', 'Programming languages')
        cls.addItem(container, 'Java', 'Programming languages')
        cls.addItem(container, 'Python', 'Programming languages')

    _index = 0
    _nameToId = dict()
    _idToName = dict()

    @classmethod
    def addItem(cls, *args):
        _0 = args
        _1 = len(args)
        if _1 == 3:
            container, string, parent = _0
            cls._nameToId.put(string, cls._index)
            cls._idToName.put(cls._index, string)
            item = container.addItem(cls._index)
            item.getItemProperty('name').setValue(string)
            if parent is not None and isinstance(container, HierarchicalContainer):
                container.setParent(cls._index, cls._nameToId[parent])
            cls._index += 1
        elif _1 == 5:
            ic, id, string_null, integer, integer_null = _0
            i = ic.addItem(id)
            i.getItemProperty(cls._PROPERTY_STRING_ID).setValue(id)
            i.getItemProperty(cls._PROPERTY_STRING_NULL).setValue(string_null)
            i.getItemProperty(cls._PROPERTY_INTEGER_NOT_NULL).setValue(integer)
            i.getItemProperty(cls._PROPERTY_INTEGER_NULL2).setValue(integer_null)
            return i
        else:
            raise ARGERROR(3, 5)

    def verifyOrder(self, ic, idOrder):
        size = len(ic)
        actual = [None] * size
        i = ic.getItemIds()
        index = 0
        while i.hasNext():
            o = i.next()
            if o.getClass() == int and idOrder[index].getClass() == str:
                o = self._idToName[o]
            actual[POSTINC(globals(), locals(), 'index')] = o
        self.assertArrays(actual, idOrder)

    def assertArrays(self, actualObjects, expectedObjects):
        self.assertEquals('Actual contains a different number of values than was expected', len(expectedObjects), len(actualObjects))
        _0 = True
        i = 0
        while True:
            if _0 is True:
                _0 = False
            else:
                i += 1
            if not (i < len(actualObjects)):
                break
            actual = actualObjects[i]
            expected = expectedObjects[i]
            self.assertEquals('Item[' + i + '] does not match', expected, actual)

    def populate(self, ic):
        self.addItem(ic, self._ITEM_STRING_1, self._ITEM_STRING_1, 1, 1)
        self.addItem(ic, self._ITEM_STRING_NULL2, None, 0, None)
        self.addItem(ic, self._ITEM_STRING_2, self._ITEM_STRING_2, 2, 2)
        self.addItem(ic, self._ITEM_ANOTHER_NULL, None, 0, None)
        self.addItem(ic, self._ITEM_DATA_MINUS1, self._ITEM_DATA_MINUS1, -1, -1)
        self.addItem(ic, self._ITEM_DATA_MINUS1_NULL, None, -1, None)
        self.addItem(ic, self._ITEM_DATA_MINUS2, self._ITEM_DATA_MINUS2, -2, -2)
        self.addItem(ic, self._ITEM_DATA_MINUS2_NULL, None, -2, None)

    def addProperties(self, ic):
        ic.addContainerProperty('id', str, None)
        ic.addContainerProperty(self._PROPERTY_STRING_ID, str, '')
        ic.addContainerProperty(self._PROPERTY_STRING_NULL, str, None)
        ic.addContainerProperty(self._PROPERTY_INTEGER_NULL2, int, None)
        ic.addContainerProperty(self._PROPERTY_INTEGER_NOT_NULL, int, 0)
        ic.addContainerProperty('comparable-null', int, 0)

    class MyObject(TestCase.Comparable):
        _data = None

        def compareTo(self, o):
            if o is None:
                return 1
            if o.data is None:
                return 0 if self._data is None else 1
            elif self._data is None:
                return -1
            else:
                return self._data.compareTo(o.data)