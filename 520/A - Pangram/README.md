<h2><a href="https://codeforces.com/contest/520/problem/A" target="_blank" rel="noopener noreferrer">520A — Pangram</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 520A](https://codeforces.com/contest/520/problem/A) |

## Topics
`implementation` `strings`

---

## Problem Statement

<div class="header"><div class="title">A. Pangram</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>A word or a sentence in some language is called a <span class="tex-font-style-it">pangram</span> if all the characters of the alphabet of this language appear in it <span class="tex-font-style-it">at least once</span>. Pangrams are often used to demonstrate fonts in printing or test the output devices.</p><p>You are given a string consisting of lowercase and uppercase Latin letters. Check whether this string is a pangram. We say that the string contains a letter of the Latin alphabet if this letter occurs in the string in uppercase or lowercase.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer <span class="tex-span"><i>n</i></span> (<span class="tex-span">1 ≤ <i>n</i> ≤ 100</span>) — the number of characters in the string.</p><p>The second line contains the string. The string consists only of uppercase and lowercase Latin letters.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Output "<span class="tex-font-style-tt">YES</span>", if the string is a pangram and "<span class="tex-font-style-tt">NO</span>" otherwise.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005391913662288502" id="id004979632287514424" class="input-output-copier">Copy</div></div><pre id="id005391913662288502">12<br>toosmallword<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009543515596981655" id="id0028483041053717273" class="input-output-copier">Copy</div></div><pre id="id009543515596981655">NO<br></pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0021003626303663692" id="id003896392017063315" class="input-output-copier">Copy</div></div><pre id="id0021003626303663692">35<br>TheQuickBrownFoxJumpsOverTheLazyDog<br></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005512501754244351" id="id006556405486140158" class="input-output-copier">Copy</div></div><pre id="id005512501754244351">YES<br></pre></div></div></div>