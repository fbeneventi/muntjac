# -*- coding: utf-8 -*-
# from com.vaadin.ui.PopupView.PopupVisibilityEvent import (PopupVisibilityEvent,)


class PopupViewClosingExample(VerticalLayout, PopupView.PopupVisibilityListener):

    def __init__(self):
        self.setSpacing(True)
        # Create the content for the popup
        content = Label('This popup will close as soon as you move the mouse cursor outside of the popup area.')
        # The PopupView popup will be as large as needed by the content
        content.setWidth('300px')
        # Construct the PopupView with simple HTML text representing the
        # minimized view
        popup = PopupView('Default popup', content)
        popup.setHideOnMouseOut(True)
        popup.addListener(self)
        self.addComponent(popup)
        content = Label('This popup will only close if you click the mouse outside the popup area.')
        # The PopupView popup will be as large as needed by the content
        content.setWidth('300px')
        popup = PopupView('Popup that won\'t auto-close', content)
        popup.setHideOnMouseOut(False)
        popup.addListener(self)
        self.addComponent(popup)

    def popupVisibilityChange(self, event):
        if not event.isPopupVisible():
            self.getWindow().showNotification('Popup closed')
