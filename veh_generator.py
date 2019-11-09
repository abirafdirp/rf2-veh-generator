import csv
import os
import shutil


with open('ngtr_00.veh') as f:
    base_veh = f.read()

drivers_data_csv = open('seeded_a.csv')
csv_reader = csv.DictReader(drivers_data_csv)

if not os.path.exists('output'):
    os.mkdir('output')

if os.path.exists('input/guest_alt.dds'):
    has_guest_dds = True
    print('guest dds detected, guest drivers will use it')
else:
    has_guest_dds = False
    print('guest dds not detected, if there is any guest drivers, it will be skipped')  # noqa

input_dir = os.fsencode('input')


skin_file_metadata = {}
for file in os.listdir(input_dir):
    file_name_with_ext = os.fsdecode(file)
    file_ext = file_name_with_ext.split('.')[-1]
    if file_ext not in ('mas', 'dds'):
        continue

    file_name = file_name_with_ext.split('.')[0]

    # must follow this format xx_alt.dds
    car_number = file_name.split('_')[1]

    # there will be 'guest' as car number
    skin_file_metadata[car_number] = {
        'file_name': file_name,
        'file_name_with_ext': file_name_with_ext,
        'file_ext': file_ext
    }

for position, line in enumerate(csv_reader):
    number_in_csv = line['NUMBER']

    # if number_in_csv not in skin_file_metadata:
    #     print(f'car number {number_in_csv} present in CSV but does not have DDS file')  # noqa
    #     continue

    # is_guest_in_data = True if line.get('GUEST', '') != '' else False
    #
    # if is_guest_in_data and not has_guest_dds:
    #     print(f'car number {number_in_csv} is guest, but you do not have guest_alt.dds file present')  # noqa
    #     continue

    name_in_data = line['NAME']
    # team_in_csv = line['TEAM']
    class_in_csv = line['CLASS']

    file_name = f'alt_{number_in_csv}'
    file_name_with_ext = f'alt_{number_in_csv}.dds'

    with open(f'output/{file_name}.VEH', 'w+') as f:
        veh = base_veh.replace('{NAME}', name_in_data)
        # veh = veh.replace('{TEAM}', team_in_csv)
        veh = veh.replace('{CLASS}', class_in_csv)
        veh = veh.replace('{NUMBER}', number_in_csv)

        # if is_guest_in_data:
        #     veh = veh.replace('{SKIN_FILE}', 'guest_alt.dds')
        # else:
        veh = veh.replace('{SKIN_FILE}', file_name_with_ext)

        f.write(veh)
        # shutil.copy(f'input/{file_name_with_ext}', f'output/{file_name_with_ext}')  # noqa
        # print(f'{file_name} VEH generated')

drivers_data_csv.close()
