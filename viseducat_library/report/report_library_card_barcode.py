import time
from odoo import models, api


class ReportLibraryCardBarcode(models.AbstractModel):
    _name = "report.viseducat_library.report_library_card_barcode"
    _description = "Library Card Barcode Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['vm.library.card'].browse(docids)
        docargs = {
            'doc_model': 'vm.library.card',
            'docs': docs,
            'time': time,
        }
        return docargs
