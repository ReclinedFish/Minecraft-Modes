import get_modslist_mcmod as gml_mcmod
import get_transurl_curseforge as gtu_cf
import check_dict_empty
from tkinter import messagebox, ttk, filedialog, END
from tkinter import Tk, Label, Entry, Button, Text
from pandas import DataFrame, merge
from re import match


def get_nameurl_dict_mods(*args):
    """
    Get the names and their urls of all mods in a mod package,
    and copy the nameurl_dict_mods in a global variable called new_nameurl_dict_mods

    获取 整合包中所有 mod 的名称和它们的 url，
    并将 nameurl_dict_mods 复制到名为 new_nameurl_dict_mods 的全局变量中

    :param args: binding keyboard shortcuts, use *args or **kwargs or event=None
                绑定键盘快捷键的时候，tkinter的bind函数会自动传入一个参数event,
                get_nameurl_dict_mods()函数需要参数，*args或**kwargs或event=None，接受这个event
    :return:
    """
    global nameurl_dict_mods

    url_mcmodpack_basic = "https://www.mcmod.cn/modpack"
    # 获取用户输入modpack num | get user input modpack num
    this_modpack = this_modpack_entry.get()
    url_mcmod_basic = "https://www.mcmod.cn"
    is_url_exist = url_mcmodpack_basic + '/' + this_modpack + '.html'

    # 每次执行 get_nameurl_dict_mods 时都需要清空output_text, | clear the content in output_text
    # (1.0, END)指的是第1行第0个字符到最后一个字符的所有内容。
    output_text.delete(1.0, END)
    output_text.insert(END, 'Input URL is:' + is_url_exist + '\n')

    # 调用 gml_mcmod.get_htmltext_mcmod 函数获取网页的 html 文本 |
    # use get_htmltext_mcmod function to get the html text of the web page
    html_str_modpack, *error = gml_mcmod.get_htmltext_mcmod(is_url_exist)

    if html_str_modpack is not None:
        # 如果获取成功，则调用get_urlname_mcmod函数获取 mods names 和 urls 字典 |
        # If the acquisition is successful, use get_urlname_mcmod function to obtain the mods names and urls dictionary
        nameurl_dict_mods = gml_mcmod.get_urlname_mcmod(html_str_modpack, url_mcmod_basic)

        # 将 nameurl_dict_mods 复制到名为 new_nameurl_dict_mods 的全局变量中
        # copy the nameurl_dict_mods in a global variable called new_nameurl_dict_mods
        global new_nameurl_dict_mods
        new_nameurl_dict_mods = nameurl_dict_mods.copy()

        # messagebox信息显示 | messagebox show information
        messagebox.showinfo("Info", "nameurl_dict_mods obtained!\nPlease click 2--Download Mods Name And MCMOD Urls.")
        output_text.insert(END, '\nThe first 5 keys of nameurl_dict_mods are :\n'
                           + "\n".join(map(str, list(nameurl_dict_mods.keys())[:5])))
        output_text.insert(END, '\n\nThe length of nameurl_dict_mods is: '
                           + str(len(nameurl_dict_mods)))
    elif error:
        output_text.insert(END, *error)
        messagebox.showerror("Error", "Please see the error message in the text box!")
    # else:
    #     messagebox.showerror("Error", "The webpage\n" + is_url_exist + "\ndoesn't exist!\n")


