




def read_file(path, project_id):
    complete_path= path + project_id
    part=1
    guard=True
    lib_list = []
    while(guard):
        try:
            with open(complete_path +'-part'+str(part)+'.c',"r") as file:
                for row in file:
                    if(str(row).startswith('#include')):
                        s = row.split('//')
                        s = s[0]
                        s = s.split('/*')
                        s = s[0]
                        s = s.strip()
                        #print(str(s))
                        lib_list.append(s)
            part = part + 1
        except OSError as e:
            guard = False
            #print('Project code total part:',part-1)
    #print(lib_list)
    return lib_list

#def file_finder():
#    path='.\\code-snippet\\0a38e0a4-10e9-4ca3-8316-a7cc2f73ccc0-part1.c'
#try:
#    path=''
#    read_file(path)
#except ValueError:
#    print("Errore!!!")
#finally:
#    print('finally')

read_file('C:\\progetti\\low-code-ard-proj\\data-scraper\\code-snippets\\','d019068e-d0ca-4db7-858e-2b9013baa305')
#read_file('C:\\progetti\\low-code-ard-proj\\data-scraper\\code-snippets\\','0a38e0a4-10e9-4ca3-8316-a7cc2f73ccc0')
#read_file('C:\\progetti\\low-code-ard-proj\\data-scraper\\code-snippets\\0a38e0a4-10e9-4ca3-8316-a7cc2f73ccc0-part1.c')