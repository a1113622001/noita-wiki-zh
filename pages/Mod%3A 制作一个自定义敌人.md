# Mod:制作一个自定义敌人

**分类:** [Category:Stubs](Category%3AStubs.md) · [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA
---

[![Effect Invisibility.png](https://noita.wiki.gg/zh/images/thumb/Effect_Invisibility.png/44px-Effect_Invisibility.png?887c92)](/zh/wiki/File:Effect_Invisibility.png)

_本页面的内容不完善或仍需整理。来帮助我们[完善它](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA?action=edit)吧！_

模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • 敌人 • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
此页面介绍了用于创建新敌人的基础知识。（施工中） 

## 常见组件和标签

实体组件  组件名 | 用途   
---|---  
[AnimalAIComponent](Documentation%3A AnimalAIComponent.md) | 控制敌人的行为和攻击。   
[DamageModelComponent](Documentation%3A DamageModelComponent.md) | 定义敌人是否能被攻击，决定各种类型的承伤倍率和材料伤害。   
[PathFindingComponent](Documentation%3A PathFindingComponent.md) | 允许敌人通过地形和敌人位置进行寻路。   
[PathFindingGridMarkerComponent](Documentation%3A PathFindingGridMarkerComponent.md) | 对寻路轨迹产生特定的影响（需要进一步研究）。   
[GenomeDataComponent](Documentation%3A GenomeDataComponent.md) | [敌人阵营](敌人阵营.md)，食物链等级等信息。   
[CharacterPlatformingComponent](Documentation%3A CharacterPlatformingComponent.md) | 决定敌人的移动能力。   
[CharacterDataComponent](Documentation%3A CharacterDataComponent.md) | 控制敌人的碰撞、物理运动等。   
[HitboxComponent](Documentation%3A HitboxComponent.md) | 决定敌人的碰撞箱。   
[CameraBoundComponent](Documentation%3A CameraBoundComponent.md) | 决定该敌人在相机的多远处会被卸载。   
[SpriteComponent](Documentation%3A SpriteComponent.md) | 敌人的精灵图。   
[SpriteAnimatorComponent](Documentation%3A SpriteAnimatorComponent.md) | 在敌人进行不同行为时切换动画。   
[AudioComponent](Documentation%3A AudioComponent.md) | 决定敌人在特定条件下播放的音效。   
标签  标签名 | 用途   
---|---  
mortal | 一个多用途标签，用于可被摧毁的生物和实体（需要进一步研究）。   
hittable | 敌人可以被击中。   
enemy | 该敌人是enemy。   
flying | 该敌人是飞行敌人。   
boss | 该敌人是BOSS。   
miniboss | 该敌人是小BOSS。   
human | （待研究）   
prey | 该敌人有可能被捕猎者锁定。   
homing_target | 该敌人有可能被追踪投射物锁定。   
destruction_target | 该敌人会被[毁灭](毁灭.md)抹消。   
teleportable_NOT | 该敌人免疫传送。   
polymorphable_NOT | 该敌人免疫变形。   
necrobot_NOT | 该敌人不会被[复活机器人](Tuonelankone.md)等复活。   
glue_NOT | 该敌人不会被胶球黏住。   
curse_NOT | 敌人免疫猛毒诅咒。   
touchmagic_immunity | 敌人免疫[点金法术](法术之触.md)带来的伤害。   
  
## AnimalAIComponent.ai_state枚举值

`AnimalAIComponent::ai_state`属性的有效值范围为 1-21，它们分别对应以下状态：
    
    
    local states = {
     "RandomMove",
     "Wandering",
     "Eating",
     "RaisingHead",
     "PreparingJump",
     "MoveNearTarget",
     "Peeing",
     "Defecating",
     "Alert",
     "Landing",
     "TakingFireDamage",
     "EscapingPrey",
     "AttackingMelee",
     "AttackingMeleeDash",
     "AttackingRanged",
     "AttackingRangedMulti",
     "Escaping",
     "JobDefault",
     "JobGoto",
     "JobHelpOtherEntity",
     "GoNearHome",
    }
    

它们可以用下面这样的代码输出：
    
    
    local animal = GetUpdatedEntityID()
    local state = ComponentGetValue2(
      EntityGetFirstComponentIncludingDisabled(animal, "AnimalAIComponent"), "ai_state"
    )
    
    print(states[state])
    
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
