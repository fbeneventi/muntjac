# Copyright (C) 2011 Vaadin Ltd.
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
#
# Note: This is a modified file from Vaadin. For further information on
#       Vaadin please visit http://www.vaadin.com.

from muntjac.terminal.gwt.client.application_configuration \
    import ApplicationConfiguration


class WidgetLoader(RunAsyncCallback):
    """A helper class used by WidgetMap implementation. Used by the generated
    code."""

    def onFailure(self, reason):
        ApplicationConfiguration.endWidgetLoading()


    def onSuccess(self):
        self.addInstantiator()
        ApplicationConfiguration.endWidgetLoading()


    def addInstantiator(self):
        pass
