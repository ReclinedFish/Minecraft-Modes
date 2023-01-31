# Minecraft-Mods-modpack-[MCMOD][]-[CurseForge][]-etc.
[MCMOD]: https://www.mcmod.cn/ 
[CurseForge]: https://www.curseforge.com/minecraft/mc-mods

Minecraft模组整合包的url链接下载器，可下载mod简体中文名称，以及与名称对应url，组成的的excel表格.xlsx文件。

The url link downloader of the Minecraft modpack, which can download the simplified Chinese name of the mod and the corresponding url, which is composed of an excel .xlsx file.


## 简介：| Introduction:

对于mcmod网站，有一个模组整合包（a mod pack），包含很多模组，| For the mcmod website, there is a mod pack, which contains many mods,

每个模组都有自己的下载地址，| Each mod has its own download address,

如果整合包中的模组的数量太多，获取每个模组的下载url很困难，| If there are too many mods in the mod pack, it is difficult to get download URL of each mod,

所以我做了这个下载器。| So I made this downloader.

<img width="452" alt="image" src="https://user-images.githubusercontent.com/123816890/215387011-f63438be-3cd3-4b8b-aa9a-aeeee52d03b4.png">


## 使用场景：| Scenes to be used:

> 例如网址https://www.mcmod.cn/modpack/253.html ，是编号为**253**的整合包的地址，| For example, the website https://www.mcmod.cn/modpack/253.html is the address of the mod pack numbered **253**,

用户可以输入模组包编号**253**，| The user can enter the mod pack number **253**,

