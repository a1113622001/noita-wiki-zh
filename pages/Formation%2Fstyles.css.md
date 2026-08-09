# Formation/styles.css

**来源:** https://noita.wiki.gg/zh/wiki/Formation%2Fstyles.css
---


    [](#L-1)/*
    [](#L-2)  Somewhat experimental CSS for Formation visualisation - WIP
    [](#L-3)*/
    [](#L-4)
    [](#L-5):root {
    [](#L-6)  --mina: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAJFBMVEUAAACbb5p/VHbRYGAnISWrMTFZQ1TRmz3w5Jv///76x6bbwGdFQ1nrAAAAAXRSTlMAQObYZgAAAMNJREFUeF7t07sKwjAUBuCThuJlsmr3GsU5GoKODn2AYhFxc/IFimRwcRE69hF8BHdfzsSK8QJBlx4H/2T7PwhJOHAPCUxa8JJKgK278QwAE+g6RgYeG/wAMImQgP2sNhqwNUMFHutdyXCzRgIkaAGpBnTGD4DKlL+DCMAFwnlfcCq4nzQKyrXhHwI6CsJUlmthtkZCJgD+qijBND84AdTzPdSUUttldjuiebRHfAOyye58erqmjeMdEAYHczb/wNSo4ALnoVf+uIyuTwAAAABJRU5ErkJggg==');
    [](#L-7)  --bd-darker: #5f543f;
    [](#L-8)}
    [](#L-9)
    [](#L-10).formation-angle::after {
    [](#L-11)  content: '';
    [](#L-12)  image-rendering: pixelated;
    [](#L-13)  position: absolute;
    [](#L-14)  top: 0;
    [](#L-15)  right: 0;
    [](#L-16)  bottom: 0;
    [](#L-17)  left: 0;
    [](#L-18)  background-size: var(--bsize-mina);
    [](#L-19)  background-position: var(--bpos-mina);
    [](#L-20)  background-repeat: no-repeat;
    [](#L-21)  background-image: var(--mina);
    [](#L-22)  --filter: drop-shadow(-2px 0.4px 1.2px var(--c-bg)) drop-shadow(0 0 0px #aaa);
    [](#L-23)  filter: var(--filter);
    [](#L-24)}
    [](#L-25).formation-angle {
    [](#L-26)  --c-bg: #191919;
    [](#L-27)  --bsize-mina: 50%;
    [](#L-28)  --bpos-mina: 10% 39%;
    [](#L-29)  --wand-direction: 90deg;
    [](#L-30)  --a-base: var(--wand-direction);
    [](#L-31)  --offby: 0;
    [](#L-32)  --dangle: calc((var(--angle) * 2) / (var(--pcount) - var(--offby)));
    [](#L-33)  --bsize: 100%;
    [](#L-34)  --bpos: 50% 50%;
    [](#L-35)  --off: 10deg;
    [](#L-36)  --w-inner: 1deg;
    [](#L-37)  --c-inner: rgb(255 233 233 / 90%);
    [](#L-38)  --w-outer: 2.6deg;
    [](#L-39)  --c-outer: rgb(0 0 0 / 80%);
    [](#L-40)  --c2l: hsl(calc(var(--angle) + var(--off) + var(--dangle)) 90% 80% / 30%);
    [](#L-41)  --c2d: hsl(calc(var(--angle) + var(--off) + var(--dangle)) 90% 40% / 30%);
    [](#L-42)  position: relative;
    [](#L-43)  border-radius: 3%;
    [](#L-44)  --border: 1px solid var(--c-bg);
    [](#L-45)  border: var(--border);
    [](#L-46)  font-family: noita;
    [](#L-47)  aspect-ratio: 1;
    [](#L-48)  display: flex;
    [](#L-49)  align-items: end;
    [](#L-50)  justify-content: left;
    [](#L-51)  padding: 10px;
    [](#L-52)  line-height: 0.2;
    [](#L-53)  color: #ddd;
    [](#L-54)  background-color: var(--c-bg);
    [](#L-55)  background-size: var(--bsize);
    [](#L-56)  background-position: var(--bpos);
    [](#L-57)  background-repeat: no-repeat;
    [](#L-58)  background-image: var(--background-image);
    [](#L-59)  --background-image: 
    [](#L-60)    var(--segments-mask),
    [](#L-61)    var(--ray-beams),
    [](#L-62)    var(--segments),
    [](#L-63)    var(--ray-shadows),
    [](#L-64)    var(--segments),
    [](#L-65)    linear-gradient(transparent,transparent);
    [](#L-66)  image-rendering: pixelated;
    [](#L-67)  text-shadow: -1px -1px 0 black, 1px 1px 0 black, -1px 1px 0 black, 1px -1px 0 black,
    [](#L-68)    0 -1px 0 black, 0 1px 0 black, -1px 0 0 black, 1px 0 0 black;
    [](#L-69)
    [](#L-70)  --segments: conic-gradient(
    [](#L-71)      from calc(var(--a-base) - var(--w-inner) - var(--angle)),
    [](#L-72)      var(--c-bg),
    [](#L-73)      var(--c2d) var(--w-inner),
    [](#L-74)      var(--c2l) var(--angle),
    [](#L-75)      var(--c2d) calc((var(--angle) * 2) + var(--w-inner)),
    [](#L-76)      var(--c-bg) calc((var(--angle) * 2) + calc(var(--w-inner) * 2)));
    [](#L-77)  --segments-mask: conic-gradient(
    [](#L-78)      from calc(var(--a-base) - var(--w-outer) - var(--angle)),
    [](#L-79)    transparent 0 calc((var(--angle) * 2) + calc(var(--w-outer) * 2)),
    [](#L-80)      var(--c-bg) calc((var(--angle) * 2) + calc(var(--w-outer) * 2)));
    [](#L-81)  --ray-beams: repeating-conic-gradient(
    [](#L-82)      from calc(var(--a-base) - calc(var(--w-inner) * 2) - var(--angle)),
    [](#L-83)      transparent,
    [](#L-84)      var(--c-inner) calc(var(--w-inner) * 1) calc(var(--w-inner) * 3),
    [](#L-85)      transparent calc(var(--w-inner) * 4) calc(var(--dangle)));
    [](#L-86)  --ray-shadows: repeating-conic-gradient(
    [](#L-87)      from calc(var(--a-base) - calc(var(--w-outer) * 2) - var(--angle)),
    [](#L-88)      transparent,
    [](#L-89)      var(--c-outer) calc(var(--w-outer) * 1) calc(var(--w-outer) * 3),
    [](#L-90)      transparent calc(var(--w-outer) * 4) calc(var(--dangle)));
    [](#L-91)}
    [](#L-92)[data-proj-count="12"] {
    [](#L-93)  --pcount: 12;
    [](#L-94)}
    [](#L-95)[data-proj-count="10"] {
    [](#L-96)  --pcount: 10;
    [](#L-97)}
    [](#L-98)[data-proj-count="6"] {
    [](#L-99)  --pcount: 6;
    [](#L-100)}
    [](#L-101)[data-proj-count="5"] {
    [](#L-102)  --pcount: 5;
    [](#L-103)}
    [](#L-104)[data-proj-count="4"] {
    [](#L-105)  --pcount: 4;
    [](#L-106)}
    [](#L-107)[data-proj-count="3"] {
    [](#L-108)  --pcount: 3;
    [](#L-109)}
    [](#L-110)[data-proj-count="2"] {
    [](#L-111)  --pcount: 2;
    [](#L-112)}
    [](#L-113)[data-angle="180"] {
    [](#L-114)  --angle: 180deg;
    [](#L-115)  --offby: 0;
    [](#L-116)}
    [](#L-117)[data-angle="90"] {
    [](#L-118)  --angle: 90deg;
    [](#L-119)}
    [](#L-120)[data-angle="45"] {
    [](#L-121)  --angle: 45deg;
    [](#L-122)}
    [](#L-123)[data-angle="20"] {
    [](#L-124)  --angle: 20deg;
    [](#L-125)}
    [](#L-126)[data-angle="30"]  {
    [](#L-127)  --angle: 30deg;
    [](#L-128)}
    [](#L-129)[data-angle="5"]  {
    [](#L-130)  --angle: 5deg;
    [](#L-131)}
    [](#L-132)
    [](#L-133)
    [](#L-134)
    [](#L-135)
    [](#L-136).formation-angle {
    [](#L-137)  --c-bg: #191919;
    [](#L-138)  --a-base: var(--wand-direction);
    [](#L-139)  --dangle: calc((var(--angle) * 2) / (var(--pcount) - var(--offby)));
    [](#L-140)  --bsize: 100%;
    [](#L-141)  --bpos: 50% 50%;
    [](#L-142)  --off: 10deg;
    [](#L-143)  --w-inner: 1deg;
    [](#L-144)  --c-inner: rgb(255 233 233 / 90%);
    [](#L-145)  --w-outer: 2.6deg;
    [](#L-146)  --c-outer: rgb(0 0 0 / 80%);
    [](#L-147)  --c2l: hsl(calc(var(--angle) + var(--off) + var(--dangle)) 90% 80% / 30%);
    [](#L-148)  --c2d: hsl(calc(var(--angle) + var(--off) + var(--dangle)) 90% 40% / 30%);
    [](#L-149)  position: relative;
    [](#L-150)  --border: 1px solid var(--c-bg);
    [](#L-151)  border: var(--border);
    [](#L-152)  border-radius: 3%;
    [](#L-153)  font-family: noita;
    [](#L-154)  aspect-ratio: 1.618;
    [](#L-155)  display: flex;
    [](#L-156)  padding: 10px;
    [](#L-157)  line-height: 0.2;
    [](#L-158)  color: #ddd;
    [](#L-159)  background-color: var(--c-bg);
    [](#L-160)  background-size: 200% 200%;
    [](#L-161)  background-repeat: no-repeat;
    [](#L-162)  background-image: var(--background-image);
    [](#L-163)  --background-image:
    [](#L-164)    var(--segments-mask), var(--ray-beams), var(--segments), var(--ray-shadows),
    [](#L-165)    var(--segments), linear-gradient(#0000, #0000);
    [](#L-166)  image-rendering: pixelated;
    [](#L-167)  text-shadow:
    [](#L-168)    -1px -1px 0 black,
    [](#L-169)    1px 1px 0 black,
    [](#L-170)    -1px 1px 0 black,
    [](#L-171)    1px -1px 0 black,
    [](#L-172)    0 -1px 0 black,
    [](#L-173)    0 1px 0 black,
    [](#L-174)    -1px 0 0 black,
    [](#L-175)    1px 0 0 black;
    [](#L-176)  --segments: conic-gradient(
    [](#L-177)    from calc(var(--a-base) - var(--w-inner) - var(--angle)),
    [](#L-178)    var(--c-bg),
    [](#L-179)    var(--c2d) var(--w-inner),
    [](#L-180)    var(--c2l) var(--angle),
    [](#L-181)    var(--c2d) calc((var(--angle) * 2) + var(--w-inner)),
    [](#L-182)    var(--c-bg) calc((var(--angle) * 2) + calc(var(--w-inner) * 2))
    [](#L-183)  );
    [](#L-184)  --segments-mask: conic-gradient(
    [](#L-185)    from calc(var(--a-base) - var(--w-outer) - var(--angle)),
    [](#L-186)    transparent 0 calc((var(--angle) * 2) + calc(var(--w-outer) * 2)),
    [](#L-187)    var(--c-bg) calc((var(--angle) * 2) + calc(var(--w-outer) * 2))
    [](#L-188)  );
    [](#L-189)  --ray-beams: repeating-conic-gradient(
    [](#L-190)    from calc(var(--a-base) - calc(var(--w-inner) * 2) - var(--angle)),
    [](#L-191)    transparent,
    [](#L-192)    var(--c-inner) calc(var(--w-inner) * 1) calc(var(--w-inner) * 3),
    [](#L-193)    transparent calc(var(--w-inner) * 4) calc(var(--dangle))
    [](#L-194)  );
    [](#L-195)  --ray-shadows: repeating-conic-gradient(
    [](#L-196)    from calc(var(--a-base) - calc(var(--w-outer) * 2) - var(--angle)),
    [](#L-197)    transparent,
    [](#L-198)    var(--c-outer) calc(var(--w-outer) * 1) calc(var(--w-outer) * 3),
    [](#L-199)    transparent calc(var(--w-outer) * 4) calc(var(--dangle))
    [](#L-200)  );
    [](#L-201)  background-position: var(--bgpos);
    [](#L-202)  --bg-y: calc(
    [](#L-203)    var(--bg-offy) + (var(--wand-extent) * cos(var(--wand-direction) - 180deg))
    [](#L-204)  );
    [](#L-205)  --bg-x: calc(
    [](#L-206)    var(--bg-offx) + (var(--wand-extent) * sin(var(--wand-direction)))
    [](#L-207)  );
    [](#L-208)  --wand-length: 16px;
    [](#L-209)  --arm-length: 4px;
    [](#L-210)  --wand-voff: -1px;
    [](#L-211)  --wand-extent: calc(
    [](#L-212)    (var(--wand-length) + var(--arm-length) - 1px) * var(--mina-scale)
    [](#L-213)  );
    [](#L-214)  /* Points at cursor relative to where it currently is */
    [](#L-215)  /*--wand-direction: calc((var(--cursor-angle) * 1rad) - 90deg); */
    [](#L-216)  /* Points at cursor relative to the viewport center */
    [](#L-217)  --wand-direction: calc(var(--cursor-client-angle) * -1rad);
    [](#L-218)  --bg-offx: 50%;
    [](#L-219)  --bg-offy: 30%;
    [](#L-220)  --offby: 0;
    [](#L-221)  --mina-scale: 2;
    [](#L-222)  --bgsize: calc(var(--bsize) + (var(--wand-extent) * 2))
    [](#L-223)    calc(var(--bsize) + (var(--wand-extent) * 2));
    [](#L-224)  --bgpos: var(--bg-x) var(--bg-y);
    [](#L-225)  --mina-body: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAAQBAMAAADHbRP9AAAAFVBMVEUAAACbb5p/VHYnISVZQ1TRmz3bwGcqwW/AAAAAAXRSTlMAQObYZgAAADJJREFUeF4txcENABAURMH3S1ga+EGcFUP/rdiEw2QgBFpQrVtLkJUkPBrP2X5aEp+UF3WjA+KEufTyAAAAAElFTkSuQmCC');
    [](#L-226)  --mina-wand: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAICAIAAABGc1mbAAAABnRSTlMAAAAAAABupgeRAAAANklEQVR4nGNgoCvQKd9Asur///9BuIxoBry/tEdQzwVCMjAw1Ga7Q8TD5TgJm2qy6w1V3YoGABTFEyRlTe82AAAAAElFTkSuQmCC');
    [](#L-227)  --mina-wandarm: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAFBAMAAAC+xnF6AAAAJFBMVEUAAACabpmabpqAVXeATYCZZpmec5obSWz///4sd7A0uuyp4vc5G+IiAAAABnRSTlMA9/X3CgqPuwmIAAAAMklEQVR4XjXKoQ0AIBTE0BoEmh2Yg7XOMQL2gmGPvxzJDzzZlFT51qR1W9oBI8uhvOcCgJoGS+xsVvQAAAAASUVORK5CYII=');
    [](#L-228)  height: auto;
    [](#L-229)  min-width: 200px;
    [](#L-230)  transform: scale(1);
    [](#L-231)  align-items: end;
    [](#L-232)  justify-content: space-between;
    [](#L-233)}
    [](#L-234)
    [](#L-235).formation-angle::before {
    [](#L-236)  content: '';
    [](#L-237)  image-rendering: pixelated;
    [](#L-238)  position: absolute;
    [](#L-239)  --top: calc(70% - (var(--height) * var(--mina-scale) * 0.5) - 1px);
    [](#L-240)  top: var(--top);
    [](#L-241)  --left: calc(50% - 3px);
    [](#L-242)  left: var(--left);
    [](#L-243)  background-image: var(--mina-body);
    [](#L-244)  background-size: contain;
    [](#L-245)  --background-position: calc(-1px * var(--mina-scale)) 50%;
    [](#L-246)  background-position: var(--background-position);
    [](#L-247)  background-repeat: no-repeat;
    [](#L-248)  --filter: drop-shadow(-2px 0.4px 1.2px var(--c-bg)) drop-shadow(0 0 0px #aaa);
    [](#L-249)  filter: var(--filter);
    [](#L-250)  width: auto;
    [](#L-251)  aspect-ratio: 6/16;
    [](#L-252)  --height: 28px;
    [](#L-253)  --scaled-height: calc(var(--height) * var(--mina-scale));
    [](#L-254)  height: var(--scaled-height);
    [](#L-255)  --transform: scaleX(
    [](#L-256)    calc(round(nearest, 1 + sin(var(--wand-direction)), 2) - 1)
    [](#L-257)  );
    [](#L-258)  transform: var(--transform);
    [](#L-259)  transform-origin: 1.5px center;
    [](#L-260)}
    [](#L-261)
    [](#L-262).formation-angle::after {
    [](#L-263)  content: '';
    [](#L-264)  image-rendering: pixelated;
    [](#L-265)  position: absolute;
    [](#L-266)  --top: calc(70% - (var(--height) * 0.5));
    [](#L-267)  top: var(--top);
    [](#L-268)  right: 0;
    [](#L-269)  --left: calc(50% - (1.5px * var(--mina-scale)));
    [](#L-270)  left: var(--left);
    [](#L-271)  background-size: contain;
    [](#L-272)  background-position: 50% 50%;
    [](#L-273)  background-repeat: no-repeat;
    [](#L-274)  background-image: var(--mina-wandarm);
    [](#L-275)  --filter: drop-shadow(-2px 0.4px 1.2px var(--c-bg)) drop-shadow(0 0 0px #aaa);
    [](#L-276)  filter: var(--filter);
    [](#L-277)  --height: calc(14px * var(--mina-scale));
    [](#L-278)  height: var(--height);
    [](#L-279)  width: var(--wand-extent);
    [](#L-280)  --transform: rotate(calc(var(--wand-direction) - 90deg));
    [](#L-281)  transform: var(--transform);
    [](#L-282)  transform-origin: 1.5px center;
    [](#L-283)}
    
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
