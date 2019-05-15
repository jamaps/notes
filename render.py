import subprocess

# input the project name
print("Year: ")
year = input()
print("Name: ")
name = input()
folder_name = year + "/" + name + "/"
print(folder_name)

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
print(out_html)
mainhtml.close()
finalhtml = open(folder_name + '/html/index.html', "w")
finalhtml.write(out_html)
finalhtml.close()

print("meow")
