# Achievement/styles.css

**来源:** https://noita.wiki.gg/zh/wiki/Achievement%2Fstyles.css
---


    [](#L-1).achievements {
    [](#L-2)  display: grid;
    [](#L-3)  margin-left: 2vw;
    [](#L-4)  grid-template-columns: auto 1fr;
    [](#L-5)  grid-template-rows: auto;
    [](#L-6)}
    [](#L-7)
    [](#L-8).achievements .desc {
    [](#L-9)  padding: 0em 1em;
    [](#L-10)  background-color: #0002;
    [](#L-11)  grid-column: 2/span 1;
    [](#L-12)  font-size: 1em;
    [](#L-13)  margin: 1.6em;
    [](#L-14)  place-content: center;
    [](#L-15)}
    [](#L-16)
    [](#L-17).pillar {
    [](#L-18)  min-width: 10vw;
    [](#L-19)  max-width: 150px;
    [](#L-20)  grid-column: 1/span 1;
    [](#L-21)}
    [](#L-22).pillar.base {
    [](#L-23)  place-self: start center;
    [](#L-24)}
    [](#L-25).pillar.top {
    [](#L-26)  grid-column: 1/span 1;
    [](#L-27)  place-self: end center;
    [](#L-28)}
    [](#L-29)
    [](#L-30).reward {
    [](#L-31)  /*--child-image-size: 140px;*/
    [](#L-32)  align-content: center;
    [](#L-33)  background-color: #0000004d;
    [](#L-34)  border-radius: 0 12px;
    [](#L-35)  border: 6px solid var(--bd-darker);
    [](#L-36)  border-style: ridge;
    [](#L-37)  margin: 0.4em 1em;
    [](#L-38)  box-shadow: 0 0 28px -4px #9d7f488a;
    [](#L-39)  outline: 2px solid #0006;
    [](#L-40)  max-width: 140px;
    [](#L-41)  max-height: 180px;
    [](#L-42)  height: 180px;
    [](#L-43)  width: 140px;
    [](#L-44)  flex: 1 0 auto;
    [](#L-45)}
    [](#L-46)/*
    [](#L-47)
    [](#L-48)@media screen {
    [](#L-49)  .resultSun > img {
    [](#L-50)    min-width:121px
    [](#L-51)  }
    [](#L-52)  .makingsunwrapper {
    [](#L-53)    display:flex;
    [](#L-54)    flex-direction:row;
    [](#L-55)    border:1px dashed #414141;
    [](#L-56)    border-radius:0 5px;
    [](#L-57)    padding:1em;
    [](#L-58)    font-size:1.4em;
    [](#L-59)    gap:2em;
    [](#L-60)    align-items:center;
    [](#L-61)    border:none
    [](#L-62)  }
    [](#L-63)  .egbox-container.egbox-sun {
    [](#L-64)    padding:0.2em;
    [](#L-65)    margin-block:1em;
    [](#L-66)    margin-inline:0;
    [](#L-67)    width:fit-content;
    [](#L-68)    gap:0.8em;
    [](#L-69)    align-items:center
    [](#L-70)  }
    [](#L-71)  .egbox-container.egbox-sun>span:first-of-type {
    [](#L-72)    text-align:center;
    [](#L-73)    font-size:1.2em;
    [](#L-74)    margin-top:0.4em
    [](#L-75)  }
    [](#L-76)  .arrow {
    [](#L-77)    grid-column: 1/span 1;
    [](#L-78)    grid-row: 1/span 2;
    [](#L-79)    place-self: center;
    [](#L-80)    min-width: 32px;
    [](#L-81)  }
    [](#L-82)  .resultSun {
    [](#L-83)    display: grid;
    [](#L-84)    grid-template-columns: min-content min-content;
    [](#L-85)    grid-template-rows: auto auto;
    [](#L-86)    margin-left: 2em;
    [](#L-87)  }
    [](#L-88)  .resultSun > img,
    [](#L-89)  .resultSun > span {
    [](#L-90)    grid-column: 2/span 1;
    [](#L-91)    place-self: center;
    [](#L-92)  }
    [](#L-93)}
    [](#L-94)@media screen and (max-width:720px) {
    [](#L-95)  .elementalcombo img {
    [](#L-96)    min-width:32px
    [](#L-97)  }
    [](#L-98)  .makingsunwrapper {
    [](#L-99)    padding:0.2em;
    [](#L-100)    border:none;
    [](#L-101)    margin-bottom:0.8em;
    [](#L-102)    flex-wrap: wrap;
    [](#L-103)    gap:0;
    [](#L-104)    justify-content: center;
    [](#L-105)  }
    [](#L-106)  .egbox-container.egbox-sun {
    [](#L-107)    padding:0.2em;
    [](#L-108)    margin-block:1em;
    [](#L-109)    margin-inline:0;
    [](#L-110)    width:auto;
    [](#L-111)    gap:0.8em;
    [](#L-112)    align-items:center
    [](#L-113)  }
    [](#L-114)  .egbox-container.egbox-sun > span:first-of-type {
    [](#L-115)    text-align:center;
    [](#L-116)    font-size:1.2em;
    [](#L-117)    margin-top:0.4em
    [](#L-118)  }
    [](#L-119)}
    [](#L-120)
    [](#L-121)@media screen {
    [](#L-122)  .books {
    [](#L-123)    display:grid;
    [](#L-124)    grid-template-rows: repeat(3, auto);
    [](#L-125)    grid-template-columns: 1fr 1fr;
    [](#L-126)    row-gap:0.8em;
    [](#L-127)    column-gap: 0.8em;
    [](#L-128)  }
    [](#L-129)  .lore-book + div {
    [](#L-130)    display: none;
    [](#L-131)  }
    [](#L-132)  .lore-book:first-child {
    [](#L-133)    min-width: unset;
    [](#L-134)    grid-column: 1/span 2;
    [](#L-135)  }
    [](#L-136)}
    [](#L-137)
    [](#L-138)@media screen and (max-width:720px) {
    [](#L-139)  .books {
    [](#L-140)    display:grid;
    [](#L-141)    grid-template-rows: repeat(5, auto);
    [](#L-142)    grid-template-columns: auto;
    [](#L-143)  }
    [](#L-144)  .lore-book:first-child {
    [](#L-145)    grid-column: 1/span 1;
    [](#L-146)  }
    [](#L-147)  .book > .lore-book {
    [](#L-148)    min-height: 24vh;
    [](#L-149)    grid-template-rows: auto 1fr;
    [](#L-150)  }
    [](#L-151)  
    [](#L-152)  .book > .lore-book .book-image {
    [](#L-153)    grid-row: 1/span 2;
    [](#L-154)  }
    [](#L-155)}
    [](#L-156)
    [](#L-157)
    [](#L-158)
    [](#L-159).mapshroom {
    [](#L-160)	display: grid;
    [](#L-161)    grid-template-columns: [left west-start]2fr[west-end center-start]3fr[meridian]2fr[center-end east-start]2fr[east-end right];
    [](#L-162)    grid-template-rows: [top north-start]1fr[north-end middle-start]4fr[middle-end south-start]1fr[south-end bottom];
    [](#L-163)	place-items: center; 
    [](#L-164)    column-gap: 2em;
    [](#L-165)    row-gap: 0.4em;
    [](#L-166)}
    [](#L-167).middle {
    [](#L-168)	grid-column: center;
    [](#L-169)	grid-row: middle;
    [](#L-170)    box-shadow: 0 0 2px 1px #b79640, 0 0 8px 3px black;
    [](#L-171)    border-radius: 2px;
    [](#L-172)}
    [](#L-173).middle img {
    [](#L-174)    border-radius: 4px;
    [](#L-175)    border: 2px solid black;
    [](#L-176)}
    [](#L-177).north {
    [](#L-178)	grid-row: north;
    [](#L-179)	text-align: center;
    [](#L-180)    grid-column: center;
    [](#L-181)    place-self: center;
    [](#L-182)}
    [](#L-183).west {
    [](#L-184)	grid-column: west;
    [](#L-185)	grid-row: middle;
    [](#L-186)	text-align: center;
    [](#L-187)}
    [](#L-188).east {
    [](#L-189)	grid-column: east;
    [](#L-190)	grid-row: middle;
    [](#L-191)	text-align: center;
    [](#L-192)}
    [](#L-193).southwest {
    [](#L-194)	grid-column: west/meridian;
    [](#L-195)	grid-row: south;
    [](#L-196)	text-align: center;
    [](#L-197)}
    [](#L-198).southeast {
    [](#L-199)	grid-column: meridian/east;
    [](#L-200)	grid-row: south;
    [](#L-201)	text-align: center;
    [](#L-202)}
    [](#L-203)*/
    
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
