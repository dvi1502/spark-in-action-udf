import runpy
import sys


modules = [
    "./lab200_library_open/openedLibrariesApp.py",
    "./lab210_library_open_sql/openedLibrariesSqlApp.py",
    "./lab900_in_range/inCustomRangeApp.py",
    "./lab910_addition/additionApp.py",
    "./lab911_addition_fail1/additionFail1App.py",
    "./lab920_column_as_parameter/columnAdditionApp.py"
]

if __name__ == '__main__':

    for i,module in enumerate(modules):
        print("{0} {1}".format(i,module))
    print("")

    test_text = input ("Введите вариант : ")
    module_number = int(test_text)

    runpy.run_path(modules[module_number], run_name='__main__')

