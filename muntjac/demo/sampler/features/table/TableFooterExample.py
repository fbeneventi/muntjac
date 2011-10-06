
import re
import locale

from muntjac.demo.sampler.ExampleUtil import ExampleUtil
from muntjac.ui import VerticalLayout, Table


class TableFooterExample(VerticalLayout):

    def __init__(self):
        # Create our data source
        dataSource = ExampleUtil.getOrderContainer()

        # Calculate total sum
        totalSum = 0.0
        for i in range(len(dataSource)):
            item = dataSource.getItem(dataSource.getIdByIndex(i))
            value = item.getItemProperty(ExampleUtil.ORDER_ITEMPRICE_PROPERTY_ID).getValue()

            amount = re.search(ur'([£$€])(\d+(?:\.\d{2})?)', str(value)).groups()[1]
            totalSum += float(amount)

        # Create a table to show the data in
        table = Table('Order table', dataSource)
        table.setPageLength(6)
        table.setWidth('100%')

        # Set alignments
        table.setColumnAlignments([Table.ALIGN_LEFT, Table.ALIGN_RIGHT,
                Table.ALIGN_RIGHT, Table.ALIGN_RIGHT])

        # Set column widths
        table.setColumnExpandRatio(ExampleUtil.ORDER_DESCRIPTION_PROPERTY_ID, 1)

        # Enable footer
        table.setFooterVisible(True)

        # Add some total sum and description to footer
        table.setColumnFooter(ExampleUtil.ORDER_DESCRIPTION_PROPERTY_ID,
                'Total Price')
        table.setColumnFooter(ExampleUtil.ORDER_ITEMPRICE_PROPERTY_ID,
                locale.currency(totalSum, grouping=True))

        self.addComponent(table)