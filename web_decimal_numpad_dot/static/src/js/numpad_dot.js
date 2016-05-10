(function() {

var instance = openerp;

instance.web.form.FieldFloat = instance.web.form.FieldFloat.extend({
    render_value: function() {
        var self = this;
        this._super();
        if (!this.get('readonly')){
            this.$el.find('input').on('keypress', this.floatKeypress.bind(this));
        }
    },
    floatKeypress: function(e){
        if((e.keyCode == '46' || e.charCode == '46')){
            var decimal_point = instance.web._t.database.parameters.decimal_point
            //Cancel the keypress
            e.preventDefault();
            // Add the decimal point to the value of the input field
            if(this.el.firstElementChild.value.slice(-1)!=decimal_point){
                this.$("input").val(this.$("input").val() + decimal_point);
            }
         }
    },
});

})();
