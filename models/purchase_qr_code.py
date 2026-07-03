from odoo import models, fields, api
import base64
import io
import qrcode


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    qr_code = fields.Binary("QR Code", compute='_generate_qr_code', store=True)

    @api.depends('name', 'amount_total')
    def _generate_qr_code(self):
        for rec in self:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data("Purchase No : ")
            qr.add_data(rec.name or '')
            qr.add_data(", Vendor : ")
            qr.add_data(rec.partner_id.name or '')
            qr.add_data(", Amount Total : ")
            qr.add_data(str(rec.amount_total or 0.0))
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            temp = io.BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            rec.qr_code = qr_image