def trans_nameurl_dict_mods(*args):
    """
    convert the urls(value) in nameurl_dict_mods to CurseForge urls,
    save the updated global variable called nameurl_dict_mods

    nameurl_dict_mods中的所有 mod 的urls接(value值)转化为 CurseForge上的 urls，
    并将更新后的字典存入全局变量 nameurl_dict_mods 中

    :param args: binding keyboard shortcuts
    :return:
    """

    # 进度条的初始值设置为0，最大值设置为 nameurl_dict_mods 的长度 |
    # the progress bar`s initial value is 0, the maximum value is the length of nameurl_dict_mods
    global stop_flag
    if not forge_fabric_others_str:
        output_text.insert(END, '\n\nPlease select: \nA--Forge\nB--Fabric\n'
                                'C--GitHub\nD--MCBBS\nE--Others\n')
        messagebox.showinfo("Info", "And then click 3--Transform Url")
        return
    else:
        output_text.insert(END, '\n\nYou have selected: {}\n'.format(forge_fabric_others_str))
        output_text.insert(END, '\nTransforming...\n')

    progress['value'] = 0
    progress['maximum'] = len(nameurl_dict_mods)

    # 用 i 和 enumerate()，返回循环的键值对列表和其下标 |
    # using i and enumerate(), returns a list of key-value pairs and their subscripts
    for i, (key_name, value_url) in enumerate(new_nameurl_dict_mods.items()):
        # 根据modpack列表中value值，获取每个mod对应的介绍网页的HTML，提取HTML字符串中的 curseforge url，更新 nameurl_dict_mods |
        # according to the value in the nameurl_dict_mods, get each mod`s HTML of the introduction page,
        # and get the curseforge url in the HTML string, update nameurl_dict_mods
        if stop_flag:
            break

        try:
            html_str_mcmod, *error = gml_mcmod.get_htmltext_mcmod(value_url)
            transurl_str = gtu_cf.get_curseforgeurl_mcmod(html_str_mcmod, forge_fabric_others_str)
            nameurl_dict_mods[key_name] = transurl_str

            progress['value'] = i + 1
            output_text.insert(END, 'Transforming: {} \n'.format(key_name))
            output_text.see(END)  # output_text输出内容滑动到最后一行 | output_text slides to the last line
            root.update()  # 更新output_text界面 | update the output_text interface

        except Exception as e:
            output_text.insert(END, f'Error occurred: {e}\n')
            messagebox.showinfo("Error", "Please click 1--Submit Number first")
            return

    if not stop_flag:
        output_text.insert(END, '\nTransformation completed!')
        output_text.see(END)
        messagebox.showinfo("Info", "nameurl_dict_mods transformed!\n"
                                    "Please click 4--Download Mods Name And CurseForge Urls button to download excel")
    else:
        stop_flag = not stop_flag
        messagebox.showinfo("Info", "Please click 3--Transform Url button to transform again")
        output_text.insert(END, '\nTransformation uncompleted!')
        output_text.see(END)


def is_nameurl_dict_mods_enmpty(my_dict):
    """
    判断列表value值是否为空 | whether the value of this list is empty
    :param my_dict:
    :return:
    """

    # 列表的value值，output_text输出value是空的个数，和是空的key值 |
    # the value of the list, output the number of empty value, and output corresponding key in the output_text
    emptykeys_list_mods, emptyvalues_num_mods = check_dict_empty.empty_values(my_dict)
    output_text.insert(END, "\n\nThe number of empty values is: {}\n\n".format(emptyvalues_num_mods))

    if emptykeys_list_mods:
        root.update()
        emptykeys_str = "\n".join(emptykeys_list_mods)
        output_text.insert(END, emptykeys_str)
        output_text.see(END)


def download_nameurl_dict_mods(*args):
    """
    convert the dictionary nameurl_dict_mods to excel and download |
    将字典 nameurl_dict_mods转换成excel，并下载

    :param args:
    :return:
    """
    # 弹出文件夹选择对话框，让用户选择一个文件夹 | a folder selection dialog box pops up, allowing the user to select a folder
    path = filedialog.askdirectory()
    if path:
        df = DataFrame(list(new_nameurl_dict_mods.items()), columns=['Name', 'Original URL'])
        modpack_number = this_modpack_entry.get()
        df.to_excel(path + ('\\nameurl_dict_mods_' + modpack_number + '.xlsx'), index=False)
        messagebox.showinfo("Info", "nameurl_dict_mods downloaded!")
        is_nameurl_dict_mods_enmpty(new_nameurl_dict_mods)


def download_trans_nameurl_dict_mods(*args):
    """
    convert the dictionary trans_nameurl_dict_mods to excel and download |
    将字典trans_nameurl_dict_mods转换成excel，并下载

    :param args:
    :return:
    """
    path = filedialog.askdirectory()
    if path:
        df = DataFrame(list(nameurl_dict_mods.items()), columns=['Name', 'Transformed URL'])
        modpack_number = this_modpack_entry.get()
        df.to_excel(path + '\\trans_nameurl_dict_mods_' + modpack_number +
                    '_' + forge_fabric_others_str + '.xlsx', index=False)
        messagebox.showinfo("Info", "trans_nameurl_dict_mods downloaded!")
        is_nameurl_dict_mods_enmpty(nameurl_dict_mods)


