# -*- coding: utf-8 -*-


class LabelRichExample(VerticalLayout, ClickListener):
    _b = None
    _richText = None
    _editor = RichTextArea()

    def __init__(self):
        self.setSpacing(True)
        self._richText = Label('<h1>Rich text example</h1>' + '<p>The <b>quick</b> brown fox jumps <sup>over</sup> the <b>lazy</b> dog.</p>' + '<p>This text can be edited with the <i>Edit</i> -button</p>')
        self._richText.setContentMode(Label.CONTENT_XHTML)
        self.addComponent(self._richText)
        self._b = Button('Edit')
        self._b.addListener(self)
        self.addComponent(self._b)
        self._editor.setWidth('100%')

    def buttonClick(self, event):
        if self.getComponentIterator().next() == self._richText:
            self._editor.setValue(self._richText.getValue())
            self.replaceComponent(self._richText, self._editor)
            self._b.setCaption('Apply')
        else:
            self._richText.setValue(self._editor.getValue())
            self.replaceComponent(self._editor, self._richText)
            self._b.setCaption('Edit')
