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


class IFormFieldFactory(object):
    """Factory interface for creating new Field-instances based on
    {@link Item}, property id and uiContext (the component responsible for
    displaying fields). Currently this interface is used by {@link Form}, but
    might later be used by some other components for {@link Field} generation.

    @author IT Mill Ltd.
    @author Richard Lincoln
    @version @VERSION@
    @since 6.0
    @see TableFieldFactory
    """

    def createField(self, item, propertyId, uiContext):
        """Creates a field based on the item, property id and the component
        (most commonly {@link Form}) where the Field will be presented.

        @param item
                   the item where the property belongs to.
        @param propertyId
                   the Id of the property.
        @param uiContext
                   the component where the field is presented, most commonly
                   this is {@link Form}. uiContext will not necessary be the
                   parent component of the field, but the one that is
                   responsible for creating it.
        @return Field the field suitable for editing the specified data.
        """
        raise NotImplementedError