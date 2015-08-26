$(document).ready(function(){
    $(document).on('click', ".to_send", function(){

        var form = $(this).parents("form");
        var theme = form.find('input[name="theme"]').val();
        var name = form.find('input[name="name"]').val();
        var email = form.find('input[name="email"]').val();
        var messages = form.find('textarea').val();

        $.get("/send.php",
            {
                theme: theme,
                your_name: name,
                email: email,
                messages: messages
            },
            function(data){
                //var response = JSON.stringify(data);
                var response = JSON.parse(data);

                if (response.error == 0)
                {
                    $(".popupBackground").css('display', 'none');
                    $("#popupMarket").css('display', 'none');
                    $("#popupVideo").css('display', 'none');

                    alert("Спасибо! Ваша заявка отправлена! Мы свяжемся с вами в ближайшее время!");
                }
                else
                {
                    alert("Заполните все поля!");
                }
            }
        );
    });
});