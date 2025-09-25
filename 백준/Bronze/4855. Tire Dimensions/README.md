# [Bronze II] Tire Dimensions - 4855 

[문제 링크](https://www.acmicpc.net/problem/4855) 

### 성능 요약

메모리: 34536 KB, 시간: 56 ms

### 분류

사칙연산, 구현, 수학, 파싱, 문자열

### 제출 일자

2025년 9월 26일 01:45:49

### 문제 설명

<p>Given the tire descriptor typically found on the sidewall of a passenger or light truck tire, you will calculate the tire's overall circumference. Each line of the sample input contains an example of a tire descriptor. The following diagram illustrates some of the terminology:</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/4855/definitions.gif" style="height:358px; width:367px"></p>

<p>The tire descriptor contains the following items of information:</p>

<ol>
	<li>One or two upper case letters to specify the type of tire. For our purposes, the tire types are "P" (passenger), "LT" (light truck), and "T" (temporary spare tire).</li>
	<li>The <em>section width</em> (of an inflated tire) in millimeters. This number is followed by a slash.</li>
	<li>The ratio of the section height to the section width, expressed as a percentage. For example, the ratio 75 means that the section height of an inflated tire is 75% of its section width.</li>
	<li>Information about the <em>construction</em> of the tire (one upper-case letter), optionally preceded by the <em>speed symbol</em> (also one upper-case letter). In the first, second, and fourth lines of the sample output, the tire construction is specified by "R", which means "radial". In the third line, it is "D", which means "diagonal". In the second line, "R" is preceded by the optional speed symbol "H".</li>
	<li>The nominal rim diameter in inches. It is called "nominal" because it does not include the rim's flanges.</li>
</ol>

<p>The <em>overall circumference</em> (the goal of your calculations) is based on the <em>overall diameter</em>, which is the diameter of an inflated tire at the outermost surface of the tread.</p>

### 입력 

 <p>The input will consist of one or more lines, terminated by end-of-file. Each line of the input will contain one tire descriptor, as discussed in the preceding paragraphs. All numerical quantities will be positive integers. Exactly one blank space will separate consecutive items (including the slash) on the input line.</p>

### 출력 

 <p>For each line of input, the program will produce exactly one line of output, consisting of: the input line, followed by a colon, one blank space, and the overall circumference, expressed in centimeters, rounded to the nearest integer. Note that 1 centimeter equals 10 millimeters, and 1 inch equals 2.54 centimeters.</p>