![image](https://user-images.githubusercontent.com/123816890/215384985-bcf5b5e6-0361-4ff4-b2a1-0e0a18dafc32.png)

然后，按下 **回车** 或 点击 **按钮1--Submit Num** 或 点击 **快捷键F1**；接着，点击 **按钮2--Download Mods Name And mcmod Url**，可以得到**nameurl_dict_mods_253.xlsx**表格文件，

Then, press **Enter** or click **Button 1--Submit Num** or click **Shortcut Key F1**; and, click **Button 2--Download Mods Name And mcmod Url**, You can get the **nameurl_dict_mods_253.xlsx** file,

![image](https://user-images.githubusercontent.com/123816890/215385084-64caacf3-6d18-4834-9cd1-c06d720af59f.png)

![image](https://user-images.githubusercontent.com/123816890/215384816-e99cc043-2cbb-4b61-b6fc-d54c450298cc.png)

然后，选择所需的mods发布平台，如[CurseForge][]中的Forge或Fabric平台、[MCBBS][]平台、[GitHub][]平台、以及其他Others平台，如[Others](https://www.youtube.com/) [Others](https://www.reddit.com/)平台，点击平台对应的按钮，

[CurseForge]:https://www.curseforge.com/minecraft/mc-mods/

[MCBBS]:https://www.mcbbs.net/

[GitHub]:https://github.com/

Then, select the mods distribution platform, such as **Forge** or **Fabric** platform in **CurseForge**, **MCBBS**, **GitHub**, and **Others**, and click the button corresponding to the platform,

![image](https://user-images.githubusercontent.com/123816890/215386827-87e4d1b4-55a5-41ee-b37f-a59a61a22cb0.png)

然后，用户可以点击**按钮3--Transform Url**，将**MCMOD**平台的**Original URL**，转换成上述平台的**Transformed URL**，接着，点击**按钮4--Download Mods Name And curseforge Url**，可以得到**trans_nameurl_dict_mods_253_forge.xlsx**表格文件，

Then, the user can click the **button 3--Transform Url** to transform the **Original URL** of the **MCMOD** platform into the **Transformed URL** of the above-mentioned platform, and then click the **button 4--Download Mods Name And curseforge Url** to get the **trans_nameurl_dict_mods_253_forge.xlsx** file,

![image](https://user-images.githubusercontent.com/123816890/215398652-efcf9aca-8d22-4cb9-9cac-59b0087a0fc4.png)

![image](https://user-images.githubusercontent.com/123816890/215399037-e31a6afa-f7b1-45dd-8679-0c9c05272d58.png)

最后，用户可以点击**按钮5--Download integrate Mods Name And Url**，下载**integrate_nameurl_dict_mods_253_forge.xlsx**表格文件。

Finally, the user can click the **button 5--Download integrate Mods Name And Url** to download **the integrate_nameurl_dict_mods_253_forge.xlsx** file.

![image](https://user-images.githubusercontent.com/123816890/215400310-532c89d3-8a97-499a-89b6-52f104764264.png)

可以使用**暂停按钮S--Stop**，停止转换url；使用**清空按钮C--Clear**，清空文本框的内容；使用**退出按钮E--Exit**，退出主窗口；**进度条**和**快捷键**均可在主窗口观察到。

You can use the stop **button S--Stop** to stop transforming urls; use the clear **button C--Clear** to clear the content of the text box; use the exit **button E--Exit** to exit the main window; the **progress bar** and **shortcut keys** can be observed in the main window arrive.

![image](https://user-images.githubusercontent.com/123816890/215402275-c2964e37-031e-4148-88b2-b2d70ab5fe27.png)

用户使用过程中，请注意**提示框**和**文本框**的提示信息。| During the use, please pay attention to the information and error in the **prompt box** and **text box**.

![image](https://user-images.githubusercontent.com/123816890/215403715-ca1e562e-1895-459d-a246-262985d51f76.png)

我会将**check_dict_empty.py**文件，**get_modslist_mcmod.py**文件，**get_transurl_curseforge.py**文件，以及**main_tkinter.py**文件打包成**exe文件**，打包过程中使用的**ICO图标**，如有侵权，请联系[ReclinedFish][]邮箱，我会及时予以删除。

[ReclinedFish]:ReclinedFish@proton.me

**check_dict_empty.py** file, **get modslist mcmod.py** file, **get transurl curseforge.py** file, And **main tkinter.py** file is packaged into **exe**, the **ICON** used in the packaging process, if there is infringement, please contact **ReclinedFish email**, I will delete in time.


## 声明：| Statement:

代码使用**Python**和其**标准库**以及**第三方库**，| The code uses **Python** and its **standard libraries** and **third-party libraries**, 

请各位理性使用，不要故意去增加[MCBBS][]平台的服务器负担。| Please use it rationally, and don't intentionally increase the server burden of the **MCMOD** platform.

[MCBBS]:https://www.mcbbs.net/

对于Python标准库tkinter的编程，主要使用了[OpenAI][]的聊天机器人[ChatGPT][]，我为**ChatGPT**的教学能力感到惊叹，这加深了我对**人工智能**方向的学习兴趣。

[OpenAI]:https://openai.com/

[ChatGPT]:https://chat.openai.com/chat

For the programming of Python standard library tkinter, **ChatGPT** is mainly used by **OpenAI**. I was amazed by the teaching ability of **ChatGPT**, which deepened my interest in learning **Artificial Intelligence(AI)**.

与大多数软件相同，本软件同样使用**MIT许可协议**。| Like most software, this software also uses the **MIT license**.


## 赞赏：| Donation:

感谢“抖内”，不论**金额**，不论**star**，哪怕是**下载量**都是我最好的鼓励！| Thanks to "Dona", regardless of **amount**, regardless of **star**, even **downloads** are my best encouragement!

![image](https://user-images.githubusercontent.com/123816890/215409707-b817a113-8d42-40e1-849f-4f8c936e313e.png)

我还未开通**Sponsor**功能，但我会经常将**GitHub Sponsors**的名单贴在此栏目中的。| I have not yet activated the **Sponsor** function, but I will often post the list of **GitHub Sponsors** in this column.

### Thanks a million! | 非常感谢！


## 预告：| Preview:

我已经向CurseForge申请了**API**，我将制作一个输入**CurseForge Urls的excel文件.xlsx**，输出**Mods的.jar文件的.exe**，适用于**win**操作系统。

I have applied for the **API** from CurseForge, and I will make **an .exe file** that suitable for **win** operating systems. The .exe file inputs **excel file .xlsx** that contains **CurseForge Urls**, and outputs **mods .jar files**.

申请API需要填写**表格**，填表地址：| To apply for an API, you need to fill out a **form**, [CurseForge API Applications][]

[CurseForge API Applications]:https://forms.monday.com/forms/dce5ccb7afda9a1c21dab1a1aa1d84eb?r=use1

我在**2023年1月16日**（周一）收到申请邮件，于**2023年1月29日**（周日）收到认可申请邮件，共用时**两周**。

I received the application email on **January 16** (Monday), 2023, and received the approved application email on **January 29** (Sunday), 2023, which took **two weeks**.

感谢CurseForge团队！| Thanks for The CurseForge team!

我有计划开启一个新的**YouTube频道**，介绍我单独编程的一些**软件的使用方法**，我将不断学习和体验新技术，能给这个世界稍稍带来一点方便，我便心满意足了。

I have plans to start a new **YouTube channel** to introduce **the use of some software** that I have programmed alone. I will continue to learn and experience new technologies. If I can bring a little convenience to the world, I will be satisfied.
