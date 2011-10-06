
from muntjac.ui import VerticalLayout, NativeSelect
from muntjac.data.property import IValueChangeListener


class NativeSelectionExample(VerticalLayout, IValueChangeListener):

    _cities = ['Berlin', 'Brussels', 'Helsinki', 'Madrid', 'Oslo',
            'Paris', 'Stockholm']

    def __init__(self):
        self.setSpacing(True)

        l = NativeSelect('Please select a city')

        for c in self._cities:
            l.addItem(c)

        l.setNullSelectionAllowed(False)
        l.setValue('Berlin')
        l.setImmediate(True)
        l.addListener(self)
        self.addComponent(l)

    # Shows a notification when a selection is made.
    def valueChange(self, event):
        self.getWindow().showNotification('Selected city: '
                + event.getProperty())