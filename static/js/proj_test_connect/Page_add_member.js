$(document).ready(function() {
    // แสดงข้อมูล Member ทันที เมื่อเปิดหน้า "eb Page
    $.ajax({
        url: 'test_connect_database', // เรียกใช้ URL
        type: 'post', // ประเภทของการส่งข้อมูล
        data: { // ข้อมูลที่จะถูกส่งไปกับ url

        },
        success: function(ajax_test_read_database) {
            console.log(ajax_test_read_database);

            let json_txt = JSON.parse(ajax_test_read_database)
            console.log(ajax_test_read_database);
            let row_no = 0
            let row
            $.each(json_txt, function(key, value_db) {
                row_no += 1;
                row += '<tr>' +
                    '<td>' + row_no + '</td>' +
                    '<td>' + value_db.member_id + '</td>' +
                    '<td>' + value_db.member_name + '</td>' +
                    '<td>' + value_db.member_surname + '</td>' +
                    '</tr>'
            })
            $('#tb_waste_item_master_list').html(row);
            // alert("Registered successfully")
            $('#txt_id').val("");
            $('#txt_name').val("");
            $('#txt_surname').val("");
            $('#txt_id').focus();
        }
    })

    //////////////////////////////////////////////////////////////////////////////////////////////////

    // เพิ่มข้อมูล Member ผ่านทางหน้า Web Page จากการกดปุ่ม Save
    $("#btn_save").click(function() {

        let get_member_id = $('#txt_id').val();
        let get_member_name = $('#txt_name').val();
        let get_member_surname = $('#txt_surname').val();
        if (get_member_id == "") {
            alert("Please type member id")
            $('#txt_id').focus();
            return;
        }
        if (get_member_name == "") {
            alert("Please type member name")
            $('#txt_name').focus();
            return;
        }
        if (get_member_surname == "") {
            alert("Please type member surname")
            $('#txt_surname').focus();
            return;
        }

        // alert(get_btn_name)

        $.ajax({
            url: 'save_member_to_database', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'dt_member_id': get_member_id,
                'dt_member_name': get_member_name,
                'dt_member_surname': get_member_surname,
            },
            success: function(ajax_save_member_to_database) {
                console.log(ajax_save_member_to_database);

                let json_txt = JSON.parse(ajax_save_member_to_database)
                console.log(ajax_save_member_to_database);
                let row_no = 0
                let row
                $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row += '<tr>' +
                        '<td>' + row_no + '</td>' +
                        '<td>' + value_db.member_id + '</td>' +
                        '<td>' + value_db.member_name + '</td>' +
                        '<td>' + value_db.member_surname + '</td>' +
                        '</tr>'
                })
                $('#tb_waste_item_master_list').html(row);
                alert("Registered successfully")
                $('#txt_id').val("");
                $('#txt_name').val("");
                $('#txt_surname').val("");
                $('#txt_id').focus();
            }
        })
    })

    //////////////////////////////////////////////////////////////////////////////////////////////////


    // เพิ่มข้อมูล Member ผ่านทาง file excel จากการกดปุ่ม Attach file
    $("#btn_upload_excel").click(function(event) {
        event.preventDefault();
        // retrieve form element
        var form = this.form;
        // prepare data
        var data = new FormData(form);
        // get url
        var url = form.action;
        // send request
        let get_path_file_excel = $('#uploadFile_add_member').val();

        if (get_path_file_excel == "") {
            alert("Please select file excel")
            $('#uploadFile_add_member').focus();
            return;
        }
        // alert(get_btn_name)
        $.ajax({
            url: 'save_member_excel_to_database', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_save_member_excel_to_database) {
                let json_txt = JSON.parse(ajax_save_member_excel_to_database)
                console.log(ajax_save_member_excel_to_database);
                let row_no = 0
                let row
                $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row += '<tr>' +
                        '<td>' + row_no + '</td>' +
                        '<td>' + value_db.member_id + '</td>' +
                        '<td>' + value_db.member_name + '</td>' +
                        '<td>' + value_db.member_surname + '</td>' +
                        '</tr>'
                })
                $('#tb_waste_item_master_list').html(row);
                alert("Upload file successfully")
                $('#txt_id').val("");
                $('#txt_name').val("");
                $('#txt_surname').val("");
                $('#txt_id').focus();
            }
        })
    })

    //////////////////////////////////////////////////////////////////////////////////////////////////


    // Delete ข้อมูล
    $('#btn_delete').click(function() {
        let input_item_delete = $('#txt_id').val();
        console.log(input_item_delete);
        $.ajax({
            url: 'delete_member_in_datebase', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'item_delete': input_item_delete
            },
            success: function(ajax_delete_member_in_datebase) {
                let json_txt = JSON.parse(ajax_delete_member_in_datebase)
                console.log(ajax_delete_member_in_datebase);
                let row_no = 0
                let row
                $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row += '<tr>' +
                        '<td>' + row_no + '</td>' +
                        '<td>' + value_db.member_id + '</td>' +
                        '<td>' + value_db.member_name + '</td>' +
                        '<td>' + value_db.member_surname + '</td>' +
                        '</tr>'
                })
                $('#tb_waste_item_master_list').html(row);
                alert("Registered successfully")
                $('#txt_id').val("");
                $('#txt_name').val("");
                $('#txt_surname').val("");
                $('#txt_id').focus();
            }
        })
    })

    //  Search data
    $('#btn_search').click(function(event) {
        let input_item_edit = $('#txt_id').val();
        if (input_item_edit == "") {
            alert("Please type member id")
            $('#txt_id').focus();
            return;
        }
        // alert('Your Id :' + " " + input_item_edit);

        $.ajax({
            url: 'edit_member_in_datebase', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'item_edit': input_item_edit
            },
            success: function(ajax_edit_member_in_datebase) {
                let json_txt = JSON.parse(ajax_edit_member_in_datebase)
                name_txt = json_txt[0].member_name
                surname_txt = json_txt[0].member_surname
                $('#txt_name').val(name_txt);
                $('#txt_surname').val(surname_txt);
            }
        })
    })
})