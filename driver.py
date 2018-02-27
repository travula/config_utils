from config import my_dict
from arg_parse import main

def change_config():
    my_dict['a'] = 2

def m_run():
    change_config()
    main()

if __name__ == '__main__':
    m_run()
    
    
    
