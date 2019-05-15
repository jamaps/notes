
![header](h.png)

## Markdown to HTML

What's the goal here? To take something I write in markdown `.md` and convert it into a clean `.html` page (like this page!). Things I want to convert sometimes in include

- Blobs of text, sometimes in paragraph form
- Headings and sub-headings
- Math Formulas
- Stylized Code Blocks
- Links to places on the internet
- Embedded Images
- Lists

To start, set up a project folder like so.

```sh
├── 2019
│   └── md_to_html
│       ├── html
│       └── md
│           └── index.md
├── main.css
├── render.py
├── add.html
```

Where `index.md` is where I write in glorious markdown. The sub-sub-folder `html` is where we will build the output. Don't worry about the other files for now.


My starting point for this is [markdown-styles](https://github.com/mixu/markdown-styles). At a simple level, this tool converts `.md` to `.html` as follows (but click on the link to the project for more detail)

```sh
generate-md --layout github --input ./md --output ./html
```

This provides a good basis. It already renders lists, sets up proper links, and loads in images no problem (images default to the body width if they have a greater pixel width). It also provides code blocks, stylized using the default GitHub template. Still needs some additions.

### Adding Custom CSS

To do so, I set up a folder called `main.css` with the tweaks that I want. This is added to the project folder.

When the `generate-md` command runs, it sets up a folder called `assets/` in `html/`. Then, I copy `main.css` into this folder.

```sh
cp main.css /2019/html/assets/css/main.css
```

However, the HTML file still needs to be updated to include reference to `main.css`. Can copy this into the header of the HTML file.

```html
<link type="text/css" rel="stylesheet" href="assets/css/main.css">
```

### Adding Formulas

Next, I also want to occasionally write some math formulas, either inline, %%u = 42%%, or on their own line like so

$$Y = \alpha + \beta X + \epsilon $$

To do this, I'll make use of the handy tool [MathJax](https://www.mathjax.org/) which can take math written in `.tex` and render it as pretty formulas. To get this working, copy the following into the HTML header.

```html
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {
  inlineMath: [ ["%%","%%"] ],
  processEscapes: true
}
});
</script>
<script type="text/javascript" async
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async>
</script>
```

### Automation

It's a little annoying to copy this extra HTML every single time I want to render a page. So let's combine everything into a single python script, which takes the sub-folder name, in this case `md_to_html` as an input, and renders everything in one swoop.

```python
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

# combine the extra html to the top of the generated index.html
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
```

---

:)
