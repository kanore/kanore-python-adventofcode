import directory as d

import splitter as s

def sumDir(entry, maxVal):
    print("DIR",len(entry))

    directories = []
    directories.append(d.Directory())

    level = 0
    for dir in entry:
        lines = s.splitBy(dir, """
""")
        for line in lines:
            code = s.splitBy(line, " ")
            print("Code",code,len(code))
            
            # each code line
            if len(code) == 3:
                # cd line call
                print("cd line call")
                if code[2] == "..":
                    level -= 1
                else:
                    level += 1

            elif len(code) == 2:
                # folder or file
                print("folder or file")
                size = 0
                if code[0] != "dir":
                    size = code[0]

                if size == 0:
                    calcDirSize()
                directories.append(d.Directory(level, code[1], size))
            else:
                # error
                eq = "="*20
                print(eq,"ERROR",eq)

        
        print("Length",len(lines))

    print(len(directories))
