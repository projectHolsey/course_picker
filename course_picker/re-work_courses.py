import os

file_2 = open("course_list2.csv", "x")

dir_path = os.path.dirname(os.path.realpath(__file__))

new_cotent = ""
with open(dir_path + '/course_list.csv', encoding='utf8') as f:
    x = f.readlines()
    for line in x:
        if "\"" in line:
            new_line = line.split("\"")

            my_teacher = new_line[1]
            if ";" in new_line[1]:
                print(my_teacher)
                teachers = new_line[1].split(";")
                end = ""
                for c_teacher in teachers:
                    try:
                        end += "{1} {0}".format(c_teacher[:c_teacher.index(",")], c_teacher[c_teacher.index(",") + 1:])
                        end = end.replace("  ", " ")
                        end += ";"
                    except:
                        end += c_teacher
                if ";" is end[:-1]:
                    end = end[:-1]
            else:
                new_line[1] = "{1} {0}".format(my_teacher[:my_teacher.index(",")], my_teacher[my_teacher.index(",") + 1:])

            for item in new_line:
                new_cotent += item


file_2.write(new_cotent)

