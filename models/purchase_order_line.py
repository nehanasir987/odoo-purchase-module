from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    quan = fields.Integer(
        string="Extra Amount",
        default=0,
        help="Manually entered extra amount, added to the subtotal and total of this line."
    )

    @api.depends('product_qty', 'price_unit', 'tax_ids', 'discount', 'quan')
    def _compute_amount(self):
        
        super()._compute_amount()
        for line in self:
            line.price_subtotal += line.quan
            line.price_total += line.quan

    def _prepare_account_move_line(self, move=None):
        vals = super()._prepare_account_move_line(move=move)
        vals['quan'] = self.quan
        vals['quantity'] = self.product_qty

        return vals
    


    
    






class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    quan = fields.Integer(
        string="Extra Amount",
        readonly=True,

        default=0,
        help="Extra amount copied automatically from the Purchase Order Line."
    )




    total_quan = fields.Integer(
        string="Total Extra Amount",
        default=0,
        help="Sum of all Extra Amount values from the Purchase Order lines."
    )




    @api.depends('quan')
    def _compute_totals(self):
        super()._compute_totals()
        for line in self:
            if line.display_type == 'product':
                line.price_subtotal += line.quan
                line.price_total += line.quan





