from .models import Table_members
from datetime import datetime

def save_Table_members(df_excel):
    # datetime_save = datetime.now()
    # date_save = datetime_save.date()
    # time_save = datetime_save.time()
    # datesave = date_save.strftime("%d/%m/%y")
    # timesave = time_save.strftime("%H:%M")
    # datetimesave = str(datesave) + " " + str(timesave)
    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        mem_name = i.member_name
        mem_surname = i.member_surname
        mem_id = i.member_id
        print(mem_id, mem_name, mem_surname)
        db_save = Table_members()
        db_save.member_name = mem_name
        db_save.member_surname = mem_surname
        db_save.member_id = mem_id
        db_save.save()
        print("Save completed" , mem_id, mem_name, mem_surname)

def save_data_to_database_from_page(request):
    member_id_dt = request.POST['dt_member_id']
    member_name_dt = request.POST['dt_member_name']
    member_surname_dt = request.POST['dt_member_surname']
    
    # print(member_id_dt, member_name_dt, member_surname_dt)
    db_save = Table_members()
    db_save.member_id = member_id_dt
    db_save.member_name = member_name_dt
    db_save.member_surname= member_surname_dt
    db_save.save()


#Function update database > update_waste_item_master_list
def update_member_list(df_update):
    # datetime_save = datetime.now()
    # date_save = datetime_save.date()
    # time_save = datetime_save.time()
    # datesave = date_save.strftime("%d/%m/%y")
    # timesave = time_save.strftime("%H:%M")
    # datetimesave = str(datesave) + " " + str(timesave)
    # print(df_update.columns)
    for i in df_update.itertuples(index=False):
        mem_name_update = i.member_name_x
        mem_surname_update = i.member_surname_x
        mem_id_update = i.member_id
        # print("Test update")
        Table_members.objects.filter(member_id=mem_id_update).update(
            member_name = mem_name_update,
            member_surname = mem_surname_update
        )

def update_member_list_from_page(request):
    member_id_edit = request.POST['dt_member_id']
    member_name_edit = request.POST['dt_member_name']
    member_surname_edit = request.POST['dt_member_surname']
    Table_members.objects.filter(member_id=member_id_edit).update(
        member_name = member_name_edit,
        member_surname = member_surname_edit
    )