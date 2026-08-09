# 三眼/styles.css

**来源:** https://noita.wiki.gg/zh/wiki/%E4%B8%89%E7%9C%BC%2Fstyles.css
---


    [](#L-1).kolmisilma-scaling {
    [](#L-2)    padding: 4px;
    [](#L-3)}
    [](#L-4).kolmisilma-scaling td:nth-of-type(1) {
    [](#L-5)    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAMAAAC5zwKfAAAAFVBMVEUAAADq+/+t4/+A1P9PsdpEjc8/e7JESsEjAAAAAXRSTlMAQObYZgAAAJRJREFUeNrt2EEKwCAMRNFqmt7/yGU2GRqwi4qByvydCx9IEMFD7ZMhgdWgoffNAr+COvwWYN5nUaIFVoJRQz1qyJDAapCWo/NZUgXOg1OWIaoCa8CGTnShZDGqApeDHTkaTznqSGAheCGqTGAxmK/eUHXUkMDlIFVHVLlMlsASMM/bo/Q0CawGqfaIlsApUD/av+sGOmEfKMmX8SkAAAAASUVORK5CYII=');
    [](#L-6)    background-position: left 4px top calc(50% - 3px);
    [](#L-7)    background-size: 2.4em;
    [](#L-8)    background-repeat: no-repeat;
    [](#L-9)    image-rendering: pixelated;
    [](#L-10)    padding: 0.4em 0.5em 0.2em 2.7em;
    [](#L-11)    text-align: center;
    [](#L-12)    line-height: 2.6em;
    [](#L-13)    font-family: noita;
    [](#L-14)    font-size: 1.5em;
    [](#L-15)    color: #b5e7ff;
    [](#L-16)    background-color: #000934aa;
    [](#L-17)    text-shadow:
    [](#L-18)      -0.1em  0     0 #000,
    [](#L-19)       0      0.1em 0 #000,
    [](#L-20)       0.1em  0     0 #000,
    [](#L-21)       0     -0.1em 0 #000,
    [](#L-22)       0.1em -0.1em 0 #000,
    [](#L-23)       0.1em  0.1em 0 #000,
    [](#L-24)      -0.1em  0.1em 0 #000,
    [](#L-25)      -0.1em -0.1em 0 #000;
    [](#L-26)}
    [](#L-27)
    [](#L-28).kolmisilma-scaling .orbs0 td:nth-of-type(1) {
    [](#L-29)    background-color: #000000aa;
    [](#L-30)}
    [](#L-31).kolmisilma-scaling .orbs10 td:nth-of-type(1),
    [](#L-32).kolmisilma-scaling .orbs10 ~ tr td:nth-of-type(1)  {
    [](#L-33)    font-size: 1.3em;
    [](#L-34)}
    [](#L-35).kolmisilma-scaling .orbs11 ~ tr td:nth-of-type(1) {
    [](#L-36)    background-color: #001d34aa;
    [](#L-37)}
    [](#L-38).kolmisilma-scaling .orbs20 ~ tr td:nth-of-type(1) {
    [](#L-39)    font-size: 1.2em;
    [](#L-40)}
    [](#L-41).kolmisilma-scaling .orbs31 ~ tr td:nth-of-type(1) {
    [](#L-42)    background-color: #000526aa;
    [](#L-43)}
    [](#L-44)
    [](#L-45).kolmisilma-scaling .thousands td:nth-of-type(2), 
    [](#L-46).kolmisilma-scaling .thousands ~ tr td:nth-of-type(2) {
    [](#L-47)    font-size: 1.4em;
    [](#L-48)    text-align: center;
    [](#L-49)    background-color: #2200ee0a;
    [](#L-50)}
    [](#L-51).kolmisilma-scaling .millions ~ tr td:nth-of-type(2) {
    [](#L-52)    font-size: 1.3em;
    [](#L-53)    background-color: #4400cc11;
    [](#L-54)}
    [](#L-55).kolmisilma-scaling .billions ~ tr td:nth-of-type(2) {
    [](#L-56)    font-size: 1.2em;
    [](#L-57)    background-color: #6600aa13;
    [](#L-58)}
    [](#L-59).kolmisilma-scaling .trillions ~ tr td:nth-of-type(2) {
    [](#L-60)    font-size: 1.1em;
    [](#L-61)    background-color: #88008815;
    [](#L-62)}
    [](#L-63).kolmisilma-scaling .quadrillions ~ tr td:nth-of-type(2) {
    [](#L-64)    font-size: 1em;
    [](#L-65)    background-color: #aa006617;
    [](#L-66)}
    [](#L-67).kolmisilma-scaling .quintillions ~ tr td:nth-of-type(2) {
    [](#L-68)    font-size: 0.9em;
    [](#L-69)    background-color: #cc004419;
    [](#L-70)}
    [](#L-71).kolmisilma-scaling .sextillions ~ tr td:nth-of-type(2) {
    [](#L-72)    font-size: 0.8em;
    [](#L-73)    background-color: #ee002223;
    [](#L-74)}
    [](#L-75).kolmisilma-scaling .infinite ~ tr td:nth-of-type(2) {
    [](#L-76)  font-size: 1.4em;
    [](#L-77)}
    [](#L-78).kolmisilma-scaling .infinite ~ tr td:nth-of-type(2) > div:nth-of-type(1) {
    [](#L-79)  margin: 0.2em 0 0 0;
    [](#L-80)}
    [](#L-81).kolmisilma-scaling .infinite ~ tr td:nth-of-type(2) > div:nth-of-type(2) {
    [](#L-82)  font-size: 0.8em;
    [](#L-83)  white-space: nowrap;
    [](#L-84)  color: red;
    [](#L-85)  margin: 0.3em 0.2em 0.5em 0.2em;
    [](#L-86)  font-family: noita-aligned;
    [](#L-87)  display: inline-flex;
    [](#L-88)  align-items: center;
    [](#L-89)}
    [](#L-90).kolmisilma-scaling .infinite ~ tr td:nth-of-type(2) > div:nth-of-type(2) > div {
    [](#L-91)  margin: 0 0.2ch;
    [](#L-92)  font-size: 0.7em;
    [](#L-93)  align-items: center;
    [](#L-94)}
    [](#L-95)
    [](#L-96).kolmisilma-scaling .threshold {
    [](#L-97)  height: 1.6em;
    [](#L-98)}
    [](#L-99)
    [](#L-100).kolmisilma-scaling .threshold > :only-child {
    [](#L-101)  width: 100%;
    [](#L-102)  height: 1.4em;
    [](#L-103)  position: relative;
    [](#L-104)  background-image: none;
    [](#L-105)  padding: 0;
    [](#L-106)}
    [](#L-107).kolmisilma-scaling .threshold > :only-child > div {
    [](#L-108)  position: absolute;
    [](#L-109)  left: -5px;
    [](#L-110)  right: -5px;
    [](#L-111)  top: -1px;
    [](#L-112)  bottom: -1px;
    [](#L-113)  padding: 0;
    [](#L-114)  background-color: #240000;
    [](#L-115)  
    [](#L-116)  border-style: solid solid;
    [](#L-117)  border-radius: 1em / 100%;
    [](#L-118)  box-sizing: border-box;
    [](#L-119)  border-width: 0.2px 0 2px 0;
    [](#L-120)  background-size: 100%;
    [](#L-121)  background-position: center;
    [](#L-122)
    [](#L-123)  color: #ffffffef;
    [](#L-124)  font-family: noita;
    [](#L-125)  font-weight: bold;
    [](#L-126)  text-shadow: -1px 1px 0 #000,1px 1px 0 #000,1px -1px 0 #000,-1px -1px 0 #000,-1px 0 0 #000,1px 0 0 #000,0 -1px 0 #000,0 1px 0 #000;
    [](#L-127)  letter-spacing: 0.1em;
    [](#L-128)  font-variant: small-caps;
    [](#L-129)  line-height: 2.1em;
    [](#L-130)  font-size: 0.7em;
    [](#L-131)}
    [](#L-132)
    [](#L-133).kolmisilma-scaling .threshold.event > :only-child > div {
    [](#L-134)  color: #eefaff;
    [](#L-135)  background-color: #002c3d;
    [](#L-136)  box-shadow: 0 1px 8px -1px #009edcc2 inset, 0 2px 2px 0 black;
    [](#L-137)  border-color: #009edc #009edc #002c3d #009edc;
    [](#L-138)}
    [](#L-139)
    [](#L-140).kolmisilma-scaling .threshold.health > :only-child > div {
    [](#L-141)  color: #ffe3e3;
    [](#L-142)  background-color: #240000;
    [](#L-143)  box-shadow: 0 1px 8px -1px #d33 inset, 0 2px 2px 0 black;
    [](#L-144)  border-color: #d33 #d33 #240000 #d33;
    [](#L-145)}
    [](#L-146)
    [](#L-147).kolmisilma-scaling .reward.reward > td:nth-of-type(1) {
    [](#L-148)    background-color: #bea409ab;
    [](#L-149)    box-shadow: 0 0 4px 5px #091b2a inset;
    [](#L-150)}
    [](#L-151)
    [](#L-152)
    [](#L-153)
    [](#L-154)@media screen and (max-width: 700px) {
    [](#L-155)  .kolmisilma-scaling.kolmisilma-scaling.kolmisilma-scaling {
    [](#L-156)    display: grid;
    [](#L-157)    grid-template-columns: auto 1fr;
    [](#L-158)    border-style: solid;
    [](#L-159)    padding: 0;
    [](#L-160)  }
    [](#L-161)  .kolmisilma-scaling.kolmisilma-scaling tbody, 
    [](#L-162)  .kolmisilma-scaling.kolmisilma-scaling tr {
    [](#L-163)    display: contents;
    [](#L-164)  }
    [](#L-165)  .kolmisilma-scaling .threshold > :only-child > div {
    [](#L-166)    grid-column: 1/span 2;
    [](#L-167)    position: static;
    [](#L-168)    margin: -1px 0 6px 0;
    [](#L-169)  }
    [](#L-170)  .kolmisilma-scaling.kolmisilma-scaling td:last-child,
    [](#L-171)  .kolmisilma-scaling.kolmisilma-scaling th:last-child {
    [](#L-172)    border-right-width: 1px;
    [](#L-173)	margin-bottom: 8px;
    [](#L-174)	border-bottom-width: 1px;
    [](#L-175)	border-radius: 0 0 0 6px;
    [](#L-176)  }
    [](#L-177)  .kolmisilma-scaling .threshold td:only-child {
    [](#L-178)    display: contents;
    [](#L-179)  }
    [](#L-180)  .kolmisilma-scaling tr > :nth-of-type(1) {
    [](#L-181)    grid-column: 1/span 1;
    [](#L-182)    border-width: 1px 1px 1px 1px;
    [](#L-183)    border-radius: 0 0 0 10px;
    [](#L-184)    margin-left: 0;
    [](#L-185)  }
    [](#L-186)  .kolmisilma-scaling tr > :nth-of-type(2) {
    [](#L-187)    align-content: center;
    [](#L-188)    grid-column: 2/span 1;
    [](#L-189)    border-width: 1px 1px 1px 0;
    [](#L-190)    border-radius: 0 7px 0 0 ;
    [](#L-191)  }
    [](#L-192)  .kolmisilma-scaling tr > :nth-of-type(3) {
    [](#L-193)    grid-column: 1/span 2;
    [](#L-194)    border-width: 0 1px 0 1px;
    [](#L-195)    margin: 0 6px 0 6px;
    [](#L-196)  }
    [](#L-197)  .kolmisilma-scaling .threshold > :only-child > div {
    [](#L-198)    font-size: 0.6em;
    [](#L-199)    margin-bottom: 6px;
    [](#L-200)    z-index: 1;
    [](#L-201)  }
    [](#L-202)  
    [](#L-203)  .kolmisilma-scaling .thousands td:nth-of-type(2),
    [](#L-204)  .kolmisilma-scaling .thousands ~ tr td:nth-of-type(2) {
    [](#L-205)    font-size: 1.6em;
    [](#L-206)    display: flex;
    [](#L-207)    justify-content: center;
    [](#L-208)    align-items: center;
    [](#L-209)  }  
    [](#L-210)  .kolmisilma-scaling .millions ~ tr td:nth-of-type(2) {
    [](#L-211)    font-size: 1.4em;
    [](#L-212)  }
    [](#L-213)  .kolmisilma-scaling .billions ~ tr td:nth-of-type(2) {
    [](#L-214)    font-size: 3vw;
    [](#L-215)  }
    [](#L-216)  .kolmisilma-scaling .trillions ~ tr td:nth-of-type(2) {
    [](#L-217)    font-size: 3vw;
    [](#L-218)  }
    [](#L-219)  .kolmisilma-scaling .quadrillions ~ tr td:nth-of-type(2) {
    [](#L-220)    font-size: 3vw;
    [](#L-221)  }
    [](#L-222)  .kolmisilma-scaling .quintillions ~ tr td:nth-of-type(2) {
    [](#L-223)    font-size: 2.9vw;
    [](#L-224)  }
    [](#L-225)  .kolmisilma-scaling .sextillions ~ tr td:nth-of-type(2) {
    [](#L-226)    font-size: 2.8vw;
    [](#L-227)  }
    [](#L-228)
    [](#L-229)  .kolmisilma-scaling.kolmisilma-scaling tr:first-child > th:nth-of-type(1) {
    [](#L-230)    border-width: 2px 1px 2px 2px;
    [](#L-231)  }
    [](#L-232)  .kolmisilma-scaling.kolmisilma-scaling tr:first-child > th:nth-of-type(2) {
    [](#L-233)    border-width: 2px 2px 2px 1px;
    [](#L-234)  }
    [](#L-235)  .kolmisilma-scaling.kolmisilma-scaling tr:first-child > th:nth-of-type(3) {
    [](#L-236)    border-width: 0 2px 1px 2px;
    [](#L-237)    padding: 0.1em;
    [](#L-238)  }
    [](#L-239)  .kolmisilma-scaling.kolmisilma-scaling tr:last-child > td {
    [](#L-240)    border-bottom-width: 1px;
    [](#L-241)  }
    [](#L-242)}
    
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
  *[1/44.5]: 2.244%
  *[1/93.3]: 1.070%
  *[1/172]: 0.580%
  *[1/185]: 0.538%
  *[1/238]: 0.419%
  *[1/649]: 0.153%
  *[1/417]: 0.239%
  *[1/410]: 0.243%
  *[1/59.8]: 1.672%
  *[1/1428]: 0.069%
  *[1/1252]: 0.079%
  *[1/105]: 0.951%
  *[1/129]: 0.769%
  *[1/166]: 0.598%
