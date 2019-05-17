import csv
import os
import shutil


with open('base.VEH') as f:
    base_veh = f.read()

drivers_data_csv = open('data.csv')
csv_reader = csv.DictReader(drivers_data_csv)

if not os.path.exists('output'):
    os.mkdir('output')

if os.path.exists('input/guest_alt.dds'):
    print('guest dds detected, guest drivers will use it')
else:
    print('guest dds not detected, if there is any guest drivers, it will be skipped')  # noqa

input_dir = os.fsencode('input')


dds_data = {}
for file in os.listdir(input_dir):
    file_name_with_ext = os.fsdecode(file)

    if not file_name_with_ext.endswith('.dds'):
        continue

    file_name = file_name_with_ext.split('.')[0]

    # must follow this format xx_alt.dds
    car_number = file_name.split('_')[0]

    # there will be 'guest' as car number
    dds_data[car_number] = {
        'file_name': file_name,
        'file_name_with_ext': file_name_with_ext
    }

drivers_data = {}
for position, line in enumerate(csv_reader):
    if position == 1:
        continue

    number_in_csv = line['NUMBER']

    if number_in_csv not in dds_data:
        print(f'car number {number_in_csv} present in CSV but does not have DDS file')  # noqa
        continue

    is_guest_in_data = True if line['GUEST'] != '' else False

    name_in_data = line['NAME']
    team_in_csv = line['TEAM']
    class_in_csv = line['CLASS']

    file_name = dds_data[number_in_csv]['file_name']
    file_name_with_ext = dds_data[number_in_csv]['file_name_with_ext']

    with open(f'output/{file_name}.VEH', 'w+') as f:
        veh = base_veh.replace('{NAME}', name_in_data)
        veh = veh.replace('{TEAM}', team_in_csv)
        veh = veh.replace('{CLASS}', class_in_csv)
        veh = veh.replace('{NUMBER}', number_in_csv)

        if is_guest_in_data:
            veh = veh.replace('{DDS}', 'guest_alt.dds')
        else:
            veh = veh.replace('{DDS}', f'{number_in_csv}_alt.dds')

        f.write(veh)
        shutil.copy(f'input/{file_name_with_ext}', f'output/{file_name_with_ext}')  # noqa
        print(f'{file_name} VEH generated')

drivers_data_csv.close()
