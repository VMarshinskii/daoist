$(document).ready(function(){

    $(document).on('click', '#order_phone .to_send', function(){
        var name = $('#order_phone input[name="name"]');
        var phone = $('#order_phone input[name="phone"]');

        $.get('/communication/create_phone_order_view/', {
            'name': name.val(),
            'phone': phone.val()
        }, function(data){
            var response = JSON.parse(data);

            $(".error_label").remove();
            if (response['errors'] == 1)
            {
                $('#order_phone').animate({'height': '295px'}, 200);
                if (response['name_error'] != undefined)
                    name.before('<p class="error_label">' + response['name_error'] + "</p>");

                if (response['phone_error'] != undefined)
                    phone.before('<p class="error_label">' + response['phone_error'] + "</p>");
            }
            else {
                $('#order_phone').animate({'height': '180px'}, 200, function(){
                    $('#order_phone').html('<h3>Заказать звонок</h3>' +
                        '<p class="form_thanks" style="margin-top:25px">Спасибо! Ваша заявка принята!</p>' +
                        '<p class="form_thanks">Мы перезвоним вам в ближайшее время.</p>');
                });

            }
        });
    });

    $(document).on('click', '#subscription .to_send', function(){
        var name = $('#subscription input[name="name"]');
        var email = $('#subscription input[name="email"]');

        $.get('/communication/add_subscriber_view/', {
            'name': name.val(),
            'email': email.val()
        }, function(data){
            var response = JSON.parse(data);

            $(".error_label").remove();
            if (response['errors'] == 1)
            {
                $('#subscription').animate({'height': '295px'}, 200);
                if (response['name_error'] != undefined)
                    name.before('<p class="error_label">' + response['name_error'] + "</p>");

                if (response['email_error'] != undefined)
                    email.before('<p class="error_label">' + response['email_error'] + "</p>");
            }
            else {
                $('#subscription').animate({'height': '180px'}, 200, function(){
                    $('#subscription').html('<h3>Подписаться на новости</h3>' +
                        '<p class="form_thanks" style="margin-top:25px">Спасибо! Ваша заявка принята!</p>' +
                        '<p class="form_thanks">Мы включили вас в список рассылки.</p>');
                });
            }
        });
    });

});