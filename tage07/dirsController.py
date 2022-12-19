import directory as d

import splitter as s

def savingDirs(entry):
    directories = []

    level = 0
    father = "/"
    for dir in entry:
        lines = s.splitBy(dir, """\n""")
        for line in lines:
            code = s.splitBy(line, " ")
            print("Code",code,len(code))
            
            # each code line
            if len(code) == 3:
                # cd line call
                if code[2] == "..":
                    level -= 1
                else:
                    level += 1
                    father = code[2]

            elif len(code) == 2:
                # folder or file
                size = 0
                if code[0] != "dir":
                    # file
                    size = code[0]

                # if size == 0:
                #     calcDirSize()
                directories.append(d.Directory(level, code[1], size, father))
        
        print("Length",len(lines))

    return directories
