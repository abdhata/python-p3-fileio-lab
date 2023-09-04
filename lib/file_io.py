def write_file(file_name="lib/employees", file_content="employee1: Abdi Hassan - Software Engineer"):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as employee :
        employee.write(f'{file_content}')
        pass

def append_file(file_name="lib/employees", append_content="employee2: Amalito - CTO"):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as employee:
        employee.write(f'{append_content}') 

def read_file(file_name="lib/employees"):
    with open(f'{file_name}.txt', encoding='utf-8') as employee:
         return employee.read()
