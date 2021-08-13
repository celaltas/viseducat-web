from odoo import models, fields


class VmMedia(models.Model):
    _name = "vm.media"
    _description = "Media Details"
    _order = "name"

    name = fields.Char('Title', size=128, required=True)
    isbn = fields.Char('ISBN Code', size=64)
    tags = fields.Many2many('vm.tag', string='Tag(s)')
    author_ids = fields.Many2many(
        'vm.author', string='Author(s)', required=True)
    edition = fields.Char('Edition')
    description = fields.Text('Description')
    publisher_ids = fields.Many2many(
        'vm.publisher', string='Publisher(s)', required=True)
    course_ids = fields.Many2many('vm.course', string='Course')
    movement_line = fields.One2many('vm.media.movement', 'media_id',
                                    'Movements')
    subject_ids = fields.Many2many(
        'vm.subject', string='Subjects')
    internal_code = fields.Char('Internal Code', size=64)
    queue_ids = fields.One2many('vm.media.queue', 'media_id', 'Media Queue')
    unit_ids = fields.One2many('vm.media.unit', 'media_id', 'Units')
    media_type_id = fields.Many2one('vm.media.type', 'Media Type')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_name_isbn',
         'unique(isbn)',
         'ISBN code must be unique per media!'),
        ('unique_name_internal_code',
         'unique(internal_code)',
         'Internal Code must be unique per media!'),
    ]