def download_integrate_nameurl_dict_mods(*args):
    """
    merge the data in new_nameurl_dict_mods and nameurl_dict_mods and save it as excel |
    将new_nameurl_dict_mods和nameurl_dict_mods中的数据合并，并保存为excel文件

    :param args:
    :return:
    """

    df1 = DataFrame.from_dict(new_nameurl_dict_mods, orient='index', columns=['Original URL'])
    df1.reset_index(inplace=True)
    df1.columns = ['Name', 'Original URL']

    df2 = DataFrame.from_dict(nameurl_dict_mods, orient='index', columns=['Transformed URL'])
    df2.reset_index(inplace=True)
    df2.columns = ['Name', 'Transformed URL']
    df = merge(df1, df2, on='Name')

    path = filedialog.askdirectory()
    if path:
        modpack_number = this_modpack_entry.get()
        df.to_excel(path + '\\integrate_nameurl_dict_mods_' + modpack_number +
                    '_' + forge_fabric_others_str + '.xlsx', index=False)
        messagebox.showinfo("Info", "integrate_nameurl_dict_mods downloaded!")


if __name__ == '__main__':
    nameurl_dict_mods = {}
    new_nameurl_dict_mods = {}
    forge_fabric_others_str = ""
    stop_flag = False

    root = Tk()
    root.title("Modpack mods` urls excels downloader from https://www.mcmod.cn/")

    # this_modpack_label
    this_modpack_label = Label(root, text="Enter the modpack number: \n"
                                          "例如https://www.mcmod.cn/modpack/253.html的253")
    this_modpack_label.grid(row=0, column=0, sticky='w')

    # this_modpack_entry
    this_modpack_entry = Entry(root, width=40, validate="key")
    this_modpack_entry.grid(row=0, column=1, sticky='e')
    this_modpack_entry.bind('<Return>', lambda event: submit_button.invoke())

    def clear_placeholder(event):
        if this_modpack_entry.get() == "Enter modpack num":
            this_modpack_entry.delete(0, END)
            this_modpack_entry.config(fg="black")

    def set_placeholder(event):
        if not this_modpack_entry.get():
            this_modpack_entry.insert(0, "Enter modpack num")
            this_modpack_entry.config(fg="gray")

    # 设置提示文本 | set info text
    this_modpack_entry.insert(0, "Enter modpack num")
    this_modpack_entry.config(fg='gray')
    # 绑定事件 | bind event
    this_modpack_entry.bind("<FocusIn>", clear_placeholder)
    this_modpack_entry.bind("<FocusOut>", set_placeholder)

    # 只允许数字输入 | Only numeric input allowed
    def validate(letter):
        if match(r"^\d+$", letter) or letter == "":
            return True
        else:
            return False

    this_modpack_entry.config(validatecommand=(this_modpack_entry.register(validate), "%P"))

    # clear_button
    def clear_text(*args):
        output_text.delete("1.0", END)

    clear_button = Button(root, text="C--Clear", command=clear_text, width=10)
    clear_button.grid(row=2, column=0, sticky='w')
    root.bind("<C>", clear_text)
    clear_button.bind("<Enter>", lambda event: clear_button.config(text='Press C to clear',
                                                                   fg='red',
                                                                   font=("Times New Roman", 9, "bold italic")))
    clear_button.bind("<Leave>", lambda event: clear_button.config(text='C--Clear',
                                                                   fg='black',
                                                                   font=("Arial", 9, "normal")))

    # exit_button
    def exit_confirm(*args):
        result = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
        if result:
            root.destroy()
        else:
            pass

    exit_button = Button(root, text="E--Exit", command=exit_confirm, width=10)
    exit_button.grid(row=3, column=0, sticky='w')
    root.bind("<E>", exit_confirm)
    exit_button.bind("<Enter>", lambda event: exit_button.config(text='Press E to exit',
                                                                 fg='red',
                                                                 font=("Times New Roman", 9, "bold italic")))
    exit_button.bind("<Leave>", lambda event: exit_button.config(text='E--Exit',
                                                                 fg='black',
                                                                 font=("Arial", 9, "normal")))

    # forge_button, fabric_button, github_button, mcbbs_button, others_button
    def get_forge_fabric_others_str(button_type):
        global forge_fabric_others_str
        if nameurl_dict_mods and (button_type == "forge"):
            forge_fabric_others_str = "forge"

        elif nameurl_dict_mods and (button_type == "fabric"):
            forge_fabric_others_str = "fabric"

        elif nameurl_dict_mods and (button_type == "github"):
            forge_fabric_others_str = "GitHub"

        elif nameurl_dict_mods and (button_type == "mcbbs"):
            forge_fabric_others_str = "MCBBS"

        elif nameurl_dict_mods and (button_type == "others"):
            forge_fabric_others_str = "Others"
        return forge_fabric_others_str


    # forge_button
    forge_button = Button(root, text="A--Forge", command=lambda: get_forge_fabric_others_str("forge"), width=12)
    forge_button.grid(row=1, column=0, sticky='w')
    root.bind("<A>", lambda event: get_forge_fabric_others_str("forge"))
    forge_button.bind("<Enter>", lambda event: forge_button.config(text='Press A for forge',
                                                                   fg='red',
                                                                   font=("Times New Roman", 9, "bold italic")))
    forge_button.bind("<Leave>", lambda event: forge_button.config(text='A--Forge',
                                                                   fg='black',
                                                                   font=("Arial", 9, "normal")))

    # fabric_button
    fabric_button = Button(root, text="F--Fabric", command=lambda: get_forge_fabric_others_str("fabric"), width=12)
    fabric_button.grid(row=1, column=0)
    root.bind("<F>", lambda event: get_forge_fabric_others_str("fabric"))
    fabric_button.bind("<Enter>", lambda event: fabric_button.config(text='Press F for fabric',
                                                                     fg='red',
                                                                     font=("Times New Roman", 9, "bold italic")))
    fabric_button.bind("<Leave>", lambda event: fabric_button.config(text='F--Fabric',
                                                                     fg='black',
                                                                     font=("Arial", 9, "normal")))

    # github_button
    github_button = Button(root, text="G--GitHub", command=lambda: get_forge_fabric_others_str("github"), width=12)
    github_button.grid(row=1, column=0, sticky='e')
    root.bind("<G>", lambda event: get_forge_fabric_others_str("github"))
    github_button.bind("<Enter>", lambda event: github_button.config(text='Press G for github',
                                                                     fg='red',
                                                                     font=("Times New Roman", 9, "bold italic")))
    github_button.bind("<Leave>", lambda event: github_button.config(text='G--GitHub',
                                                                     fg='black',
                                                                     font=("Arial", 9, "normal")))

    # mcbbs_button
    mcbbs_button = Button(root, text="M--MCBBS", command=lambda: get_forge_fabric_others_str("mcbbs"), width=12)
    mcbbs_button.grid(row=1, column=1, sticky='w')
    root.bind("<M>", lambda event: get_forge_fabric_others_str("mcbbs"))
    mcbbs_button.bind("<Enter>", lambda event: mcbbs_button.config(text='Press M for mcbbs',
                                                                   fg='red',
                                                                   font=("Times New Roman", 9, "bold italic")))
    mcbbs_button.bind("<Leave>", lambda event: mcbbs_button.config(text='M--MCBBS',
                                                                   fg='black',
                                                                   font=("Arial", 9, "normal")))

    # others_button
    others_button = Button(root, text="O--Others", command=lambda: get_forge_fabric_others_str("others"), width=12)
    others_button.grid(row=1, column=1)
    root.bind("<O>", lambda event: get_forge_fabric_others_str("others"))
    others_button.bind("<Enter>", lambda event: others_button.config(text='Press O for others',
                                                                     fg='red',
                                                                     font=("Times New Roman", 9, "bold italic")))
    others_button.bind("<Leave>", lambda event: others_button.config(text='O--Others',
                                                                     fg='black',
                                                                     font=("Arial", 9, "normal")))

    # stop_button
    def stop_trans_button(*args):
        global stop_flag
        if stop_flag:
            stop_flag = False
        else:
            stop_flag = True

    stop_button = Button(root, text="S--Stop", command=stop_trans_button, width=10)
    stop_button.grid(row=1, column=1, sticky='e')
    root.bind("<S>", stop_trans_button)
    stop_button.bind("<Enter>", lambda event: stop_button.config(text='Press S to stop',
                                                                 fg='red',
                                                                 font=("Times New Roman", 9, "bold italic")))
    stop_button.bind("<Leave>", lambda event: stop_button.config(text='S--Stop',
                                                                 fg='black',
                                                                 font=("Arial", 9, "normal")))

    # submit_button
    submit_button = Button(root, text="1--Submit Num", command=get_nameurl_dict_mods, width=20)
    submit_button.grid(row=2, column=0, sticky='e')
    root.bind("<F1>", get_nameurl_dict_mods)
    submit_button.bind("<Enter>", lambda event: submit_button.config(text='Press F1 to submit',
                                                                     fg='red',
                                                                     font=("Times New Roman", 9, "bold italic")))
    submit_button.bind("<Leave>", lambda event: submit_button.config(text='1--Submit Num',
                                                                     fg='black',
                                                                     font=("Arial", 9, "normal")))

    # download_button
    download_button = Button(root, text="2--Download Mods Name And MCMOD Urls", command=download_nameurl_dict_mods,
                             width=40)
    download_button.grid(row=2, column=1, sticky='e')
    root.bind("<F2>", download_nameurl_dict_mods)
    download_button.bind("<Enter>", lambda event: download_button.config(text='Press F2 to download',
                                                                         fg='red',
                                                                         font=("Times New Roman", 9, "bold italic")))
    download_button.bind("<Leave>", lambda event: download_button.config(text='2--Download Mods Name And MCMOD Urls',
                                                                         fg='black',
                                                                         font=("Arial", 9, "normal")))

    # trans_button
    trans_button = Button(root, text="3--Transform Url", command=trans_nameurl_dict_mods, width=20)
    trans_button.grid(row=3, column=0, sticky='e')
    root.bind("<F3>", trans_nameurl_dict_mods)
    trans_button.bind("<Enter>", lambda event: trans_button.config(text='Press F3 to trans',
                                                                   fg='red',
                                                                   font=("Times New Roman", 9, "bold italic")))
    trans_button.bind("<Leave>", lambda event: trans_button.config(text='3--Transform Url',
                                                                   fg='black',
                                                                   font=("Arial", 9, "normal")))

    # download_trans_button
    download_trans_button = Button(root, text="4--Download Mods Name And CurseForge Urls",
                                   command=download_trans_nameurl_dict_mods,
                                   width=40)
    download_trans_button.grid(row=3, column=1, sticky='e')
    root.bind("<F4>", download_trans_nameurl_dict_mods)
    download_trans_button.bind("<Enter>", lambda event: download_trans_button.config(text='Press F4 to download',
                                                                                     fg='red',
                                                                                     font=("Times New Roman", 9,
                                                                                           "bold italic")))
    download_trans_button.bind("<Leave>",
                               lambda event: download_trans_button.config(
                                   text='4--Download Mods Name And CurseForge Urls',
                                   fg='black',
                                   font=("Arial", 9, "normal")))

    # download_integrate_button
    download_integrate_button = Button(root, text="5--Download integrate Mods Name And Url",
                                       command=download_integrate_nameurl_dict_mods,
                                       width=80)
    download_integrate_button.grid(row=5, column=0, columnspan=2)
    root.bind("<F5>", download_integrate_nameurl_dict_mods)
    download_integrate_button.bind("<Enter>",
                                   lambda event: download_integrate_button.config(text='Press F5 to download',
                                                                                  fg='red',
                                                                                  font=(
                                                                                      "Times New Roman", 9,
                                                                                      "bold italic")))
    download_integrate_button.bind("<Leave>",
                                   lambda event: download_integrate_button.config(
                                       text='5--Download integrate Mods Name And Url',
                                       fg='black',
                                       font=("Arial", 9, "normal")))

    # progress
    progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
    progress.grid(row=4, column=0, columnspan=2)

    # output_text
    output_text = Text(root)
    output_text.grid(row=6, column=0, columnspan=2)

    # info_label
    info_label = Label(root, text="Please follow the button order(1->2->3->4->5) and info!")
    info_label.grid(row=7, column=0, columnspan=2)

    root.mainloop()
