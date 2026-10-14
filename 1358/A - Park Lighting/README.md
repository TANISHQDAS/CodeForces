<h2><a href="https://codeforces.com/contest/1358/problem/A" target="_blank" rel="noopener noreferrer">1358A — Park Lighting</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1358A](https://codeforces.com/contest/1358/problem/A) |

## Topics
`greedy` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Park Lighting</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Due to the coronavirus pandemic, city authorities obligated citizens to keep a social distance. The mayor of the city Semyon wants to light up Gluharniki park so that people could see each other even at night to keep the social distance.</p><p>The park is a rectangular table with $$$n$$$ rows and $$$m$$$ columns, where the cells of the table are squares, and the boundaries between the cells are streets. External borders are also streets. Every street has length $$$1$$$. For example, park with $$$n=m=2$$$ has $$$12$$$ streets.</p><p>You were assigned to develop a plan for lighting the park. You can put lanterns in the middle of the streets. The lamp lights two squares near it (or only one square if it stands on the border of the park).</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/7df5389fd8c341033accde7fd22d03802e1fd9e1.png" style="zoom: 15.0%;max-width: 100.0%;max-height: 100.0%;">   <span class="tex-font-size-small">The park sizes are: $$$n=4$$$, $$$m=5$$$. The lighted squares are marked yellow. Please note that all streets have length $$$1$$$. Lanterns are placed in the middle of the streets. In the picture <span class="tex-font-style-bf">not all</span> the squares are lit.</span> </center><p>Semyon wants to spend the least possible amount of money on lighting but also wants people throughout the park to keep a social distance. So he asks you to find the minimum number of lanterns that are required to light all the squares.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases in the input. Then $$$t$$$ test cases follow.</p><p>Each test case is a line containing two integers $$$n$$$, $$$m$$$ ($$$1 \le n, m \le 10^4$$$) — park sizes.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$t$$$ answers to the test cases. Each answer must be a single integer — the minimum number of lanterns that are required to light all the squares.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008667430741702224" id="id0026246585347996365" class="input-output-copier">Copy</div></div><pre id="id008667430741702224">5
1 1
1 3
2 2
3 3
5 3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005000300930474176" id="id0007927489887226169" class="input-output-copier">Copy</div></div><pre id="id005000300930474176">1
2
2
5
8
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>Possible optimal arrangement of the lanterns for the $$$2$$$-nd test case of input data example: <img class="tex-graphics" src="https://espresso.codeforces.com/ea885fae2457a5c0d0494300d1cd2279f14fc2a2.png" style="max-width: 100.0%;max-height: 100.0%;"></p><p>Possible optimal arrangement of the lanterns for the $$$3$$$-rd test case of input data example: <img class="tex-graphics" src="https://espresso.codeforces.com/d2647da857f242032940a341ee0f72cd7a3713d9.png" style="max-width: 100.0%;max-height: 100.0%;"> </p></div>