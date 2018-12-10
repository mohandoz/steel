$(function () {
    console.log("ready")
    var radioValueSteel;
    var radioValueTreat;
    var radioValueTemp;
    var radioValueHold;
    var radioValueCool;
    var radioValueMirco;

    $('input[name=steeltype]').click(function () {

        radioValueSteel = $("input[name='steeltype']:checked").val();

        if (radioValueSteel) {


        }

    });

    $('input[name=Heat-treatment]').click(function () {

        radioValueTreat = $("input[name='Heat-treatment']:checked").val();

        if (radioValueTreat) {


        }

    });

    $('input[name=Heat-Temp]').click(function () {

        radioValueTemp = $("input[name='Heat-Temp']:checked").val();

        if (radioValueTemp) {


        }

    });

    $('input[name=Holding-time]').click(function () {

        radioValueHold = $("input[name='Holding-time']:checked").val();

        if (radioValueHold) {


        }

    });

    $('input[name=cooling-media]').click(function () {

        radioValueCool = $("input[name='cooling-media']:checked").val();

        if (radioValueCool) {


        }

    });

    $('input[name=microstructure]').click(function () {

        radioValueMirco = $("input[name='microstructure']:checked").val();

        if (radioValueMirco) {


        }

    });


   





    // fixed
    var FormStuff = {

        init: function () {
            this.applyConditionalRequired();
            this.bindUIActions();
        },

        bindUIActions: function () {
            $("input[type='radio']").on("change", this.applyConditionalRequired);
        },

        applyConditionalRequired: function () {

            $(".require-if-active").each(function () {
                var el = $(this);
                if ($(el.data("require-pair")).is(":checked")) {
                    el.prop("required", true);
                } else {
                    el.prop("required", false);
                }
            });

        }

    };

    FormStuff.init();


})


