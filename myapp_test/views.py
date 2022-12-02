from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Table_members , Table_login
import pandas as pd
from .proj_test_function import save_Table_members , save_data_to_database_from_page , update_member_list , update_member_list_from_page
import json
from json import dumps


# Create your views here.
def go_index(request):
    return render(request, 'index_test.html')

def Page_add_member(request):
    return render(request, 'Page_add_member.html')

def page_login(request):
    return render(request, 'page_login.html')

#เปิดหน้า web Page ขึ้นมาแล้วให้แสดงข้อมูลเลย
@csrf_exempt
def test_connect_database(request):
    # btn_name_sv = request.POST['btn_name']
    # member_id_dt = request.POST['dt_member_id']
    # member_name_dt = request.POST['dt_member_name']
    # member_surname_dt = request.POST['dt_member_surname']
    # print("Test request server : " , btn_name_sv)
    # print("Test request POST : " , member_id_dt , member_name_dt , member_surname_dt)

     #Read Excel
    # df_excel = pd.read_excel(r"C:\django_Project\project_test\static\upload\add_member.xlsx")
    # print(df_excel)

    #save_Table_members(df_excel)

    #save_data_to_database_from_page(request)

     # Read database from dBeaver and Print show
    db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
    #print(db_item_master)

    json_records = db_item_master.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)

    ajax_test_read_database = dumps(data_loads)
    return HttpResponse(ajax_test_read_database)

#Save ข้อมูล Member ที่ถูกเพิ่มเข้ามาใหม่ผ่านทาง web page จากการกดปุ่ม Save
@csrf_exempt
def save_member_to_database(request):
    member_id_edit = request.POST['dt_member_id']
    # btn_name_sv = request.POST['btn_name']
    # member_id_dt = request.POST['dt_member_id']
    # member_name_dt = request.POST['dt_member_name']
    # member_surname_dt = request.POST['dt_member_surname']
    # print("Test request server : " , btn_name_sv)
    # print("Test request POST : " , member_id_dt , member_name_dt , member_surname_dt)

     #Read Excel
    # df_excel = pd.read_excel(r"C:\django_Project\project_test\static\upload\add_member.xlsx")
    # print(df_excel)

    #save_Table_members(df_excel)
    check_id = Table_members.objects.filter(member_id=member_id_edit).exists() #เช็คค่า ID
    print(check_id)
    if check_id == False:
        save_data_to_database_from_page(request)

        # Read database from dBeaver and Print show
        db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
        #print(db_item_master)

        json_records = db_item_master.reset_index().to_json(orient='records')
        data_loads = json.loads(json_records)

        ajax_save_member_to_database = dumps(data_loads)
        return HttpResponse(ajax_save_member_to_database)

    else:
        update_member_list_from_page(request)
        db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
        json_records = db_item_master.reset_index().to_json(orient='records')
        data_loads = json.loads(json_records)
       
        ajax_save_member_to_database = dumps(data_loads)
        return HttpResponse(ajax_save_member_to_database)


