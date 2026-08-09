# Mod:音频

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E9%9F%B3%E9%A2%91
---

模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
音频 • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
此页面介绍了默认音频如何**提取** 、**替换** 以及**新增** 你自己的音频。 

## 

现有音频的提取与替换

`.wav`音频文件被压缩在`Steam\steamapps\common\Noita\data\audio\Desktop\`目录下的20多个`.bank`文件之中。 

  1. 下载并解压 "Fmod bank tools.zip" ~~[(discord link)](https://cdn.discordapp.com/attachments/632303734877192192/702085775516237845/Fmod_Bank_Tools.zip)~~ （已失效）
  2. 找一个你想要修改的bank文件（如`event_cues.bank`）将它复制到你要提取的bank的文件夹里。
  3. 运行`Fmod Bank Tools.exe` 设置`Bank Source Folder`到bank文件夹路径（完整路径 `C:/.../bank`）并设置`Wav Destination Folder`到wav存放的目标文件夹路径（也是完整路径）。两个文件夹都应该在你解压zip的文件夹里。
  4. 点击工具的 Extract (提取) 按钮以获得bank中的所有音频文件。 
     * 现在你可以用游戏音效来创作音乐了！
  5. 通过编辑 wav 文件夹中的`bankname.txt`获取正确的音效名以替换(或新增)任意 .wav 文件，然后在`Fmod Bank Tools.exe` 中点击 Rebuild（重新构建）。如果遇到报错点击 ok 直到它完成。
  6. 进入游戏测试。 (记住这主要是用于替换而不是新增，你可以通过Fmod Studio来新增更多功能).



**注意：因为这种方式替换了bank文件，所以你不能启用多个音效替换mod！**

## 为Noita创建自定义音频

Noita 使用[FMOD Studio](https://www.fmod.com) 作为自己的音效引擎, (使用版本 2.01.05). 基本原理是这些由音效构成的Fmod "bank" 文件，且每个音效都附加了单独的事件。这些事件在XML/Lua中被引用以播放对应的音效。 

从以下两个目录开始: 

  * `Noita/tools_modding/noita-fmod-project/`
  * `Noita/mods/example/`



### 安装

  1. 确保Noita本体目录(tools_modding)下有 noita-fmod-project 文件夹
  2. 从 FMOD 官网安装FMOD Studio (version 2.01.05)(需要注册登录才能下载).



### FMOD

  1. 在 Fmod Studio中打开 **noita-mods.fspro** ，你将会看到一个包含`create`示例事件的**snd_mod** 文件夹。在Noita中有多种不同的事件，但现在请记住`create` 和 `loop`是最常见的。
  2. 通过点击处于**snd_mod**`create`事件你将会看到一个处于异步模式（Async 选中这段音轨即可查看）具有音调自动随机化、`Distance`参数、能在游戏中产生如音量衰减效果的`lowpass`参数的`worm_attack_bite_01`示例音频
  3. Noita also has many Routing Groups which add effects to your audio such as reverb and equalization, to access these you'll need to go to the `Window` options and then `Mixer`, where you can move your sounds into their respective groups, such as `game_sfx` which houses `snd_mod/create`, this group is what you'll likely use the most.(译者注:这条不想翻译,这个不重要😣,因为这个步骤你不会用fmod的话很难复现出来, 我建议你直接替换示例中的音频)
  4. 决定好要在事件中制作音效你就想要把它添加到bank中，这样Noita才能将其作为游戏资源使用它。需要右键这个事件选择`Assign To Bank`中的目标bank（最好不是Master Bank）
  5. 在此之后你需要通过点击`File`选项下的`Build`来进行构建。
  6. 至此并没有结束，Noita仍然不知道如何访问Bnak中的事件，因此你需要在`File`选项下使用`Export GUIDs`来生成一份映射表。这是你需要在`init.lua`中加载的内容，这样Noita就有了bank音频的引用。



### Noita

  1. 将`noita-fmod-project/Build` 复制 **GUIDs.txt** 到你的mod文件夹.
  2. Go into `noita-fmod-project/Build/Desktop` and copy and paste the `bankname`.bank file (忽略 Master Bank) you created in FMOD into your mod's directory.
  3. 将`noita-fmod-project/Build/Desktop`你在Fmod中生成的`bankname`.bank文件复制到你的mod文件夹。
  4. 在你mod的 **init.lua** 文件中添加 (使用你自己的 GUIDs.txt 文件路径)


    
    
    ModRegisterAudioEventMappings("mods/modname/directory/to/GUIDs.txt")
    

  1. 在你想添加音效的xml文件中根据你在Fmod中创建的事件添加对应的`AudioComponent` 或 `AudioLoopComponent`



一个投射物的`AudioComponent`大概会是这样: 
    
    
    <!-- file: .bank 要替换为 .snd 译者注: 并不需要!!! -->
    <!-- event_root: 在Fmod中你创建的内部含有 create 或 loop 事件的一个事件文件夹 -->
    <AudioComponent
        file="mods/modname/directory/to/bankname.snd"
        event_root="foldername/eventname"
        set_latest_event_position="1"
    ></AudioComponent>
    

  1. 进入游戏体验吧！



## 默认音效列表

参见: [Mod: 声音列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) (_暂不完整_) 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
