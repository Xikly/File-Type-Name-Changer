import os

def main(looped):
    while True:
        if looped is True:
            print('\n##############\nLETS GO AGAIN!\n##############\n')

        folder = input('Directory: ')
        type_name = input('File type to replace: ').lower()
        new_type = input('New type: ').lower()

        changed = 0
        failed = 0

        print("\n")

        for filename in os.listdir(folder):
            try:
                infilename = os.path.join(folder,filename)
                if not os.path.isfile(infilename): continue
                oldbase = os.path.splitext(filename)
                
                if oldbase[1] == f".{type_name}":
                    newname = infilename.replace(f'.{type_name}', f'.{new_type}')
                    output = os.rename(infilename, newname)
                    changed = changed + 1
                    print(f"TYPE CHANGED ::: [{oldbase[0]}.{type_name}] -> [{oldbase[0]}.{new_type}]")
            except:
                failed = failed + 1
                print(f"TYPE CHANGE FAILED ::: [{oldbase[0]}.{type_name}] -> [{oldbase[0]}.{new_type}]")

        print(f"\n{changed} FILE TYPES CHANGED\n{failed} FILE TYPE CHANGE FAILS")
        looped = True

main(looped = False)