# -*- coding: utf-8 -*-


class OptionGroupDisabledItemsExample(VerticalLayout, Property.ValueChangeListener):
    _cities = Arrays.asList(['Berlin', 'Brussels', 'Helsinki', 'Madrid', 'Oslo', 'Paris', 'Stockholm'])

    def __init__(self):
        # Shows a notification when a selection is made. The listener will be
        # called whenever the value of the component changes, i.e when the user
        # makes a new selection.

        self.setSpacing(True)
        # 'Shorthand' constructor - also supports data binding using Containers
        citySelect = OptionGroup('Please select a city', self._cities)
        # Set disabled items
        citySelect.setItemEnabled('Helsinki', False)
        citySelect.setItemEnabled('Oslo', False)
        citySelect.setNullSelectionAllowed(False)
        # user can not 'unselect'
        citySelect.select('Berlin')
        # select this by default
        citySelect.setImmediate(True)
        # send the change to the server at once
        citySelect.addListener(self)
        # react when the user selects something
        self.addComponent(citySelect)
        self.addComponent(Label('<h3>Multi-selection</h3>', Label.CONTENT_XHTML))
        # Create the multiselect option group
        # 'Shorthand' constructor - also supports data binding using Containers
        citySelect = OptionGroup('Please select cities', self._cities)
        # Set disabled items
        citySelect.setItemEnabled('Helsinki', False)
        citySelect.setItemEnabled('Oslo', False)
        citySelect.setMultiSelect(True)
        citySelect.setNullSelectionAllowed(False)
        # user can not 'unselect'
        citySelect.select('Berlin')
        # select this by default
        citySelect.setImmediate(True)
        # send the change to the server at once
        citySelect.addListener(self)
        # react when the user selects something
        self.addComponent(citySelect)

    def valueChange(self, event):
        self.getWindow().showNotification('Selected city: ' + event.getProperty())
