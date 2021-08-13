
from odoo.tests import common


class TestLibraryCommon(common.SavepointCase):
    def setUp(self):
        super(TestLibraryCommon, self).setUp()
        self.vm_library_card_type = self.env['vm.library.card.type']
        self.vm_library_card = self.env['vm.library.card']
        self.vm_media = self.env['vm.media']
        self.vm_media_unit = self.env['vm.media.unit']
        self.vm_media_movement = self.env['vm.media.movement']
        self.vm_media_purchase = self.env['vm.media.purchase']
        self.vm_media_queue = self.env['vm.media.queue']
        self.wizard_issue = self.env['issue.media']
        self.reserve_media = self.env['reserve.media']
        self.return_media = self.env['return.media']
