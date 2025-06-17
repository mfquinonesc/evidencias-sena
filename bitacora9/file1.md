## Hacer que el campo fecha y hora del formulario Órdenes de Servicio sea obligatorio

En el modelo para crear las órdenes de servicio se modificó el campo ```date``` para que sea requerido y también se agregó una excepción cuando el campo es nulo.

```python
    date = fields.Datetime('Fecha y Hora', default=lambda *a: fields.Datetime.now(), copy=False, required=True)
```

```python
    @api.model
        def create(self, vals, ):
            if not vals['date']:
                raise ValidationError("Debe seleccionar fecha y hora")
            if 'folio' not in vals:
                number = self.env['ir.sequence'].next_by_code('motion.service_orders')
                vals['folio'] = str(number)
            if self.state not in vals:
                vals['state'] = 'nueva'
                if 'employee_id' in vals and vals['employee_id']:
                    vals['state'] = 'assigned'
            result = super(serviceOrder, self).create(vals)
            # self.defaul_message(result.id)
            return result
```