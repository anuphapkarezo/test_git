$(document).ready(function() {
    $('#txt_user').focus();

    $.ajax({
        url: 'selection_values', // เรียกใช้ URL
        type: 'post', // ประเภทของการส่งข้อมูล
        data: { // ข้อมูลที่จะถูกส่งไปกับ url

        },
        success: function(ajax_selection_values) {
            // console.log(ajax_selection_values);
            let before_select = '<select id="opt_case" style="width: 250px; margin-left: 30px; margin-top: 20px;">'
            let default_select = '<option value="default" selected>Please select data</option>'
            let after_select = '</select>'
            var select_login;
            let row_option_value = '';

            let json_txt = JSON.parse(ajax_selection_values)
            let row_no = 0

            $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row_option_value += '<option value="' + value_db.user_login + '">' + value_db.user_login + '</option>'
                })
                // console.log(row_option_value);
            select_login = before_select + default_select + row_option_value + after_select
                // console.log(select_login);
            $('#opt_case').html(select_login);
        }
    })


    $("#btn_save").click(function() {
        let input_item_user = $('#txt_user').val();
        let input_item_pass = $('#txt_pass').val();
        if (input_item_user == "") {
            alert("Please type Username")
            $('#txt_user').focus();
            return;
        }
        if (input_item_pass == "") {
            alert("Please type Password")
            $('#txt_pass').focus();
            return;
        }
        console.log(input_item_user);
        console.log(input_item_pass);
        $.ajax({
            url: 'page_login_programming', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'item_user': input_item_user,
                'item_pass': input_item_pass
            },
            success: function(ajax_page_login) {
                let json_txt = JSON.parse(ajax_page_login)
                $('#opt_case').val("Test");

                user_txt = json_txt[0].user_login
                pass_txt = json_txt[0].pass_login

                console.log("DB user :" + user_txt);
                console.log("DB pass :" + pass_txt);
                if (input_item_user == user_txt && input_item_pass == pass_txt) {
                    alert("Login completed")
                    $('#txt_user').val('');
                    $('#txt_pass').val('');
                    $('#txt_user').focus();
                    window.open('Page_add_member')

                } else {
                    alert("Username Or Password incorrect, Try to check again please.")
                }
            }
        })
    })

    $("#btn_cancel").click(function(event) {
        $('#txt_user').val('');
        $('#txt_pass').val('');
        $('#txt_user').focus();
    })

})