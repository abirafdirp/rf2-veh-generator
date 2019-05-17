import csv
import os
import shutil


with open('base.VEH') as f:
    base_veh = f.read()

drivers_data = open('data.csv')
csv_reader = csv.DictReader(drivers_data)

if os.path.exists('input/guest_alt.dds'):
    print('guest dds detected, guest drivers will use it')
else:
    print('guest dds not detected, if there is any guest drivers, it will be skipped')  # noqa

input_dir = os.fsencode('input')

for file in os.listdir(input_dir):
    file_name_with_ext = os.fsdecode(file)

    if not file_name_with_ext.endswith('.dds'):
        print(f'invalid file present in input directory: {file_name_with_ext}')
        continue

    file_name = file_name_with_ext.split('.')[0]

    # must follow this format xx_alt.dds
    car_number = file_name.split('_')[0]
    is_guest = True if car_number == 'guest' else False
    if not car_number.isdigit() and not is_guest:
        print(
            f'invalid dds file name_in_data format, must be xx_alt.dds: '
            f'{file_name_with_ext}'
        )
        continue

    for position, line in enumerate(csv_reader):
        if position == 1:
            continue

        number_in_data = line['NUMBER']
        if not number_in_data == car_number:
            continue

        is_guest_in_data = True if line['GUEST'] != '' else False
        name_in_data = line['NAME']
        team_in_data = line['TEAM']
        class_in_data = line['CLASS']

        with open(f'output/{file_name}.VEH', 'w+') as f:
            veh = base_veh.replace('{NAME}', name_in_data)
            veh = veh.replace('{TEAM}', team_in_data)
            veh = veh.replace('{CLASS}', class_in_data)
            veh = veh.replace('{NUMBER}', number_in_data)

            if is_guest_in_data:
                veh = veh.replace('{DDS}', 'guest_alt.dds')
            else:
                veh = veh.replace('{DDS}', f'{car_number}_alt.dds')

            f.write(veh)
            shutil.copy(f'input/{file_name_with_ext}', f'output/{file_name_with_ext}')  # noqa
            print(f'{file_name} VEH generated')
    drivers_data.seek(0)

drivers_data.close()