#Save ข้อมูล Member ที่ถูกเพิ่มเข้ามาทาง File Excelจากการกดปุ่ม Attach file
@csrf_exempt
def save_member_excel_to_database(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_save_member_excel_to_database = 'Not found file for upload'
        return HttpResponse(ajax_save_member_excel_to_database)

    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))
    excel_raw_data['member_id'] = excel_raw_data['member_id'].astype(str) #Convert int64 to str

    db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
    # print("Path File :" , excel_raw_data)

    check_db = Table_members.objects.all().exists() #จะได้ค่า true/false เท่านั้น
    print(check_db)
    if check_db == False:
         save_Table_members(excel_raw_data)
         db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
         json_records = db_item_master.reset_index().to_json(orient='records')
         data_loads = json.loads(json_records)
         ajax_save_member_excel_to_database = dumps(data_loads)
         return HttpResponse(ajax_save_member_excel_to_database)
    
    else:
        db_item_master["exists_data"] = "YES"
        
        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["member_id"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
        # print(df_merge_data[["member_id" , "exists_data"]])
        # ajax_save_member_excel_to_database = 1
        # return HttpResponse(ajax_save_member_excel_to_database)
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"member_name_x":"member_name" , "member_surname_x":"member_surname"  },axis=1 , inplace=True)
            save_Table_members(df_merge_data_save)
            db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
            json_records = db_item_master.reset_index().to_json(orient='records')
            data_loads = json.loads(json_records)
            ajax_save_member_excel_to_database = dumps(data_loads)
            return HttpResponse(ajax_save_member_excel_to_database)
            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_member_list(df_merge_data_update)
            #convert to Json
            db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
            json_records = db_item_master.reset_index().to_json(orient='records')
            data_loads = json.loads(json_records)
            ajax_save_member_excel_to_database = dumps(data_loads)
            return HttpResponse(ajax_save_member_excel_to_database)

    # btn_name_sv = request.POST['btn_name']
    # member_id_dt = request.POST['dt_member_id']
    # member_name_dt = request.POST['dt_member_name']
    # member_surname_dt = request.POST['dt_member_surname']
    # print("Test request server : " , btn_name_sv)
    # print("Test request POST : " , member_id_dt , member_name_dt , member_surname_dt)

     #Read Excel
    # path_file_excel_upload = request.POST['get_path']
    # print("Path File :" , path_file_excel_upload)

    # df_excel = pd.read_excel(path_file_excel_upload)
    # print(df_excel)
    
    # df_excel = pd.read_excel(r"path_file_excel_get")
    

    # check_db = Table_members.objects.all().exists() #จะได้ค่า true/false เท่านั้น
    # if check_db == False:
    #     save_Table_members(df_excel)
    #     json_records = db_item_master.reset_index().to_json(orient='records')
    #     data_loads = json.loads(json_records)
    #     ajax_save_member_excel_to_database = dumps(data_loads)
    #     return HttpResponse(ajax_save_member_excel_to_database)

    # else:
    #     db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
    #     db_item_master["exists_data"] = "YES"
    #     # print(db_item_master.columns)
        
    #     df_merge_data = pd.merge(df_excel,db_item_master,how="left",on=["member_id"])
    #     df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
        
    #     df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
    #     df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
    #     if len(df_merge_data_save) > 0 :
    #         #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
    #         df_merge_data_save.rename({"description_EN_x":"description_EN" , "description_TH_x":"description_TH" , "waste_group_code_x":"waste_group_code" },axis=1 , inplace=True)
    #         save_Table_members(df_merge_data_save)
    #         # print("df_merge_data_save")
    #     if len(df_merge_data_update) > 0 :
    #         update_member_list(df_merge_data_update)
    #         #convert to Json
    #         json_records = db_item_master.reset_index().to_json(orient='records')
    #         data_loads = json.loads(json_records)
    #         ajax_save_member_excel_to_database = dumps(data_loads)
    #         return HttpResponse(ajax_save_member_excel_to_database)


@csrf_exempt
def delete_member_in_datebase(request):
    member_id_delete = request.POST['item_delete']
    print(member_id_delete)
    Table_members.objects.filter(member_id=member_id_delete).delete()
    
    db_item_master = pd.DataFrame(list(Table_members.objects.all().values()))
    json_records = db_item_master.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)
    ajax_delete_member_in_datebase = dumps(data_loads)
    return HttpResponse(ajax_delete_member_in_datebase )

@csrf_exempt
def edit_member_in_datebase(request):
    member_id_edit = request.POST['item_edit']
    print(member_id_edit)

    df_name_result = pd.DataFrame(list(Table_members.objects.filter(member_id=member_id_edit).values()))  

    json_records = df_name_result.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)

    ajax_edit_member_in_datebase = dumps(data_loads)
    return HttpResponse(ajax_edit_member_in_datebase)

@csrf_exempt
def page_login_programming(request):
    user_get = request.POST['item_user']
    print(user_get)

    df_data_result = pd.DataFrame(list(Table_login.objects.filter(user_login=user_get).values()))
    # print(df_data_result)

    json_records = df_data_result.reset_index().to_json(orient='records')
    print(df_data_result)
    data_loads = json.loads(json_records)

    ajax_page_login = dumps(data_loads)
    return HttpResponse(ajax_page_login)

@csrf_exempt
def selection_values(request):
    db_item_master = pd.DataFrame(list(Table_login.objects.all().values()))
    json_records = db_item_master.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)

    ajax_selection_values = dumps(data_loads)
    return HttpResponse(ajax_selection_values)