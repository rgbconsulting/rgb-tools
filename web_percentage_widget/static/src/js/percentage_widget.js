/******************************************************************************
    WEB Percentage Widget
    See README file for full copyright and licensing details.
******************************************************************************/

openerp.web_percentage_widget = function(instance) {

    instance.web.form.widgets.add('percentage', 'instance.web_percentage_widget.PercentageWidget');
    instance.web_percentage_widget.PercentageWidget = instance.web.form.FieldFloat.extend({

        display_name: 'PercentageWidget',
        template: "PercentageWidget",
        render_value: function() {
            if (!this.get("effective_readonly")) {
                this._super();
            } else {
                var _value = parseFloat(this.get('value'));
                if (isNaN(_value)) {
                    this.$el.find(".percentage_filed").text('');
                }
                else{
                    this.$el.find(".percentage_filed").text((_value*100).toFixed(2) + '%');
                }
            }
        }
    });

    instance.web.list.columns.add('field.percentage', 'instance.web.list.Percentage');
    instance.web.list.Percentage = instance.web.list.Column.extend({

        _format: function (row_data, options) {
            var _value = parseFloat(row_data[this.id].value);
            if (isNaN(_value)) {
                return null;
            }
            return (_value*100).toFixed(2) + '%';
        }
    });

}
