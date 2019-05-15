import subprocess

folder_names = ["2019/intro_to_QGIS/","2019/md_to_html/"]
#"2019/housing-affordability/","2019/intro_to_GIS_1/"

for folder_name in folder_names:

    # run generate-md to conver the md file to github-like html
    subprocess.call(['generate-md', '--layout github', '--input', folder_name + 'md', '--output', folder_name + '/html'])

    # copy in the main.css file
    subprocess.call(['cp', 'main.css', folder_name + 'html/assets/css/main.css'])

    # add in the extra html to the top of the generated index.html
    addhtml = open("add.html","r")
    out_html = ""
    for row in addhtml:
        if row != "":
            out_html = out_html + row
    addhtml.close()
    mainhtml = open(folder_name + '/html/index.html',"r")
    flag = 0
    for row in mainhtml:
        if flag == 1 and row != "":
            out_html += row
        if "<body>" in row:
            flag = 1
    mainhtml.close()
    finalhtml = open(folder_name + '/html/index.html', "w")
    finalhtml.write(out_html)
    finalhtml.close()
    print("meow")
